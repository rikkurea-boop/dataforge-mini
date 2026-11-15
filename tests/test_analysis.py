"""Unit tests cho module analysis.py (bao phủ OR-01..06, OR-09..13, OR-15 và IO-01..10)."""

import io
import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from analysis import (
    MAX_CSV_BYTES,
    clean_data,
    inspect_data,
    load_csv,
    mean_by_group,
    numeric_stats,
)

SAMPLE_CSV_PATH = Path(__file__).resolve().parent.parent / "sample_data.csv"


def test_sample_raw_profile_or01():
    """OR-01: Dataset chuẩn có 12x4, 2 duplicate toàn dòng, 2 ô thiếu và đúng kiểu cột."""
    raw = load_csv(SAMPLE_CSV_PATH)
    profile = inspect_data(raw)

    assert profile == {
        "rows": 12,
        "columns": 4,
        "missing_cells": 2,
        "duplicate_rows": 2,
    }
    num_cols = list(raw.select_dtypes(include="number").columns)
    text_cols = list(raw.select_dtypes(include=["object", "string", "category"]).columns)
    assert set(num_cols) == {"gio_hoc", "diem"}
    assert set(text_cols) == {"ten", "lop"}


def test_clean_data_canonical_or02_or03_or15():
    """OR-02/03/15: Xóa trùng trước rồi điền median (4 và 8), không làm đổi bảng raw."""
    raw = load_csv(SAMPLE_CSV_PATH)
    raw_snapshot = raw.copy(deep=True)

    cleaned = clean_data(raw)
    cleaned_profile = inspect_data(cleaned)

    assert cleaned_profile == {
        "rows": 10,
        "columns": 4,
        "missing_cells": 0,
        "duplicate_rows": 0,
    }
    # Bảng raw không bị thay đổi sau clean_data
    pd.testing.assert_frame_equal(raw, raw_snapshot)

    # Kiểm tra đúng 2 ô được điền theo oracle
    minh_hours = cleaned.loc[cleaned["ten"] == "Minh", "gio_hoc"].iloc[0]
    ngoc_grade = cleaned.loc[cleaned["ten"] == "Ngoc", "diem"].iloc[0]
    assert minh_hours == pytest.approx(4.0)
    assert ngoc_grade == pytest.approx(8.0)

    # OR-15: cùng raw luôn cho kết quả cleaned giống nhau
    pd.testing.assert_frame_equal(cleaned, clean_data(raw_snapshot))


def test_numeric_stats_and_groupby_or04_or05_or06():
    """OR-04/05/06: Thống kê NumPy dùng ddof=0 và trung bình nhóm A=8.0, B=7.6."""
    cleaned = clean_data(load_csv(SAMPLE_CSV_PATH))
    grade_stats = numeric_stats(cleaned, "diem")
    hours_stats = numeric_stats(cleaned, "gio_hoc")

    assert grade_stats["count"] == 10
    assert grade_stats["min"] == pytest.approx(6.0)
    assert grade_stats["max"] == pytest.approx(10.0)
    assert grade_stats["mean"] == pytest.approx(7.8)
    assert grade_stats["median"] == pytest.approx(8.0)
    assert grade_stats["std"] == pytest.approx(math.sqrt(1.56))
    assert hours_stats["mean"] == pytest.approx(4.4)

    grouped = mean_by_group(cleaned, "lop", "diem")
    assert grouped["A"] == pytest.approx(8.0)
    assert grouped["B"] == pytest.approx(7.6)


def test_edge_all_na_and_singleton_or09_or10():
    """OR-09/10: Cột số toàn NaN trả về None; cột 1 giá trị trả về std=0."""
    df_all_na = pd.DataFrame({"x": [np.nan, np.nan]})
    cleaned_na = clean_data(df_all_na)
    assert cleaned_na["x"].isna().all()
    assert numeric_stats(cleaned_na, "x") == {
        "count": 0,
        "min": None,
        "max": None,
        "mean": None,
        "median": None,
        "std": None,
    }

    df_single = pd.DataFrame({"x": [7.5, np.nan]})
    stats_single = numeric_stats(df_single, "x")
    assert stats_single["count"] == 1
    assert stats_single["min"] == pytest.approx(7.5)
    assert stats_single["max"] == pytest.approx(7.5)
    assert stats_single["mean"] == pytest.approx(7.5)
    assert stats_single["median"] == pytest.approx(7.5)
    assert stats_single["std"] == pytest.approx(0.0)


def test_groupby_missing_keys_and_all_na_group_or11():
    """OR-11: Bỏ nhóm có nhãn NA; nhóm không có giá trị số hợp lệ giữ NaN chứ không thành 0."""
    df = pd.DataFrame(
        {
            "lop": ["A", "B", None, "C"],
            "diem": [8.0, 6.0, 9.0, np.nan],
        }
    )
    grouped = mean_by_group(df, "lop", "diem")

    assert list(grouped.index) == ["A", "B", "C"]
    assert grouped["A"] == pytest.approx(8.0)
    assert grouped["B"] == pytest.approx(6.0)
    assert math.isnan(grouped["C"])


def test_imputation_creates_duplicate_no_second_drop_or12():
    """OR-12: Điền trung vị có thể tạo dòng trùng mới; không drop trùng lần hai."""
    df = pd.DataFrame({"nhom": ["X", "X", "Y"], "val": [1.0, np.nan, 1.0]})
    cleaned = clean_data(df)
    profile = inspect_data(cleaned)

    assert profile["rows"] == 3
    assert profile["missing_cells"] == 0
    assert profile["duplicate_rows"] == 1


def test_reject_infinity_or13():
    """OR-13: Từ chối giá trị vô cực (+inf/-inf) khi load, clean, tính stats và groupby."""
    csv_inf = io.StringIO("lop,diem\nA,inf\nB,8\n")
    with pytest.raises(ValueError):
        load_csv(csv_inf)

    df_inf = pd.DataFrame({"lop": ["A", "B"], "diem": [np.inf, 8.0]})
    with pytest.raises(ValueError):
        clean_data(df_inf)
    with pytest.raises(ValueError):
        numeric_stats(df_inf, "diem")
    with pytest.raises(ValueError):
        mean_by_group(df_inf, "lop", "diem")


def test_io_validation_and_roundtrip_io01_to_io10():
    """IO-01..10: Kiểm tra file rỗng, BOM, lỗi UTF-8, dấu ';', header trùng/trống, >2MiB và roundtrip."""
    # IO-01: file rỗng / chỉ có khoảng trắng
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"   \n  "))

    # IO-02: chỉ có header, 0 dòng dữ liệu
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,lop,diem\n"))

    # IO-03: thừa cột / không đều / lỗi quoting
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,diem\nAn,8,extra\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,diem\nAn,8\nBinh,9,extra\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b'ten,diem\n"An,8\n'))

    # IO-04: UTF-8 BOM được đọc sạch tên cột
    bom_bytes = "\ufefften,lop,diem\nAn,A,8\n".encode("utf-8")
    df_bom = load_csv(io.BytesIO(bom_bytes))
    assert list(df_bom.columns) == ["ten", "lop", "diem"]

    # IO-05: sai mã hóa UTF-8
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"\xff\xfe\x00\x00"))

    # IO-06: dấu chấm phẩy không được tự đoán
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten;lop;diem\nAn;A;8\n"))

    # IO-07: header trống hoặc trùng tên cột
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,,diem\nAn,A,8\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,ten,diem\nAn,A,8\n"))

    # IO-08: vượt quá giới hạn 2 MiB
    oversized = io.BytesIO(b"a,b\n" + b"1,2\n" * (MAX_CSV_BYTES // 3))
    with pytest.raises(ValueError):
        load_csv(oversized)

    # IO-09: chữ giống số ("8a") giữ nguyên dạng chữ, không ép thành số
    df_mixed = load_csv(io.BytesIO(b"ten,diem\nAn,8a\nBinh,9\n"))
    assert "diem" not in df_mixed.select_dtypes(include="number").columns
    with pytest.raises(ValueError):
        numeric_stats(df_mixed, "diem")

    # IO-10: roundtrip export CSV (index=False, utf-8-sig) giữ nguyên 10x4 của bảng đã clean
    cleaned = clean_data(load_csv(SAMPLE_CSV_PATH))
    exported_bytes = cleaned.to_csv(index=False).encode("utf-8-sig")
    reloaded = load_csv(io.BytesIO(exported_bytes))
    assert reloaded.shape == (10, 4)
    assert list(reloaded.columns) == ["ten", "lop", "gio_hoc", "diem"]

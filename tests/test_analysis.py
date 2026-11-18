"""Kiểm thử tự động cho xử lý dữ liệu (analysis), biểu đồ (charts) và giao diện (app)."""

import io
import json
import math
import subprocess
import zipfile
from pathlib import Path
from unittest.mock import patch

from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

import app
from analysis import (
    MAX_CSV_BYTES,
    clean_data,
    column_profile,
    correlation_matrix,
    filter_data,
    inspect_data,
    load_csv,
    mean_by_group,
    numeric_stats,
)
from charts import boxplot, correlation_heatmap, group_bar, histogram, scatter

SAMPLE_CSV_PATH = Path(__file__).resolve().parent.parent / "sample_data.csv"


def test_sample_raw_profile():
    """Dataset mẫu ban đầu có 12x4, 2 dòng trùng toàn phần, 2 ô thiếu và đúng kiểu cột."""
    raw = load_csv(SAMPLE_CSV_PATH)
    profile = inspect_data(raw)

    assert profile == {
        "rows": 12,
        "columns": 4,
        "missing_cells": 2,
        "duplicate_rows": 2,
    }
    col_table = column_profile(raw)
    assert list(col_table["Cột"]) == ["ten", "lop", "gio_hoc", "diem"]
    assert col_table.loc[col_table["Cột"] == "diem", "Ô thiếu"].iloc[0] == 1

    num_cols = list(raw.select_dtypes(include="number").columns)
    text_cols = list(raw.select_dtypes(include=["object", "string", "category"]).columns)
    assert set(num_cols) == {"gio_hoc", "diem"}
    assert set(text_cols) == {"ten", "lop"}


def test_clean_data_canonical_and_strategies():
    """Xóa dòng trùng trước rồi điền trung vị/trung bình/xóa thiếu, giữ nguyên bảng gốc."""
    raw = load_csv(SAMPLE_CSV_PATH)
    raw_snapshot = raw.copy(deep=True)

    cleaned = clean_data(raw)
    assert inspect_data(cleaned) == {
        "rows": 10,
        "columns": 4,
        "missing_cells": 0,
        "duplicate_rows": 0,
    }
    pd.testing.assert_frame_equal(raw, raw_snapshot)

    assert cleaned.loc[cleaned["ten"] == "Minh", "gio_hoc"].iloc[0] == pytest.approx(4.0)
    assert cleaned.loc[cleaned["ten"] == "Ngoc", "diem"].iloc[0] == pytest.approx(8.0)
    pd.testing.assert_frame_equal(cleaned, clean_data(raw_snapshot))

    # Chiến lược điền trung bình (mean) và xóa dòng thiếu (drop)
    cleaned_mean = clean_data(raw, remove_duplicates=True, missing_strategy="mean")
    assert inspect_data(cleaned_mean)["rows"] == 10
    assert cleaned_mean.loc[cleaned_mean["ten"] == "Ngoc", "diem"].iloc[0] == pytest.approx(70.0 / 9.0)

    cleaned_drop = clean_data(raw, remove_duplicates=True, missing_strategy="drop")
    assert inspect_data(cleaned_drop) == {
        "rows": 8,
        "columns": 4,
        "missing_cells": 0,
        "duplicate_rows": 0,
    }

    with pytest.raises(ValueError):
        clean_data(raw, missing_strategy="unknown")


def test_numeric_stats_and_groupby():
    """Thống kê NumPy dùng ddof=0, Q1/Q3/IQR/outliers và trung bình nhóm A=8.0, B=7.6."""
    cleaned = clean_data(load_csv(SAMPLE_CSV_PATH))
    grade_stats = numeric_stats(cleaned, "diem")
    hours_stats = numeric_stats(cleaned, "gio_hoc")

    assert grade_stats["count"] == 10
    assert grade_stats["min"] == pytest.approx(6.0)
    assert grade_stats["max"] == pytest.approx(10.0)
    assert grade_stats["mean"] == pytest.approx(7.8)
    assert grade_stats["median"] == pytest.approx(8.0)
    assert grade_stats["std"] == pytest.approx(math.sqrt(1.56))
    assert grade_stats["q1"] == pytest.approx(7.0)
    assert grade_stats["q3"] == pytest.approx(8.75)
    assert grade_stats["iqr"] == pytest.approx(1.75)
    assert grade_stats["outliers"] == 0
    assert hours_stats["mean"] == pytest.approx(4.4)

    grouped = mean_by_group(cleaned, "lop", "diem")
    assert grouped["A"] == pytest.approx(8.0)
    assert grouped["B"] == pytest.approx(7.6)

    corr = correlation_matrix(cleaned)
    assert corr.shape == (2, 2)
    assert corr.loc["gio_hoc", "diem"] > 0.9


def test_filter_data_and_outliers():
    """Lọc theo nhóm, lọc theo khoảng số và đếm ngoại lai IQR."""
    cleaned = clean_data(load_csv(SAMPLE_CSV_PATH))
    only_a = filter_data(cleaned, group_column="lop", selected_groups=["A"])
    assert len(only_a) == 5
    assert set(only_a["lop"]) == {"A"}

    high_scores = filter_data(cleaned, numeric_column="diem", value_range=(8.0, 10.0))
    assert len(high_scores) == 6
    assert high_scores["diem"].min() >= 8.0

    df_out = pd.DataFrame({"val": [10, 11, 12, 11, 10, 12, 50]})
    assert numeric_stats(df_out, "val")["outliers"] == 1


def test_edge_all_na_and_singleton():
    """Cột số toàn NaN trả về None; cột chỉ có 1 giá trị trả về std=0."""
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
        "q1": None,
        "q3": None,
        "iqr": None,
        "outliers": 0,
    }

    df_single = pd.DataFrame({"x": [7.5, np.nan]})
    stats_single = numeric_stats(df_single, "x")
    assert stats_single["count"] == 1
    assert stats_single["min"] == pytest.approx(7.5)
    assert stats_single["max"] == pytest.approx(7.5)
    assert stats_single["mean"] == pytest.approx(7.5)
    assert stats_single["median"] == pytest.approx(7.5)
    assert stats_single["std"] == pytest.approx(0.0)
    assert stats_single["iqr"] == pytest.approx(0.0)
    assert stats_single["outliers"] == 0


def test_groupby_missing_keys_and_all_na_group():
    """Bỏ nhóm có nhãn NA; nhóm không có giá trị số hợp lệ giữ NaN chứ không thành 0."""
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


def test_imputation_creates_duplicate_no_second_drop():
    """Điền trung vị có thể tạo dòng trùng mới; không xóa trùng lần thứ hai."""
    df = pd.DataFrame({"nhom": ["X", "X", "Y"], "val": [1.0, np.nan, 1.0]})
    cleaned = clean_data(df)
    profile = inspect_data(cleaned)

    assert profile["rows"] == 3
    assert profile["missing_cells"] == 0
    assert profile["duplicate_rows"] == 1


def test_reject_infinity():
    """Từ chối giá trị vô cực (+inf/-inf) khi đọc, làm sạch, tính stats, groupby và corr."""
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
    with pytest.raises(ValueError):
        correlation_matrix(df_inf)


def test_io_validation_and_roundtrip():
    """Kiểm tra file rỗng, BOM, lỗi UTF-8, dấu ';', header trùng/trống, >2 MiB và roundtrip."""
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"   \n  "))

    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,lop,diem\n"))

    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,diem\nAn,8,extra\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,diem\nAn,8\nBinh,9,extra\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b'ten,diem\n"An,8\n'))

    bom_bytes = "\ufefften,lop,diem\nAn,A,8\n".encode("utf-8")
    df_bom = load_csv(io.BytesIO(bom_bytes))
    assert list(df_bom.columns) == ["ten", "lop", "diem"]

    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"\xff\xfe\x00\x00"))

    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten;lop;diem\nAn;A;8\n"))

    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,,diem\nAn,A,8\n"))
    with pytest.raises(ValueError):
        load_csv(io.BytesIO(b"ten,ten,diem\nAn,A,8\n"))

    oversized = io.BytesIO(b"a,b\n" + b"1,2\n" * (MAX_CSV_BYTES // 3))
    with pytest.raises(ValueError):
        load_csv(oversized)

    df_mixed = load_csv(io.BytesIO(b"ten,diem\nAn,8a\nBinh,9\n"))
    assert "diem" not in df_mixed.select_dtypes(include="number").columns
    with pytest.raises(ValueError):
        numeric_stats(df_mixed, "diem")

    cleaned = clean_data(load_csv(SAMPLE_CSV_PATH))
    exported_bytes = cleaned.to_csv(index=False).encode("utf-8-sig")
    reloaded = load_csv(io.BytesIO(exported_bytes))
    assert reloaded.shape == (10, 4)
    assert list(reloaded.columns) == ["ten", "lop", "gio_hoc", "diem"]


def test_charts_canonical_figures():
    """Kiểm tra 5 biểu đồ Matplotlib (histogram, bar, scatter, boxplot, heatmap) trên mẫu chuẩn."""
    raw = load_csv(SAMPLE_CSV_PATH)
    cleaned = clean_data(raw)

    fig_hist = histogram(cleaned, "diem")
    assert isinstance(fig_hist, Figure)
    ax_hist = fig_hist.axes[0]
    counts = [patch.get_height() for patch in ax_hist.patches]
    assert counts == pytest.approx([2.0, 2.0, 3.0, 2.0, 1.0])
    assert sum(counts) == pytest.approx(10.0)
    assert ax_hist.get_ylabel() == "Số quan sát"
    assert ax_hist.get_xlabel() == "diem"

    means = mean_by_group(cleaned, "lop", "diem")
    fig_bar = group_bar(means)
    assert isinstance(fig_bar, Figure)
    ax_bar = fig_bar.axes[0]
    bar_heights = [patch.get_height() for patch in ax_bar.patches]
    assert bar_heights == pytest.approx([8.0, 7.6])
    assert ax_bar.get_ylim()[0] == pytest.approx(0.0)
    assert ax_bar.get_ylabel() == "Trung bình"

    for df_case in (raw, cleaned):
        fig_scatter = scatter(df_case, "gio_hoc", "diem")
        assert isinstance(fig_scatter, Figure)
        offsets = fig_scatter.axes[0].collections[0].get_offsets()
        expected_pairs = df_case[["gio_hoc", "diem"]].dropna().to_numpy(dtype=float)
        assert len(offsets) == 10
        assert np.allclose(offsets, expected_pairs)

    fig_box = boxplot(cleaned, "diem", "lop")
    assert isinstance(fig_box, Figure)
    assert [t.get_text() for t in fig_box.axes[0].get_xticklabels()] == ["A", "B"]

    fig_heat = correlation_heatmap(correlation_matrix(cleaned))
    assert isinstance(fig_heat, Figure)
    assert len(fig_heat.axes[0].texts) == 4


def test_charts_edge_cases_and_app_import():
    """Loại nhóm NaN, chặn ±inf/all-NA/0-cặp/trùng cột và kiểm tra import app."""
    fig_partial = group_bar(pd.Series([8.0, np.nan], index=["A", "C"]))
    assert len(fig_partial.axes[0].patches) == 1

    df_empty_num = pd.DataFrame({"x": [np.nan, np.nan], "y": [1.0, 2.0]})
    with pytest.raises(ValueError):
        histogram(df_empty_num, "x")
    with pytest.raises(ValueError):
        boxplot(df_empty_num, "x")
    with pytest.raises(ValueError):
        group_bar(pd.Series([np.nan, np.nan], index=["A", "B"]))
    with pytest.raises(ValueError):
        scatter(pd.DataFrame({"x": [1.0, np.nan], "y": [np.nan, 2.0]}), "x", "y")
    with pytest.raises(ValueError):
        scatter(pd.DataFrame({"x": [1.0, 2.0]}), "x", "x")
    with pytest.raises(ValueError):
        correlation_heatmap(pd.DataFrame({"x": [1.0]}))

    df_inf = pd.DataFrame({"x": [1.0, np.inf], "y": [2.0, 3.0]})
    with pytest.raises(ValueError):
        histogram(df_inf, "x")
    with pytest.raises(ValueError):
        scatter(df_inf, "x", "y")
    with pytest.raises(ValueError):
        boxplot(df_inf, "x")
    with pytest.raises(ValueError):
        group_bar(pd.Series([1.0, np.inf], index=["A", "B"]))

    assert callable(app.main)
    assert SAMPLE_CSV_PATH.exists()


class _FakeUpload(io.BytesIO):
    """Stream giả lập file tải lên có thuộc tính name và size để kiểm thử giao diện."""

    def __init__(self, data: bytes, name: str = "custom.csv", size: int | None = None):
        super().__init__(data)
        self.name = name
        self.size = len(data) if size is None else size


def test_streamlit_ui_flows():
    """Kiểm thử toàn bộ luồng giao diện mới: ẩn ban đầu, làm sạch, xác nhận, lọc & xuất báo cáo."""
    app_path = Path(__file__).resolve().parent.parent / "app.py"

    # 1. Chưa tải file: ẩn hoàn toàn bảng, checkbox, selectbox, chỉ hiện nút cập nhật + thông báo
    at_empty = AppTest.from_file(str(app_path)).run()
    assert not at_empty.exception
    assert len(at_empty.checkbox) == 0
    assert len(at_empty.button) == 1
    assert at_empty.button[0].label == "↻ Cập nhật"
    assert len(at_empty.dataframe) == 0
    assert len(at_empty.metric) == 0
    assert len(at_empty.info) == 1

    # 2. Đã tải sample_data.csv lên nhưng chưa bấm xác nhận
    sample_bytes = SAMPLE_CSV_PATH.read_bytes()
    with patch(
        "streamlit.file_uploader",
        side_effect=lambda *args, **kwargs: _FakeUpload(sample_bytes, name="sample_data.csv"),
    ):
        at = AppTest.from_file(str(app_path)).run()
        assert not at.exception
        assert len(at.checkbox) == 1
        assert len(at.selectbox) == 1  # chọn chiến lược điền thiếu
        assert len(at.button) == 2
        assert len(at.dataframe) == 0

        # 3. Bấm xác nhận với mặc định Raw (không xóa trùng, giữ ô thiếu)
        at.button[1].click().run()
        assert not at.exception
        assert len(at.get("download_button")) == 2  # CSV + báo cáo .txt
        assert len(at.metric) == 10
        assert at.metric[0].value == "11"
        assert at.metric[2].value == "7.73"

        # 4. Bật xóa trùng + chọn Điền trung vị (Median) -> bấm xác nhận
        at.checkbox[0].check().run()
        at.selectbox[0].select("Điền trung vị (Median)").run()
        assert len(at.dataframe) == 0  # chờ bấm xác nhận lại
        at.button[1].click().run()
        assert not at.exception

        summary_rows = at.dataframe[0].value.to_dict(orient="records")
        assert summary_rows[0]["Số dòng"] == 12
        assert summary_rows[1]["Số dòng"] == 10
        assert summary_rows[1]["Ô thiếu"] == 0
        assert summary_rows[1]["Dòng trùng"] == 0

        assert at.metric[0].value == "10"
        assert at.metric[2].value == "7.8"
        assert at.metric[5].value == "1.25"

        # 5. Đổi cột Y trên selectbox và lọc riêng nhóm A
        at.selectbox[1].select("gio_hoc").run()
        assert not at.exception
        assert at.metric[2].value == "4.4"

        at.multiselect[0].unselect("B").run()
        assert not at.exception
        assert at.metric[0].value == "5"

    assert app._format_num(40.0) == "40"
    assert app._format_num(7.8000) == "7.8"
    assert app._format_num(39.4444) == "39.44"
    assert app._format_num(-0.001) == "0"

    # 6. Kiểm tra đọc file tải lên hợp lệ và chặn file vượt 2 MiB
    custom_df, custom_label = app._load_input_dataframe(
        _FakeUpload(b"ten,lop,gio_hoc,diem\nX,K,5,9\nY,K,7,10\n", name="lop_k.csv")
    )
    assert custom_df.shape == (2, 4)
    assert "lop_k.csv" in custom_label

    with pytest.raises(ValueError):
        app._load_input_dataframe(
            _FakeUpload(b"a,b\n1,2\n", name="huge.csv", size=MAX_CSV_BYTES + 1)
        )
    with pytest.raises(ValueError):
        app._load_input_dataframe(None)


def test_auto_update_git_and_zip(tmp_path: Path):
    """Kiểm tra cơ chế tự động cập nhật từ GitHub qua Git và fallback tải ZIP."""
    # 1. Trường hợp dùng Git: chưa có bản mới -> không pull
    git_dir = tmp_path / "repo_git"
    (git_dir / ".git").mkdir(parents=True)

    calls: list[list[str]] = []

    def fake_git_same(cmd, **kwargs):
        calls.append(cmd)
        if "rev-parse" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="abc1234567890\n", stderr="")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with patch("app.shutil.which", return_value="/usr/bin/git"), patch(
        "app.subprocess.run", side_effect=fake_git_same
    ):
        updated, msg = app._check_and_update(git_dir)
    assert updated is False
    assert "abc1234" in msg
    assert not any("pull" in c for c in calls)

    # 2. Trường hợp dùng Git: có commit mới -> thực hiện pull --ff-only
    calls.clear()

    def fake_git_new(cmd, **kwargs):
        calls.append(cmd)
        if cmd[-1] == "HEAD":
            return subprocess.CompletedProcess(cmd, 0, stdout="1111111aaaa\n", stderr="")
        if "origin/main" in cmd and "rev-parse" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="2222222bbbb\n", stderr="")
        return subprocess.CompletedProcess(cmd, 0, stdout="Updating...", stderr="")

    with patch("app.shutil.which", return_value="/usr/bin/git"), patch(
        "app.subprocess.run", side_effect=fake_git_new
    ):
        updated, msg = app._check_and_update(git_dir)
    assert updated is True
    assert "2222222" in msg
    assert any("pull" in c and "--ff-only" in c for c in calls)

    # 3. Trường hợp tải ZIP (không có .git): tải bản mới, giải nén đè & bỏ qua lần kiểm tra sau
    zip_dir = tmp_path / "repo_zip"
    zip_dir.mkdir()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("dataforge-mini-main/README.md", "updated content")
        zf.writestr("dataforge-mini-main/../evil.txt", "blocked")
    zip_bytes = buf.getvalue()

    class _FakeResponse:
        def __init__(self, payload: bytes):
            self._payload = payload

        def read(self) -> bytes:
            return self._payload

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    def fake_urlopen(req, timeout=10):
        url = req.full_url
        if "api.github.com" in url:
            return _FakeResponse(json.dumps({"sha": "9999999cccc"}).encode("utf-8"))
        return _FakeResponse(zip_bytes)

    with patch("app.urllib.request.urlopen", side_effect=fake_urlopen):
        updated, msg = app._check_and_update(zip_dir)
        assert updated is True
        assert "9999999" in msg
        assert (zip_dir / "README.md").read_text(encoding="utf-8") == "updated content"
        assert not (tmp_path / "evil.txt").exists()

        # Lần 2 SHA trùng nhau -> báo đang ở bản mới nhất, không tải ZIP nữa
        updated_again, msg_again = app._check_and_update(zip_dir)
        assert updated_again is False
        assert "9999999" in msg_again

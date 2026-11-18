"""Module xử lý, kiểm tra chất lượng và phân tích dữ liệu dùng Pandas và NumPy."""

import csv
import io
from pathlib import Path
from typing import BinaryIO

import numpy as np
import pandas as pd

MAX_CSV_BYTES = 2 * 1024 * 1024  # Giới hạn 2 MiB cho file CSV đầu vào
VALID_MISSING_STRATEGIES = {"median", "mean", "drop", "keep"}


def _read_csv_bytes(source: str | Path | BinaryIO) -> bytes:
    """Đọc dữ liệu byte từ đường dẫn file hoặc đối tượng stream, kiểm tra giới hạn 2 MiB."""
    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.stat().st_size > MAX_CSV_BYTES:
            raise ValueError("File CSV vượt quá giới hạn cho phép 2 MiB.")
        return path.read_bytes()

    if hasattr(source, "seek"):
        source.seek(0)
    raw = source.read(MAX_CSV_BYTES + 1)
    if hasattr(source, "seek"):
        source.seek(0)

    raw_bytes = raw.encode("utf-8") if isinstance(raw, str) else bytes(raw)
    if len(raw_bytes) > MAX_CSV_BYTES:
        raise ValueError("File CSV vượt quá giới hạn cho phép 2 MiB.")
    return raw_bytes


def _validate_csv_text(text: str) -> None:
    """Kiểm tra tiêu đề CSV và dòng thừa cột trước khi Pandas tự đổi tên hoặc làm lệch cột."""
    rows = [row for row in csv.reader(io.StringIO(text)) if row]
    if not rows:
        raise ValueError("File CSV rỗng, không có dòng tiêu đề.")

    header = rows[0]
    if len(header) == 1 and ";" in header[0]:
        raise ValueError("Định dạng chưa hỗ trợ: chỉ nhận CSV phân cách bằng dấu phẩy (,).")

    cleaned = [col.strip() for col in header]
    if any(col == "" for col in cleaned):
        raise ValueError("Header CSV có tên cột trống.")
    if len(set(cleaned)) != len(cleaned):
        raise ValueError("Header CSV có tên cột bị trùng lặp.")

    for line_no, row in enumerate(rows[1:], start=2):
        if len(row) > len(header):
            raise ValueError(f"Dòng {line_no} có nhiều cột hơn tiêu đề CSV.")


def _check_no_infinity(df: pd.DataFrame) -> None:
    """Chặn các giá trị vô cực (±inf) trong các cột số; vẫn cho phép NaN."""
    num_df = df.select_dtypes(include="number")
    if num_df.empty:
        return
    values = num_df.to_numpy(dtype=float, na_value=0.0)
    if np.isinf(values).any():
        raise ValueError("Dữ liệu chứa giá trị vô cực (±inf), không được hỗ trợ.")


def _require_numeric_column(df: pd.DataFrame, column: str) -> None:
    """Xác nhận cột tồn tại và mang kiểu dữ liệu số."""
    if column not in df.columns:
        raise ValueError(f"Không tìm thấy cột '{column}'.")
    if column not in df.select_dtypes(include="number").columns:
        raise ValueError(f"Cột '{column}' không phải là cột dữ liệu số.")


def load_csv(source: str | Path | BinaryIO) -> pd.DataFrame:
    """Đọc CSV UTF-8 dấu phẩy thành DataFrame và kiểm tra các lỗi đầu vào cơ bản."""
    raw_bytes = _read_csv_bytes(source)
    try:
        text = raw_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("File không đúng bảng mã UTF-8.") from exc

    if not text.strip():
        raise ValueError("File CSV rỗng, không có dữ liệu.")

    _validate_csv_text(text)

    try:
        df = pd.read_csv(io.StringIO(text), sep=",", index_col=False)
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as exc:
        raise ValueError(f"Cú pháp CSV không hợp lệ: {exc}") from exc

    if df.empty:
        raise ValueError("File CSV chỉ có dòng tiêu đề, không có dòng dữ liệu nào.")

    _check_no_infinity(df)
    return df


def inspect_data(df: pd.DataFrame) -> dict[str, int]:
    """Trả về thông số tổng quan của bảng dữ liệu mà không làm thay đổi bảng gốc."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated(keep="first").sum()),
    }


def column_profile(df: pd.DataFrame) -> pd.DataFrame:
    """Tạo bảng kiểm tra chất lượng từng cột (kiểu dữ liệu, số ô thiếu, tỷ lệ thiếu, giá trị duy nhất)."""
    total_rows = max(len(df), 1)
    records = []
    for col in df.columns:
        missing = int(df[col].isna().sum())
        records.append(
            {
                "Cột": str(col),
                "Kiểu dữ liệu": str(df[col].dtype),
                "Hợp lệ": int(df[col].notna().sum()),
                "Ô thiếu": missing,
                "Tỷ lệ thiếu (%)": round(missing * 100.0 / total_rows, 1),
                "Giá trị duy nhất": int(df[col].nunique(dropna=True)),
            }
        )
    return pd.DataFrame(records)


def clean_data(
    df: pd.DataFrame,
    remove_duplicates: bool = True,
    missing_strategy: str = "median",
) -> pd.DataFrame:
    """Tạo bản sao sạch: tùy chọn bỏ dòng trùng toàn phần và xử lý ô thiếu cột số."""
    if missing_strategy not in VALID_MISSING_STRATEGIES:
        raise ValueError(f"Chiến lược xử lý ô thiếu không hợp lệ: '{missing_strategy}'.")

    _check_no_infinity(df)
    cleaned = df.copy(deep=True)

    # Bước 1: bỏ trùng toàn dòng trước khi tính trung vị/trung bình
    if remove_duplicates:
        cleaned = cleaned.drop_duplicates(keep="first").copy()

    # Bước 2: xử lý ô thiếu theo chiến lược đã chọn
    if missing_strategy == "drop":
        return cleaned.dropna().copy()

    if missing_strategy in {"median", "mean"}:
        reducer = np.median if missing_strategy == "median" else np.mean
        for col in cleaned.select_dtypes(include="number").columns:
            if cleaned[col].isna().any():
                valid = cleaned[col].dropna()
                if len(valid) > 0:
                    fill_val = float(reducer(valid.to_numpy(dtype=float)))
                    cleaned[col] = cleaned[col].astype(float).fillna(fill_val)

    return cleaned


def filter_data(
    df: pd.DataFrame,
    group_column: str | None = None,
    selected_groups: list[str] | None = None,
    numeric_column: str | None = None,
    value_range: tuple[float, float] | None = None,
) -> pd.DataFrame:
    """Lọc bảng dữ liệu theo danh sách nhóm và khoảng giá trị số (Pandas boolean indexing)."""
    filtered = df.copy()
    if group_column and selected_groups is not None and group_column in filtered.columns:
        filtered = filtered[filtered[group_column].astype(str).isin(selected_groups)]

    if numeric_column and value_range is not None and numeric_column in filtered.columns:
        _require_numeric_column(filtered, numeric_column)
        low, high = value_range
        # Giữ lại cả dòng có giá trị nằm trong [low, high] hoặc đang trống (nếu chưa clean)
        col_series = filtered[numeric_column]
        filtered = filtered[col_series.isna() | col_series.between(low, high)]

    return filtered


def numeric_stats(df: pd.DataFrame, column: str) -> dict[str, int | float | None]:
    """Tính thống kê mô tả bằng NumPy (ddof=0, Q1/Q3/IQR và số ngoại lai theo quy tắc 1.5*IQR)."""
    _require_numeric_column(df, column)
    _check_no_infinity(df[[column]])

    values = df[column].dropna().to_numpy(dtype=float)
    count = int(values.size)
    if count == 0:
        return {
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

    q1, q3 = (float(v) for v in np.percentile(values, [25, 75]))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outlier_count = int(np.sum((values < lower_bound) | (values > upper_bound)))

    return {
        "count": count,
        "min": float(np.min(values)),
        "max": float(np.max(values)),
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "std": float(np.std(values, ddof=0)),
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "outliers": outlier_count,
    }


def mean_by_group(df: pd.DataFrame, group_column: str, value_column: str) -> pd.Series:
    """Tính giá trị trung bình của cột số theo từng nhóm bằng Pandas GroupBy."""
    if group_column not in df.columns:
        raise ValueError(f"Không tìm thấy cột nhóm '{group_column}'.")
    text_cols = df.select_dtypes(include=["object", "string", "category"]).columns
    if group_column not in text_cols:
        raise ValueError(f"Cột '{group_column}' không phải cột nhóm dạng chữ hoặc phân loại.")

    _require_numeric_column(df, value_column)
    _check_no_infinity(df[[value_column]])

    return df.groupby(group_column, dropna=True, observed=True)[value_column].mean().astype(float)


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Tính ma trận tương quan Pearson cho các cột dữ liệu số."""
    _check_no_infinity(df)
    num_df = df.select_dtypes(include="number")
    if num_df.shape[1] < 2:
        return pd.DataFrame()
    return num_df.corr(method="pearson")

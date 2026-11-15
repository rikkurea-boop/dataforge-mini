"""Module xử lý và phân tích dữ liệu tối giản dùng Pandas và NumPy."""

import csv
import io
from pathlib import Path
from typing import BinaryIO

import numpy as np
import pandas as pd

MAX_CSV_BYTES = 2 * 1024 * 1024  # Giới hạn 2 MiB cho file CSV đầu vào


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
    # Từ chối file dùng dấu chấm phẩy làm phân cách chính
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
        # utf-8-sig tự động loại bỏ UTF-8 BOM nếu có ở đầu file
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


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Tạo bản sao sạch: xóa dòng trùng toàn phần trước, điền trung vị cột số sau."""
    _check_no_infinity(df)
    cleaned = df.copy(deep=True)
    # Bước 1: bỏ trùng toàn dòng trước khi tính trung vị
    cleaned = cleaned.drop_duplicates(keep="first").copy()

    # Bước 2: điền trung vị cho từng cột số còn thiếu (không điền cột chữ, không xóa trùng lần 2)
    for col in cleaned.select_dtypes(include="number").columns:
        if cleaned[col].isna().any():
            valid = cleaned[col].dropna()
            if len(valid) > 0:
                median_val = float(np.median(valid.to_numpy(dtype=float)))
                cleaned[col] = cleaned[col].astype(float).fillna(median_val)

    return cleaned


def numeric_stats(df: pd.DataFrame, column: str) -> dict[str, int | float | None]:
    """Tính các chỉ số thống kê mô tả bằng NumPy với độ lệch chuẩn tổng thể (ddof=0)."""
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
        }

    return {
        "count": count,
        "min": float(np.min(values)),
        "max": float(np.max(values)),
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "std": float(np.std(values, ddof=0)),
    }


def mean_by_group(df: pd.DataFrame, group_column: str, value_column: str) -> pd.Series:
    """Tính giá trị trung bình của cột số theo từng nhóm bằng Pandas GroupBy."""
    if group_column not in df.columns:
        raise ValueError(f"Không tìm thấy cột nhóm '{group_column}'.")
    # Hỗ trợ cả dtype object, string (Pandas 3.x) và category
    text_cols = df.select_dtypes(include=["object", "string", "category"]).columns
    if group_column not in text_cols:
        raise ValueError(f"Cột '{group_column}' không phải cột nhóm dạng chữ hoặc phân loại.")

    _require_numeric_column(df, value_column)
    _check_no_infinity(df[[value_column]])

    return df.groupby(group_column, dropna=True, observed=True)[value_column].mean().astype(float)

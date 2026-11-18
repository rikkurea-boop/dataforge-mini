"""Module tạo các biểu đồ Matplotlib độc lập (trả về đối tượng Figure)."""

import numpy as np
import pandas as pd
from matplotlib.figure import Figure


def _prepare_numeric_frame(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Kiểm tra các cột mang kiểu số, chặn ±inf rồi giữ các dòng không bị thiếu."""
    numeric_cols = df.select_dtypes(include="number").columns
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Không tìm thấy cột '{col}'.")
        if col not in numeric_cols:
            raise ValueError(f"Cột '{col}' không phải cột dữ liệu số.")

    raw_values = df[columns].to_numpy(dtype=float, na_value=0.0)
    if np.isinf(raw_values).any():
        raise ValueError("Dữ liệu chứa giá trị vô cực (±inf), không thể vẽ biểu đồ.")

    return df[columns].dropna()


def histogram(df: pd.DataFrame, column: str) -> Figure:
    """Vẽ biểu đồ tần suất 5 khoảng (bins=5) cho một cột số sau khi bỏ ô trống."""
    valid = _prepare_numeric_frame(df, [column])
    if valid.empty:
        raise ValueError(f"Cột '{column}' không có giá trị số hợp lệ để vẽ histogram.")

    values = valid[column].to_numpy(dtype=float)
    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    ax.hist(values, bins=5, density=False, color="#4C78A8", edgecolor="black")
    ax.set_title(f"Phân phối tần suất của {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Số quan sát")
    fig.tight_layout()
    return fig


def group_bar(means: pd.Series) -> Figure:
    """Vẽ biểu đồ cột biểu diễn giá trị trung bình từng nhóm với trục Y bắt đầu từ 0."""
    if not isinstance(means, pd.Series):
        raise ValueError("Đầu vào của biểu đồ cột phải là pandas Series.")

    if np.isinf(means.to_numpy(dtype=float, na_value=0.0)).any():
        raise ValueError("Dữ liệu trung bình nhóm chứa giá trị vô cực (±inf).")

    valid = means.dropna().astype(float)
    if valid.empty:
        raise ValueError("Không có nhóm có dữ liệu số hợp lệ để vẽ biểu đồ cột.")

    labels = [str(label) for label in valid.index]
    heights = valid.to_numpy(dtype=float)

    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    ax.bar(labels, heights, color="#59A14F", edgecolor="black")
    ax.set_ylim(bottom=0)
    ax.set_title("Giá trị trung bình theo nhóm")
    ax.set_xlabel(str(means.index.name) if means.index.name else "Nhóm")
    ax.set_ylabel("Trung bình")
    fig.tight_layout()
    return fig


def scatter(df: pd.DataFrame, x_column: str, y_column: str) -> Figure:
    """Vẽ biểu đồ phân tán giữa hai cột số khác nhau, ghép cặp theo cùng hàng."""
    if x_column == y_column:
        raise ValueError("Hai cột X và Y của biểu đồ phân tán phải khác nhau.")

    paired = _prepare_numeric_frame(df, [x_column, y_column])
    if paired.empty:
        raise ValueError("Không có cặp giá trị (X, Y) hợp lệ cùng hàng để vẽ scatter.")

    x_vals = paired[x_column].to_numpy(dtype=float)
    y_vals = paired[y_column].to_numpy(dtype=float)

    title = f"Biểu đồ phân tán: {x_column} và {y_column}"
    if len(x_vals) >= 2 and np.std(x_vals) > 0 and np.std(y_vals) > 0:
        r_val = float(np.corrcoef(x_vals, y_vals)[0, 1])
        title = f"{title} (r = {r_val:.2f})"

    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    ax.scatter(x_vals, y_vals, color="#E15759", edgecolor="black", alpha=0.85)
    ax.set_title(title)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    fig.tight_layout()
    return fig


def boxplot(df: pd.DataFrame, column: str, group_column: str | None = None) -> Figure:
    """Vẽ biểu đồ hộp (Boxplot) để quan sát phân vị và phát hiện giá trị ngoại lai."""
    _prepare_numeric_frame(df, [column])

    groups_data: list[np.ndarray] = []
    labels: list[str] = []

    if group_column and group_column in df.columns:
        grouped = df[[group_column, column]].dropna()
        for name, sub in grouped.groupby(group_column, observed=True):
            vals = sub[column].to_numpy(dtype=float)
            if vals.size > 0:
                groups_data.append(vals)
                labels.append(str(name))
    else:
        vals = df[column].dropna().to_numpy(dtype=float)
        if vals.size > 0:
            groups_data = [vals]
            labels = [column]

    if not groups_data:
        raise ValueError(f"Không có đủ dữ liệu số hợp lệ ở '{column}' để vẽ boxplot.")

    fig = Figure(figsize=(6, 4))
    ax = fig.subplots()
    bp = ax.boxplot(groups_data, tick_labels=labels, patch_artist=True)
    for box in bp["boxes"]:
        box.set(facecolor="#9ECAE1", edgecolor="#1E3A5F", linewidth=1.2)
    for median in bp["medians"]:
        median.set(color="#D95F02", linewidth=1.8)

    ax.set_title(f"Phân phối & Ngoại lai (Boxplot): {column}")
    ax.set_xlabel(group_column if (group_column and group_column in df.columns) else "Cột số")
    ax.set_ylabel(column)
    fig.tight_layout()
    return fig

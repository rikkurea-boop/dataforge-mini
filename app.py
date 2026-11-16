"""Giao diện Streamlit một trang cho ứng dụng DataForge Mini."""

from pathlib import Path

import pandas as pd
import streamlit as st

from analysis import (
    MAX_CSV_BYTES,
    clean_data,
    inspect_data,
    load_csv,
    mean_by_group,
    numeric_stats,
)
from charts import group_bar, histogram, scatter

SAMPLE_CSV_PATH = Path(__file__).resolve().parent / "sample_data.csv"


def _default_index(options: list[str], preferred: str) -> int:
    """Chọn vị trí mặc định nếu tên cột ưu tiên có mặt trong danh sách."""
    return options.index(preferred) if preferred in options else 0


def _load_input_dataframe(uploaded_file) -> tuple[pd.DataFrame, str]:
    """Đọc dữ liệu từ file tải lên hoặc bộ dữ liệu mẫu cạnh app.py."""
    if uploaded_file is not None:
        if uploaded_file.size > MAX_CSV_BYTES:
            raise ValueError("File tải lên vượt quá giới hạn cho phép 2 MiB.")
        return load_csv(uploaded_file), f"File tải lên: `{uploaded_file.name}`"

    return load_csv(SAMPLE_CSV_PATH), "Bộ dữ liệu mẫu mặc định (`sample_data.csv` — dữ liệu giả lập)"


def main() -> None:
    """Điều phối luồng xử lý và hiển thị ứng dụng một trang."""
    st.set_page_config(page_title="DataForge Mini", layout="wide")
    st.title("DataForge Mini — Xử lý, Phân tích & Trực quan hóa Dữ liệu")
    st.caption(
        "Ứng dụng minh họa Chương 5.5 (Pandas, NumPy, Matplotlib). "
        "Chỉ hỗ trợ file CSV UTF-8 phân cách bằng dấu phẩy (≤ 2 MiB)."
    )

    uploaded = st.file_uploader(
        "Tải lên file CSV (hoặc để trống để dùng sample_data.csv)",
        type=["csv"],
    )

    try:
        raw_df, source_label = _load_input_dataframe(uploaded)
    except (ValueError, pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError, OSError) as exc:
        st.error(f"Không thể đọc dữ liệu CSV: {exc}")
        st.stop()

    st.info(f"Nguồn dữ liệu đang dùng: {source_label}")

    use_clean = st.checkbox(
        "Làm sạch dữ liệu (xóa dòng trùng toàn phần trước, sau đó điền trung vị cột số)"
    )

    try:
        active_df = clean_data(raw_df) if use_clean else raw_df
    except ValueError as exc:
        st.error(f"Không thể xử lý dữ liệu: {exc}")
        st.stop()

    raw_info = inspect_data(raw_df)
    active_info = inspect_data(active_df)

    st.subheader("1. Tổng quan & Bảng dữ liệu")
    summary_table = pd.DataFrame(
        [
            {"Trạng thái": "Dữ liệu gốc (Raw)", **raw_info},
            {"Trạng thái": "Dữ liệu đang xem (Active)", **active_info},
        ]
    )
    summary_table.columns = ["Trạng thái", "Số dòng", "Số cột", "Ô thiếu", "Dòng trùng"]
    st.dataframe(summary_table, hide_index=True)

    if use_clean and (active_info["missing_cells"] > 0 or active_info["duplicate_rows"] > 0):
        st.warning(
            f"Lưu ý sau làm sạch vẫn còn {active_info['missing_cells']} ô thiếu "
            f"(cột chữ hoặc cột số toàn trống không tự điền) và "
            f"{active_info['duplicate_rows']} dòng trùng phát sinh sau khi điền trung vị."
        )

    st.dataframe(active_df)
    csv_bytes = active_df.to_csv(index=False).encode("utf-8-sig")
    export_name = "dataforge_cleaned.csv" if use_clean else "dataforge_raw.csv"
    st.download_button(
        label="Tải xuống CSV đang xem",
        data=csv_bytes,
        file_name=export_name,
        mime="text/csv",
    )

    st.subheader("2. Chọn cột phân tích")
    num_cols = list(active_df.select_dtypes(include="number").columns)
    group_cols = list(active_df.select_dtypes(include=["object", "string", "category"]).columns)

    if not num_cols:
        st.warning(
            "Bảng dữ liệu hiện không có cột số hợp lệ (các cột chứa chữ như '8a' được giữ nguyên dạng chữ). "
            "Không thể tính thống kê và vẽ biểu đồ."
        )
        return

    col1, col2, col3 = st.columns(3)
    with col1:
        y_col = st.selectbox(
            "Cột số chính (Thống kê & trục Y)",
            options=num_cols,
            index=_default_index(num_cols, "diem"),
        )
    with col2:
        group_col: str | None = None
        if group_cols:
            group_col = st.selectbox(
                "Cột phân nhóm (Bar & GroupBy)",
                options=group_cols,
                index=_default_index(group_cols, "lop"),
            )
        else:
            st.info("Không có cột chữ/phân loại để phân nhóm.")
    with col3:
        x_options = [col for col in num_cols if col != y_col]
        x_col: str | None = None
        if x_options:
            x_col = st.selectbox(
                "Cột số trục X (Biểu đồ phân tán)",
                options=x_options,
                index=_default_index(x_options, "gio_hoc"),
            )
        else:
            st.info("Cần ít nhất 2 cột số khác nhau để vẽ biểu đồ phân tán.")

    st.subheader("3. Thống kê mô tả (NumPy) & Trung bình nhóm (Pandas)")
    stats = numeric_stats(active_df, y_col)
    if stats["count"] == 0:
        st.info(f"Cột '{y_col}' chưa có giá trị số hợp lệ (toàn ô trống).")
    else:
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        m1.metric("Số quan sát", stats["count"])
        m2.metric("Nhỏ nhất", f"{stats['min']:.2f}")
        m3.metric("Lớn nhất", f"{stats['max']:.2f}")
        m4.metric("Trung bình", f"{stats['mean']:.4f}")
        m5.metric("Trung vị", f"{stats['median']:.4f}")
        m6.metric("Độ lệch chuẩn (ddof=0)", f"{stats['std']:.4f}")

    group_means: pd.Series | None = None
    if group_col is not None:
        group_means = mean_by_group(active_df, group_col, y_col)
        valid_means = group_means.dropna()
        if valid_means.empty:
            st.info(f"Không có nhóm hợp lệ trong '{group_col}' có giá trị số ở '{y_col}'.")
        else:
            st.write(f"Trung bình `{y_col}` theo `{group_col}`:")
            st.dataframe(valid_means.rename("Trung bình").reset_index(), hide_index=True)

    st.subheader("4. Trực quan hóa dữ liệu (Matplotlib)")
    c1, c2, c3 = st.columns(3)

    with c1:
        try:
            st.pyplot(histogram(active_df, y_col))
        except ValueError as exc:
            st.info(str(exc))

    with c2:
        if group_means is None:
            st.info("Ẩn biểu đồ cột vì chưa có cột phân nhóm.")
        else:
            try:
                st.pyplot(group_bar(group_means))
            except ValueError as exc:
                st.info(str(exc))

    with c3:
        if x_col is None:
            st.info("Ẩn biểu đồ phân tán vì cần tối thiểu 2 cột số.")
        else:
            try:
                st.pyplot(scatter(active_df, x_col, y_col))
                st.caption("Lưu ý: biểu đồ phân tán thể hiện mối liên hệ giữa hai biến, không kết luận quan hệ nhân quả.")
            except ValueError as exc:
                st.info(str(exc))


if __name__ == "__main__":
    main()

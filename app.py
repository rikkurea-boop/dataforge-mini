"""Giao diện Streamlit một trang cho ứng dụng DataForge Mini."""

import importlib
import io
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd
import streamlit as st

from analysis import (
    MAX_CSV_BYTES,
    clean_data,
    column_profile,
    filter_data,
    inspect_data,
    load_csv,
    mean_by_group,
    numeric_stats,
)
from charts import boxplot, group_bar, histogram, scatter

GITHUB_REPO = "rikkurea-boop/dataforge-mini"
GITHUB_BRANCH = "main"

MISSING_OPTIONS = {
    "Giữ nguyên ô thiếu (Raw)": "keep",
    "Điền trung vị (Median)": "median",
    "Điền trung bình (Mean)": "mean",
    "Xóa dòng có ô thiếu (dropna)": "drop",
}


def _default_index(options: list[str], preferred: str) -> int:
    """Chọn vị trí mặc định nếu tên cột ưu tiên có mặt trong danh sách."""
    return options.index(preferred) if preferred in options else 0


def _with_one_based_index(
    df: pd.DataFrame,
    y_col: str | None = None,
    x_col: str | None = None,
    group_col: str | None = None,
) -> pd.DataFrame:
    """Tạo bản hiển thị đánh số từ 1, kèm cột ghi chú dữ liệu đưa vào biểu đồ."""
    view = df.copy()
    if y_col is not None:
        notes: list[str] = []
        for _, row in view.iterrows():
            if pd.isna(row[y_col]):
                notes.append(f"− Bỏ biểu đồ (thiếu {y_col})")
            else:
                skipped = []
                if x_col is not None and pd.isna(row[x_col]):
                    skipped.append(f"Scatter: thiếu {x_col}")
                if group_col is not None and pd.isna(row[group_col]):
                    skipped.append(f"Nhóm: thiếu {group_col}")
                notes.append(f"− Bỏ ở {'; '.join(skipped)}" if skipped else "✓ Hợp lệ")
        view["Ghi chú biểu đồ"] = notes
    view.index = range(1, len(view) + 1)
    return view


def _load_input_dataframe(uploaded_file) -> tuple[pd.DataFrame, str]:
    """Đọc dữ liệu từ file CSV người dùng đã tải lên."""
    if uploaded_file is None:
        raise ValueError("Chưa có file CSV nào được tải lên.")
    if uploaded_file.size > MAX_CSV_BYTES:
        raise ValueError("File tải lên vượt quá giới hạn cho phép 2 MiB.")
    return load_csv(uploaded_file), f"File tải lên: `{uploaded_file.name}`"


def _format_num(value: int | float | None) -> str:
    """Làm tròn số tối đa 2 chữ số thập phân và bỏ đuôi .0/.00 nếu là số tròn."""
    if value is None:
        return "-"
    rounded = round(float(value), 2)
    if rounded == 0:
        rounded = 0.0
    return f"{rounded:.2f}".rstrip("0").rstrip(".")


def _build_summary_text(
    source_label: str,
    raw_info: dict[str, int],
    filtered_info: dict[str, int],
    y_col: str | None,
    stats: dict[str, int | float | None] | None,
    group_col: str | None,
    group_means: pd.Series | None,
) -> bytes:
    """Tạo nội dung báo cáo tóm tắt dạng văn bản thuần (UTF-8) để tải nhanh từ ứng dụng."""
    lines = [
        "=== BÁO CÁO TÓM TẮT DATAFORGE MINI ===",
        f"Nguồn dữ liệu: {source_label}",
        f"Dữ liệu gốc: {raw_info['rows']} dòng × {raw_info['columns']} cột "
        f"(thiếu {raw_info['missing_cells']} ô, trùng {raw_info['duplicate_rows']} dòng)",
        f"Dữ liệu đang xem (sau xử lý & lọc): {filtered_info['rows']} dòng × {filtered_info['columns']} cột",
        "",
    ]
    if y_col and stats and stats["count"]:
        lines.extend(
            [
                f"--- Thống kê cột số: {y_col} ---",
                f"Số quan sát: {stats['count']}",
                f"Nhỏ nhất / Lớn nhất: {_format_num(stats['min'])} / {_format_num(stats['max'])}",
                f"Trung bình / Trung vị: {_format_num(stats['mean'])} / {_format_num(stats['median'])}",
                f"Độ lệch chuẩn (ddof=0): {_format_num(stats['std'])}",
                f"Q1 / Q3 / IQR: {_format_num(stats['q1'])} / {_format_num(stats['q3'])} / {_format_num(stats['iqr'])}",
                f"Số giá trị ngoại lai (1.5*IQR): {stats['outliers']}",
                "",
            ]
        )
    if group_col and group_means is not None and not group_means.dropna().empty:
        lines.append(f"--- Trung bình {y_col} theo {group_col} ---")
        for name, val in group_means.dropna().items():
            lines.append(f"  - {name}: {_format_num(val)}")
    return "\n".join(lines).encode("utf-8-sig")


def _check_and_update(app_dir: Path | None = None) -> tuple[bool, str]:
    """Kiểm tra bản mới trên GitHub và tự động cập nhật (hỗ trợ cả Git lẫn bản tải ZIP)."""
    root = (Path(app_dir) if app_dir is not None else Path(__file__).resolve().parent).resolve()

    try:
        if (root / ".git").exists() and shutil.which("git"):
            def _git(*args: str, timeout: int = 15) -> str:
                res = subprocess.run(
                    ["git", "-C", str(root), *args],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    check=True,
                )
                return res.stdout.strip()

            _git("fetch", "--quiet", "origin", GITHUB_BRANCH)
            local_sha = _git("rev-parse", "HEAD")
            remote_sha = _git("rev-parse", f"origin/{GITHUB_BRANCH}")
            if local_sha == remote_sha:
                return False, f"Đang ở bản mới nhất ({local_sha[:7]})."
            _git("pull", "--ff-only", "origin", GITHUB_BRANCH, timeout=30)
            return True, f"Đã cập nhật từ `{local_sha[:7]}` lên `{remote_sha[:7]}`."

        req = urllib.request.Request(
            f"https://api.github.com/repos/{GITHUB_REPO}/commits/{GITHUB_BRANCH}",
            headers={"User-Agent": "DataForge-Mini"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            remote_sha = json.loads(resp.read().decode("utf-8"))["sha"]

        marker = root / ".update_sha"
        local_sha = marker.read_text(encoding="utf-8").strip() if marker.exists() else ""
        if local_sha == remote_sha:
            return False, f"Đang ở bản mới nhất ({remote_sha[:7]})."

        zip_req = urllib.request.Request(
            f"https://github.com/{GITHUB_REPO}/archive/refs/heads/{GITHUB_BRANCH}.zip",
            headers={"User-Agent": "DataForge-Mini"},
        )
        with urllib.request.urlopen(zip_req, timeout=30) as resp:
            zip_bytes = resp.read()

        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                parts = Path(info.filename).parts
                if len(parts) < 2:
                    continue
                rel = Path(*parts[1:])
                if any(part in {".git", ".venv", "__pycache__"} for part in rel.parts):
                    continue
                dest = (root / rel).resolve()
                if not dest.is_relative_to(root):
                    continue
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(zf.read(info.filename))
                if dest.suffix == ".command":
                    dest.chmod(0o755)

        marker.write_text(remote_sha, encoding="utf-8")
        return True, f"Đã tải và cập nhật bản mới nhất (`{remote_sha[:7]}`)."
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise RuntimeError(
                "Không tìm thấy dữ liệu cập nhật trên GitHub (lỗi 404). "
                "Repository hiện có thể đang để Private — hãy chuyển repo sang Public hoặc dùng bản git clone."
            ) from exc
        raise RuntimeError(f"Không thể cập nhật tự động (HTTP {exc.code}): {exc.reason}") from exc
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        urllib.error.URLError,
        zipfile.BadZipFile,
        OSError,
        KeyError,
        json.JSONDecodeError,
    ) as exc:
        detail = getattr(exc, "stderr", None) or str(exc)
        raise RuntimeError(f"Không thể cập nhật tự động: {detail.strip()}") from exc


def main() -> None:
    """Điều phối luồng xử lý và hiển thị ứng dụng một trang."""
    st.set_page_config(page_title="DataForge Mini", layout="wide")
    st.markdown(
        """
        <style>
        .st-key-btn_update {
            position: fixed;
            top: 0;
            right: 6.75rem;
            height: 3.75rem;
            display: flex;
            align-items: center;
            width: auto !important;
            z-index: 999995;
        }
        .st-key-btn_update button {
            min-height: unset;
            height: 2rem;
            padding: 0 0.6rem;
            display: inline-flex;
            align-items: center;
        }
        .st-key-btn_update button p {
            margin: 0;
            font-size: 0.875rem;
            line-height: 1.2;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    update_clicked = st.button(
        "↻ Cập nhật",
        key="btn_update",
        type="tertiary",
        help="Kiểm tra và tự động cập nhật bản mới từ GitHub",
    )
    st.title("DataForge Mini — Xử lý, Phân tích & Trực quan hóa Dữ liệu")

    if notice := st.session_state.pop("update_notice", None):
        st.success(notice)

    if update_clicked:
        with st.spinner("Đang kiểm tra cập nhật trên GitHub..."):
            try:
                updated, msg = _check_and_update()
            except RuntimeError as exc:
                st.error(str(exc))
            else:
                if updated:
                    for mod_name in ("analysis", "charts"):
                        if mod_name in sys.modules:
                            importlib.reload(sys.modules[mod_name])
                    st.session_state["update_notice"] = msg
                    st.rerun()
                st.info(msg)

    st.caption(
        "Ứng dụng minh họa Chương 5.5 (Pandas, NumPy, Matplotlib) — "
        "Chỉ hỗ trợ file CSV UTF-8 dấu phẩy (≤ 2 MiB)."
    )

    uploaded = st.file_uploader(
        "Tải lên file CSV để bắt đầu phân tích",
        type=["csv"],
    )

    if uploaded is not None:
        st.session_state.pop("use_sample", None)
    elif not st.session_state.get("use_sample"):
        st.session_state.pop("confirmed_key", None)
        if st.button("Dùng thử nhanh với dữ liệu mẫu (sample_data.csv)", type="primary"):
            st.session_state["use_sample"] = True
            st.session_state["confirmed_key"] = ("sample_data.csv", False, "keep")
            st.rerun()
        st.info(
            "Vui lòng tải lên một file CSV hoặc bấm nút dùng thử mẫu ở trên để mở 3 tab "
            "Làm sạch, Thống kê và Biểu đồ."
        )
        return

    if uploaded is None:
        s_col1, s_col2 = st.columns([4, 1.3], vertical_alignment="center")
        with s_col1:
            st.info("Đang dùng thử bộ dữ liệu mẫu có sẵn: `sample_data.csv` (12 dòng × 4 cột).")
        with s_col2:
            if st.button("Đóng dữ liệu mẫu", width="stretch"):
                st.session_state.pop("use_sample", None)
                st.session_state.pop("confirmed_key", None)
                st.rerun()

    with st.container(border=True):
        c_clean1, c_clean2 = st.columns(2)
        with c_clean1:
            remove_dups = st.checkbox("Xóa dòng trùng lặp toàn phần (keep first)", value=False)
        with c_clean2:
            missing_label = st.selectbox(
                "Chiến lược xử lý ô số bị thiếu",
                options=list(MISSING_OPTIONS.keys()),
                index=0,
            )
        missing_strategy = MISSING_OPTIONS[missing_label]

        file_token = (
            getattr(uploaded, "file_id", f"{uploaded.name}:{uploaded.size}")
            if uploaded is not None
            else "sample_data.csv"
        )
        current_key = (file_token, remove_dups, missing_strategy)

        if st.button("Xác nhận xử lý dữ liệu", type="primary"):
            st.session_state["confirmed_key"] = current_key

    if st.session_state.get("confirmed_key") != current_key:
        st.info("Nhấn nút **Xác nhận xử lý dữ liệu** để bắt đầu đọc file, tính thống kê và vẽ biểu đồ.")
        return

    try:
        if uploaded is not None:
            raw_df, source_label = _load_input_dataframe(uploaded)
        else:
            sample_path = Path(__file__).resolve().parent / "sample_data.csv"
            raw_df = load_csv(sample_path)
            source_label = "Dữ liệu mẫu có sẵn: `sample_data.csv`"
        active_df = clean_data(
            raw_df,
            remove_duplicates=remove_dups,
            missing_strategy=missing_strategy,
        )
    except (ValueError, pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError, OSError) as exc:
        st.error(f"Không thể xử lý dữ liệu CSV: {exc}")
        st.stop()

    raw_info = inspect_data(raw_df)
    active_info = inspect_data(active_df)
    is_cleaning_active = remove_dups or missing_strategy != "keep"

    st.success(f"Đã xử lý xong — {source_label} ({active_info['rows']} dòng × {active_info['columns']} cột)")

    num_cols = list(active_df.select_dtypes(include="number").columns)
    group_cols = list(active_df.select_dtypes(include=["object", "string", "category"]).columns)

    if not num_cols:
        st.dataframe(_with_one_based_index(active_df))
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
                "Cột phân nhóm (Bar, Boxplot & GroupBy)",
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

    # Gom bộ lọc nâng cao & sắp xếp vào mục gấp gọn để tránh rối mắt khi mới mở app
    selected_groups_filter: list[str] | None = None
    val_range_filter: tuple[float, float] | None = None
    with st.expander("Tùy chọn lọc dữ liệu & sắp xếp (áp dụng cho cả 3 tab)", expanded=False):
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            if group_col is not None:
                all_groups = sorted(active_df[group_col].dropna().astype(str).unique().tolist())
                chosen_groups = st.multiselect(
                    f"Lọc theo {group_col}",
                    options=all_groups,
                    default=all_groups,
                )
                if len(chosen_groups) < len(all_groups):
                    selected_groups_filter = chosen_groups

        with f_col2:
            valid_y = active_df[y_col].dropna()
            if not valid_y.empty:
                min_v, max_v = float(valid_y.min()), float(valid_y.max())
                if min_v < max_v:
                    chosen_range = st.slider(
                        f"Lọc khoảng giá trị {y_col}",
                        min_value=min_v,
                        max_value=max_v,
                        value=(min_v, max_v),
                    )
                    if chosen_range != (min_v, max_v):
                        val_range_filter = chosen_range

        with f_col3:
            sort_mode = st.selectbox(
                f"Sắp xếp theo {y_col}",
                options=["Thứ tự gốc", "Giảm dần", "Tăng dần"],
                index=0,
            )

    filtered_df = filter_data(
        active_df,
        group_column=group_col,
        selected_groups=selected_groups_filter,
        numeric_column=y_col,
        value_range=val_range_filter,
    )
    if sort_mode == "Giảm dần":
        filtered_df = filtered_df.sort_values(by=y_col, ascending=False, na_position="last")
    elif sort_mode == "Tăng dần":
        filtered_df = filtered_df.sort_values(by=y_col, ascending=True, na_position="last")

    if filtered_df.empty:
        st.warning("Không có dòng dữ liệu nào khớp bộ lọc hiện tại. Hãy nới rộng điều kiện lọc.")
        return

    stats = numeric_stats(filtered_df, y_col)
    group_means = mean_by_group(filtered_df, group_col, y_col) if group_col is not None else None

    tab_data, tab_stats, tab_charts = st.tabs(
        ["1. Dữ liệu & Làm sạch", "2. Thống kê mô tả", "3. Biểu đồ trực quan"]
    )

    with tab_data:
        summary_table = pd.DataFrame(
            [
                {"Trạng thái": "Dữ liệu gốc (Raw)", **raw_info},
                {"Trạng thái": "Sau xử lý (Active)", **active_info},
            ]
        )
        summary_table.columns = ["Trạng thái", "Số dòng", "Số cột", "Ô thiếu", "Dòng trùng"]
        st.dataframe(summary_table, hide_index=True)

        if is_cleaning_active and (active_info["missing_cells"] > 0 or active_info["duplicate_rows"] > 0):
            st.warning(
                f"Lưu ý sau xử lý vẫn còn {active_info['missing_cells']} ô thiếu "
                f"(cột chữ hoặc cột số toàn trống) và {active_info['duplicate_rows']} dòng trùng."
            )

        n_y_valid = int(filtered_df[y_col].notna().sum())
        scatter_note = (
            f" · Đủ vẽ Scatter: **{int(filtered_df[[x_col, y_col]].dropna().shape[0])}** cặp"
            if x_col is not None
            else ""
        )
        st.caption(
            f"Bảng dữ liệu đang xem: **{len(filtered_df)} / {len(active_df)}** dòng "
            f"· Đủ dữ liệu chính: **{n_y_valid}** dòng{scatter_note}."
        )
        st.dataframe(
            _with_one_based_index(filtered_df, y_col=y_col, x_col=x_col, group_col=group_col)
        )

        with st.expander("Kiểm tra chi tiết từng cột (Kiểu dữ liệu, tỷ lệ thiếu, giá trị duy nhất)"):
            st.dataframe(column_profile(active_df), hide_index=True)

        valid_for_top = filtered_df.dropna(subset=[y_col])
        if not valid_for_top.empty:
            with st.expander(f"Xem Top 5 giá trị cao nhất & thấp nhất theo {y_col}"):
                top_c1, top_c2 = st.columns(2)
                with top_c1:
                    st.write("Top 5 cao nhất:")
                    st.dataframe(valid_for_top.nlargest(5, y_col), hide_index=True)
                with top_c2:
                    st.write("Top 5 thấp nhất:")
                    st.dataframe(valid_for_top.nsmallest(5, y_col), hide_index=True)

        csv_bytes = filtered_df.to_csv(index=False).encode("utf-8-sig")
        export_name = "dataforge_cleaned.csv" if is_cleaning_active else "dataforge_raw.csv"
        st.download_button(
            label="Tải xuống CSV đang xem",
            data=csv_bytes,
            file_name=export_name,
            mime="text/csv",
        )

    with tab_stats:
        if stats["count"] == 0:
            st.info(f"Cột '{y_col}' chưa có giá trị số hợp lệ (toàn ô trống).")
        else:
            r1 = st.columns(4)
            r1[0].metric("Số quan sát", stats["count"], border=True)
            r1[1].metric("Nhỏ nhất", _format_num(stats["min"]), border=True)
            r1[2].metric("Trung bình", _format_num(stats["mean"]), border=True)
            r1[3].metric("Trung vị", _format_num(stats["median"]), border=True)

            r2 = st.columns(4)
            r2[0].metric("Lớn nhất", _format_num(stats["max"]), border=True)
            r2[1].metric("Độ lệch chuẩn (ddof=0)", _format_num(stats["std"]), border=True)
            r2[2].metric("Q1 (25%)", _format_num(stats["q1"]), border=True)
            r2[3].metric("Q3 (75%)", _format_num(stats["q3"]), border=True)

            r3 = st.columns(4)
            r3[0].metric("Khoảng tứ phân vị (IQR)", _format_num(stats["iqr"]), border=True)
            r3[1].metric("Số ngoại lai (Outliers)", stats["outliers"], border=True)

        if group_col is not None and group_means is not None:
            valid_means = group_means.dropna()
            if valid_means.empty:
                st.info(f"Không có nhóm hợp lệ trong '{group_col}' có giá trị số ở '{y_col}'.")
            else:
                st.write(f"Trung bình `{y_col}` theo `{group_col}`:")
                st.dataframe(
                    valid_means.map(_format_num).rename("Trung bình").reset_index(),
                    hide_index=True,
                )

        summary_bytes = _build_summary_text(
            source_label,
            raw_info,
            inspect_data(filtered_df),
            y_col,
            stats,
            group_col,
            group_means,
        )
        st.download_button(
            label="Tải báo cáo tóm tắt (.txt)",
            data=summary_bytes,
            file_name="dataforge_summary.txt",
            mime="text/plain",
        )

    with tab_charts:
        c1, c2 = st.columns(2)

        with c1:
            try:
                st.pyplot(histogram(filtered_df, y_col))
                st.caption(
                    f"**Phân phối tần suất (Histogram):** Chia `{y_col}` thành 5 khoảng; "
                    "cột càng cao nghĩa là có càng nhiều dữ liệu rơi vào khoảng đó."
                )
            except ValueError as exc:
                st.info(str(exc))

        with c2:
            if group_means is None:
                st.info("Ẩn biểu đồ cột vì chưa có cột phân nhóm.")
            else:
                try:
                    st.pyplot(group_bar(group_means))
                    st.caption(
                        f"**So sánh nhóm (Biểu đồ cột):** Hiển thị trung bình `{y_col}` theo từng nhóm `{group_col}`; "
                        "trục dọc bắt đầu từ 0 để so sánh chính xác."
                    )
                except ValueError as exc:
                    st.info(str(exc))

        c3, c4 = st.columns(2)
        with c3:
            if x_col is None:
                st.info("Ẩn biểu đồ phân tán vì cần tối thiểu 2 cột số.")
            else:
                try:
                    st.pyplot(scatter(filtered_df, x_col, y_col))
                    valid_pairs = filtered_df[[x_col, y_col]].dropna()
                    n_pairs = len(valid_pairs)
                    n_overlap = n_pairs - len(valid_pairs.drop_duplicates())
                    overlap_note = (
                        f" (có {n_overlap} cặp trùng tọa độ chồng khít lên nhau)"
                        if n_overlap > 0
                        else ""
                    )
                    st.caption(
                        f"**Cách đọc Scatter (`{x_col}` → `{y_col}`):** Đang vẽ **{n_pairs} cặp**{overlap_note}. "
                        "Đường nét đứt hướng lên nghĩa là khi X tăng thì Y thường tăng (chỉ mô tả xu hướng, không kết luận nhân quả)."
                    )
                except ValueError as exc:
                    st.info(str(exc))

        with c4:
            try:
                st.pyplot(boxplot(filtered_df, y_col, group_col))
                if stats["count"]:
                    st.caption(
                        f"**Cách đọc đơn giản (`{y_col}`):** Phần lớn dữ liệu tập trung trong hộp xanh "
                        f"(từ **{_format_num(stats['q1'])}** đến **{_format_num(stats['q3'])}**), "
                        f"vạch cam là trung vị (**{_format_num(stats['median'])}**), hộp càng gọn dữ liệu càng đều; "
                        f"hiện có **{stats['outliers']}** điểm bất thường (nếu có sẽ hiện chấm đỏ ngoài hai đầu râu)."
                    )
            except ValueError as exc:
                st.info(str(exc))


if __name__ == "__main__":
    main()

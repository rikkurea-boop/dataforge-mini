"""DataForge Mini — Xử lý, phân tích và trực quan hóa dữ liệu CSV (1 file tối giản)."""

import csv, io
from pathlib import Path
import numpy as np, pandas as pd, streamlit as st
from matplotlib.figure import Figure

BASE_DIR = Path(__file__).parent
MAX_BYTES = 2 * 1024 * 1024

fmt = lambda v: "-" if v is None else f"{(0.0 if round(float(v), 2) == 0 else round(float(v), 2)):.2f}".rstrip("0").rstrip(".")

# --- 1. ĐỌC & KIỂM LỖI CSV ---
def load_csv(source) -> pd.DataFrame:
    raw = Path(source).read_bytes() if isinstance(source, (str, Path)) else (source.seek(0), source.read(MAX_BYTES + 1))[1]
    if len(raw) > MAX_BYTES: raise ValueError("File CSV vượt quá 2 MiB.")
    try: text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e: raise ValueError("File không đúng UTF-8.") from e
    rows = [r for r in csv.reader(io.StringIO(text)) if r]
    if not rows: raise ValueError("File CSV rỗng.")
    header = [c.strip() for c in rows[0]]
    if len(header) == 1 and ";" in header[0]: raise ValueError("Chỉ hỗ trợ CSV phân cách dấu phẩy (,).")
    if any(c == "" for c in header) or len(set(header)) != len(header): raise ValueError("Header trống hoặc trùng tên cột.")
    for i, r in enumerate(rows[1:], start=2):
        if len(r) > len(header): raise ValueError(f"Dòng {i} thừa cột so với tiêu đề.")
    df = pd.read_csv(io.StringIO(text), sep=",", index_col=False)
    if df.empty: raise ValueError("CSV không có dòng dữ liệu.")
    num_df = df.select_dtypes(include="number")
    if not num_df.empty and np.isinf(num_df.to_numpy(dtype=float, na_value=0.0)).any():
        raise ValueError("Dữ liệu chứa giá trị vô cực (±inf).")
    return df

# --- 2. KIỂM TRA, LÀM SẠCH & THỐNG KÊ ---
def inspect_data(df: pd.DataFrame) -> dict[str, int]:
    return {"rows": int(df.shape[0]), "cols": int(df.shape[1]),
            "missing": int(df.isna().sum().sum()), "dups": int(df.duplicated(keep="first").sum())}

def clean_data(df: pd.DataFrame, drop_dup: bool = True, missing: str = "median") -> pd.DataFrame:
    out = df.drop_duplicates(keep="first").copy() if drop_dup else df.copy()
    if missing == "drop": return out.dropna().copy()
    if missing in ("median", "mean"):
        fn = np.median if missing == "median" else np.mean
        for col in out.select_dtypes(include="number").columns:
            valid = out[col].dropna()
            if out[col].isna().any() and len(valid) > 0:
                out[col] = out[col].astype(float).fillna(float(fn(valid.to_numpy(dtype=float))))
    return out

def numeric_stats(df: pd.DataFrame, col: str) -> dict[str, int | float | None]:
    vals = df[col].dropna().to_numpy(dtype=float)
    if vals.size == 0:
        return dict.fromkeys(["min", "max", "mean", "median", "std", "q1", "q3", "iqr"], None) | {"count": 0, "outliers": 0}
    q1, q3 = (float(v) for v in np.percentile(vals, [25, 75]))
    iqr = q3 - q1
    return {"count": int(vals.size), "min": float(np.min(vals)), "max": float(np.max(vals)),
            "mean": float(np.mean(vals)), "median": float(np.median(vals)), "std": float(np.std(vals, ddof=0)),
            "q1": q1, "q3": q3, "iqr": iqr, "outliers": int(np.sum((vals < q1 - 1.5 * iqr) | (vals > q3 + 1.5 * iqr)))}

def mean_by_group(df: pd.DataFrame, group_col: str, val_col: str) -> pd.Series:
    return df.groupby(group_col, dropna=True, observed=True)[val_col].mean().dropna().astype(float)

# --- 3. BIỂU ĐỒ MATPLOTLIB ĐỘC LẬP ---
def _make_fig(title: str, xlabel: str, ylabel: str, grid_axis: str = "y") -> tuple[Figure, object]:
    fig = Figure(figsize=(5.5, 3.6)); ax = fig.subplots()
    ax.set_axisbelow(True); ax.grid(axis=grid_axis, linestyle="--", alpha=0.4)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    return fig, ax

def chart_hist(df: pd.DataFrame, col: str) -> Figure:
    vals = df[col].dropna().to_numpy(dtype=float)
    fig, ax = _make_fig(f"Phân phối tần suất: {col}", col, "Số quan sát")
    counts, edges, patches = ax.hist(vals, bins=5, color="#4C78A8", edgecolor="#1E293B")
    ax.set_xticks(edges); ax.set_xticklabels([fmt(e) for e in edges])
    ax.bar_label(patches, labels=[str(int(round(c))) for c in counts], padding=3)
    ax.set_ylim(0, max(float(np.max(counts)), 1.0) * 1.18)
    fig.tight_layout(); return fig

def chart_bar(means: pd.Series, group_col: str, val_col: str) -> Figure:
    fig, ax = _make_fig(f"Trung bình {val_col} theo {group_col}", group_col, f"Trung bình {val_col}")
    heights = means.to_numpy(dtype=float)
    bars = ax.bar([str(k) for k in means.index], heights, color="#6B9AC4", edgecolor="#1E293B")
    ax.bar_label(bars, labels=[fmt(h) for h in heights], padding=3)
    ax.set_ylim(0, max(float(np.max(heights)), 1.0) * 1.18)
    fig.tight_layout(); return fig

def chart_scatter(df: pd.DataFrame, x_col: str, y_col: str) -> Figure:
    paired = df[[x_col, y_col]].dropna()
    x_v, y_v = paired[x_col].to_numpy(dtype=float), paired[y_col].to_numpy(dtype=float)
    fig, ax = _make_fig(f"Tương quan: {x_col} và {y_col}", x_col, y_col, grid_axis="both")
    ax.scatter(x_v, y_v, color="#E15759", edgecolor="#7F1D1D", alpha=0.85)
    if len(x_v) >= 2 and np.std(x_v) > 0:
        slope, intercept = np.polyfit(x_v, y_v, 1)
        x_line = np.array([float(np.min(x_v)), float(np.max(x_v))])
        ax.plot(x_line, slope * x_line + intercept, linestyle="--", color="#1E3A5F")
        if np.std(y_v) > 0: ax.set_title(f"{x_col} vs {y_col} (r = {np.corrcoef(x_v, y_v)[0, 1]:.2f})")
    fig.tight_layout(); return fig

def chart_box(df: pd.DataFrame, col: str, group_col: str | None = None) -> Figure:
    if group_col and group_col in df.columns:
        groups = [(str(k), g[col].to_numpy(dtype=float)) for k, g in df[[group_col, col]].dropna().groupby(group_col, observed=True)]
        groups = [(k, v) for k, v in groups if v.size > 0]
    else:
        vals = df[col].dropna().to_numpy(dtype=float)
        groups = [(col, vals)] if vals.size > 0 else []
    fig, ax = _make_fig(f"Boxplot: {col}", group_col or "Cột số", col)
    bp = ax.boxplot([v for _, v in groups], tick_labels=[k for k, _ in groups], patch_artist=True)
    for box in bp["boxes"]: box.set(facecolor="#9ECAE1", edgecolor="#1E3A5F")
    for med in bp["medians"]: med.set(color="#D95F02", linewidth=2)
    fig.tight_layout(); return fig

# --- 4. GIAO DIỆN STREAMLIT TỐI GIẢN ---
def main() -> None:
    st.set_page_config(page_title="DataForge Mini", layout="wide")
    st.title("DataForge Mini")
    st.caption("Xử lý, phân tích và trực quan hóa dữ liệu CSV (NumPy · Pandas · Matplotlib)")

    with st.sidebar:
        st.header("1. Nguồn dữ liệu")
        sample_files = sorted(p.name for p in (BASE_DIR / "samples").glob("*.csv")) if (BASE_DIR / "samples").exists() else []
        mode = st.radio("Chọn nguồn", ["Dữ liệu mẫu (sample_data.csv)", "Bộ test (samples/)", "Tải file CSV"])
        source = BASE_DIR / "sample_data.csv"
        if mode == "Bộ test (samples/)" and sample_files:
            source = BASE_DIR / "samples" / st.selectbox("Chọn file test", sample_files)
        elif mode == "Tải file CSV":
            source = st.file_uploader("Chọn file CSV (UTF-8, dấu phẩy)", type=["csv"])
        st.header("2. Làm sạch")
        drop_dup = st.checkbox("Xóa dòng trùng lặp", value=True)
        missing = st.selectbox("Ô số thiếu", ["median", "mean", "drop", "keep"], format_func={
            "median": "Điền trung vị (Median)", "mean": "Điền trung bình (Mean)",
            "drop": "Xóa dòng thiếu", "keep": "Giữ nguyên dữ liệu gốc"}.get)

    if source is None:
        st.info("Vui lòng chọn hoặc tải lên một file CSV ở thanh bên trái."); return
    try: raw_df = load_csv(source)
    except ValueError as err:
        st.error(f"Lỗi đọc dữ liệu: {err}"); return

    cleaned_df = clean_data(raw_df, drop_dup=drop_dup, missing=missing)
    num_cols = list(cleaned_df.select_dtypes(include="number").columns)
    cat_cols = list(cleaned_df.select_dtypes(exclude="number").columns)

    with st.sidebar:
        st.header("3. Cột & Lọc")
        y_col = st.selectbox("Cột số chính", num_cols, index=num_cols.index("diem") if "diem" in num_cols else 0) if num_cols else None
        group_col = st.selectbox("Cột phân nhóm", ["(Không)"] + cat_cols, index=cat_cols.index("lop") + 1 if "lop" in cat_cols else 0)
        group_col = None if group_col == "(Không)" else group_col
        x_choices = [c for c in num_cols if c != y_col]
        x_col = st.selectbox("Cột số trục X (Scatter)", x_choices, index=x_choices.index("gio_hoc") if "gio_hoc" in x_choices else 0) if x_choices else None
        view_df = cleaned_df.copy()
        if group_col:
            uniq = sorted(view_df[group_col].dropna().astype(str).unique().tolist())
            picked = st.multiselect(f"Lọc {group_col}", uniq, default=uniq)
            view_df = view_df[view_df[group_col].astype(str).isin(picked)]

    raw_info, cur_info = inspect_data(raw_df), inspect_data(view_df)
    st.subheader("1. Dữ liệu & Kiểm tra")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Số dòng", cur_info["rows"], delta=cur_info["rows"] - raw_info["rows"])
    c2.metric("Số cột", cur_info["cols"])
    c3.metric("Ô thiếu", cur_info["missing"], delta=cur_info["missing"] - raw_info["missing"], delta_color="inverse")
    c4.metric("Dòng trùng", cur_info["dups"], delta=cur_info["dups"] - raw_info["dups"], delta_color="inverse")
    st.dataframe(view_df, width="stretch")
    st.download_button("Tải CSV đã xử lý", view_df.to_csv(index=False).encode("utf-8-sig"), "dataforge_cleaned.csv", "text/csv")

    if not y_col:
        st.warning("Bảng dữ liệu không có cột số để thống kê và vẽ biểu đồ."); return
    stats = numeric_stats(view_df, y_col)
    st.subheader(f"2. Thống kê mô tả: {y_col}")
    if stats["count"] == 0:
        st.info(f"Cột '{y_col}' không có giá trị số hợp lệ."); return
    r1 = st.columns(4)
    r1[0].metric("Số quan sát", stats["count"]); r1[1].metric("Min / Max", f"{fmt(stats['min'])} / {fmt(stats['max'])}")
    r1[2].metric("Trung bình", fmt(stats["mean"])); r1[3].metric("Trung vị", fmt(stats["median"]))
    r2 = st.columns(4)
    r2[0].metric("Độ lệch chuẩn (ddof=0)", fmt(stats["std"])); r2[1].metric("Q1 / Q3", f"{fmt(stats['q1'])} / {fmt(stats['q3'])}")
    r2[2].metric("IQR", fmt(stats["iqr"])); r2[3].metric("Ngoại lai (1.5×IQR)", stats["outliers"])

    means = mean_by_group(view_df, group_col, y_col) if group_col else pd.Series(dtype=float)
    if group_col and not means.empty:
        st.dataframe(means.rename("Trung bình").map(fmt), width="stretch")

    st.subheader("3. Biểu đồ trực quan")
    g1, g2 = st.columns(2)
    g1.pyplot(chart_hist(view_df, y_col), width="stretch")
    if group_col and not means.empty:
        g2.pyplot(chart_bar(means, group_col, y_col), width="stretch")
    else:
        g2.info("Chọn cột phân nhóm để vẽ biểu đồ cột.")
    g3, g4 = st.columns(2)
    if x_col and not view_df[[x_col, y_col]].dropna().empty:
        g3.pyplot(chart_scatter(view_df, x_col, y_col), width="stretch")
    else:
        g3.info("Cần 2 cột số hợp lệ để vẽ Scatter.")
    g4.pyplot(chart_box(view_df, y_col, group_col), width="stretch")

if __name__ == "__main__":
    main()

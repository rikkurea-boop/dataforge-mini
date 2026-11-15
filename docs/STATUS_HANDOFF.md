# STATUS_HANDOFF — DataForge Mini · T01 (P0) DONE trên nhánh `feat/implementation`

**CURRENT STATE: P0 / T01 DONE ON `feat/implementation` — CHỜ DUYỆT KẾ HOẠCH RÚT GỌN HOẶC TIẾP TỤC T02.** Đã hoàn tất khởi tạo môi trường ảo CPython 3.13.16, cài đặt và xác minh tương thích 5 thư viện, khóa `requirements.txt`.

## Repository và phiên bản nguồn sự thật

- Repository: https://github.com/rikkurea-boop/dataforge-mini (**private**, không đổi quyền).
- Nhánh mặc định trên remote: `main` (PR #1 merge commit `c3d979c20a8a49493139d195130713097ae77b83`, baseline trước T01: `b47682db9705c2c5e279d4e0d79b9f862bbd478e`).
- Nhánh làm việc hiện hành: **`feat/implementation`**.
- **Chưa có** `app.py`, `analysis.py`, `charts.py`, `sample_data.csv`, `tests/test_analysis.py`, PDF, video hay bằng chứng chạy ứng dụng. Không sửa Data-Forge gốc.

## Tiến độ

| Phase | State | Ghi chú |
|---|---|---|
| R01–R07 + FINAL | DONE | Hồ sơ đặc tả đã merge vào `main` qua PR #1 |
| P0 — T01 (Environment & Lock) | **DONE** | Tạo `.venv` Python 3.13.16, `pip check` & smoke import PASS, khóa `requirements.txt` |
| P0–P4 / T02–T10 | **NOT STARTED** | Đang chờ chủ dự án xác nhận phương án gộp bước kế hoạch hoặc mở T02 |

## Quyết định đã khóa

- Ứng dụng 1 trang Streamlit, ba source files Python, một dataset CSV tổng hợp, không thêm DB/ML/CI.
- M01–M07; năm hàm analysis và ba hàm Matplotlib Figure; oracle `12→10`, mean `7.8`, std tổng thể `ddof=0`, GroupBy A8/B7.6, ba biểu đồ.
- Test plan OR-01..15, IO-01..10, UI-01..06 **chưa phải test đã chạy**.
- Gói nộp: GitHub URL giảng viên xem được, YouTube demo, PDF 15–20 trang ≤100 MB, tự đánh giá 3+2+2+1+2. Chi tiết `docs/DELIVERABLES.md`; chưa có sản phẩm nộp.
- **Môi trường đã xác minh (T01):** macOS `26.6.2` (`BuildVersion: 25G83`), CPython `3.13.16`, `numpy==2.5.4`, `pandas==3.1.1`, `matplotlib==3.11.2`, `streamlit==1.67.0`, `pytest==9.2.0` (đã khóa trong `requirements.txt`). Lưu ý: Pandas đang chạy nhánh **3.1.1** — bắt buộc giữ rule `select_dtypes(include=["object", "string", "category"])`.

## Bằng chứng thực thi T01 (2026-11-16)

- Nhánh: `feat/implementation` (từ baseline `b47682db9705c2c5e279d4e0d79b9f862bbd478e`).
- File tạo/sửa: `requirements.txt`, `README.md`, `docs/STATUS_HANDOFF.md` (`.venv/` bị bỏ qua theo `.gitignore`).
- Lệnh & kết quả thực tế:
  - `/opt/homebrew/bin/python3.13 -m venv .venv` + `.venv/bin/python -V` → `Python 3.13.16` (exit 0)
  - `.venv/bin/python -m pip install numpy pandas matplotlib streamlit pytest` → cài đặt thành công `numpy-2.5.4`, `pandas-3.1.1`, `matplotlib-3.11.2`, `streamlit-1.67.0`, `pytest-9.2.0` (exit 0)
  - `.venv/bin/python -m pip check` → `No broken requirements found.` (exit 0)
  - `MPLCONFIGDIR=/tmp/mpl .venv/bin/python -c "import numpy as np, pandas as pd, matplotlib, matplotlib.figure as mf, streamlit as st, pytest; df = pd.DataFrame({'a': [1.0, 2.0]}); s = float(np.std(df['a'].to_numpy(), ddof=0)); fig = mf.Figure(); print('OK', np.__version__, pd.__version__, matplotlib.__version__, st.__version__, pytest.__version__, s)"` → `OK 2.5.4 3.1.1 3.11.2 1.67.0 9.2.0 0.5` (exit 0)

## Điều còn chưa xác minh

Deadline, video length bắt buộc, việc phải làm PPT, PDF template chi tiết, chính sách xem private repo của thầy. Không đoán, kiểm lại trước thời điểm nộp.

## Hành động tiếp theo duy nhất

**Trình chủ dự án phương án tối giản và gộp các bước trong `docs/PLAN.md` (theo yêu cầu mới nhất), hoặc bắt đầu `T02` (tạo `sample_data.csv`).**

## Handoff template

Phase/date, branch/PR, HEAD SHA before/after, files changed, exact commands/results or NOT RUN, blockers/UNKNOWN, next task.

# STATUS_HANDOFF — DataForge Mini · Hoàn tất S01–S05 (Chờ chủ dự án demo & nộp form)

**CURRENT STATE: CODE FROZEN AT `8f49332` & S05 DELIVERABLES PREPARED — AWAITING OWNER'S VIDEO RECORDING & FORM SUBMISSION.** Toàn bộ mã nguồn ứng dụng, kiểm thử (11/11 PASS), báo cáo PDF 18 trang (kiểm định render đủ 18 trang, 373 KB), kịch bản video và đoạn tự đánh giá F06 đã sẵn sàng.

## Repository và phiên bản nguồn sự thật

- Repository: https://github.com/rikkurea-boop/dataforge-mini (**private**, chủ dự án kiểm tra/chỉnh quyền người chấm trước khi nộp form).
- Nhánh đồng bộ trên GitHub: **`main`** và **`feat/implementation`** (PR #1 merge commit cũ: `c3d979c20a8a49493139d195130713097ae77b83`).
- **Code & Dataset Baseline SHA:** **`8f49332b69dc8eeddfc902b098d120cfef74e15a`** (mọi số liệu, ảnh biểu đồ và kết quả kiểm thử `EV-01..13` gắn với commit này; các commit sau nếu có chỉ cập nhật tài liệu hướng dẫn).
- **Đã có trong repo:** `requirements.txt`, `sample_data.csv`, `analysis.py`, `charts.py`, `app.py`, `tests/test_analysis.py`.
- **Đã có ngoài repo (thư mục scratch/brain):** `DataForge_Mini_Bao_Cao_18_Trang.pdf` (18 trang, 382.252 bytes), 3 ảnh biểu đồ chuẩn (`ev07_histogram.png`, `ev08_group_bar.png`, `ev09_scatter.png`), kịch bản video và nội dung tự chấm F06.
- **Chưa có (do chủ dự án tự thực hiện):** chạy app quay video YouTube (F04), điền họ tên/MSSV/link YouTube vào trang 1 & 18 PDF (nếu cần), mở quyền repo (F03) và bấm nộp Google Form. Không sửa Data-Forge gốc.

## Tiến độ

| Bước (Lộ trình 5 bước) | State | Ghi chú |
|---|---|---|
| R01–R07 + FINAL | DONE | Hồ sơ đặc tả đã merge vào `main` qua PR #1 |
| **S01** (T01 — Môi trường) | **DONE** (`011320c`) | `.venv` Python 3.13.16, `pip check` & smoke import PASS, khóa `requirements.txt` |
| **S02** (T02–T05 — Dữ liệu & `analysis.py`) | **DONE** (`ee9ccba`) | `sample_data.csv` (12×4), 5 hàm `analysis.py`, 8/8 tests `pytest` PASS |
| **S03** (T06–T08 — `charts.py` & `app.py`) | **DONE** (`1911d34`) | 3 Figure (`OR-07/08/11/14`), UI Streamlit 1 trang, bắt lỗi & export CSV, 10/10 tests `pytest` PASS |
| **S04** (T09 — QA & Thu minh chứng) | **DONE** (`8f49332`) | UI smoke `AppTest` (`UI-01..06`), `pytest` 11/11 PASS, `pip check` PASS, trích `EV-01..13` |
| **S05** (T10 — Sản phẩm nộp) | **DONE (gói chuẩn bị)** | Đã tạo & kiểm định PDF 18 trang (373 KB), soạn tự chấm F06 (9.5/10) & kịch bản video; chờ user quay & nộp form |

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

## Bằng chứng thực thi S02 (2026-11-16)

- Nhánh: `feat/implementation` (sau commit T01 `011320cd5d754d4f1993c3425a0da061d8480cbc`).
- File tạo/sửa: `docs/PLAN.md`, `sample_data.csv`, `analysis.py`, `tests/test_analysis.py`, `README.md`, `docs/STATUS_HANDOFF.md`.
- Lệnh & kết quả kiểm thử thực tế:
  - `PYTHONPATH=/Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/.venv/bin/python -m pytest -v /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/tests/test_analysis.py` → `8 passed in 0.75s` (exit 0), bao phủ `OR-01..06`, `OR-09..13`, `OR-15` và `IO-01..10`.

## Bằng chứng thực thi S03 (2026-11-16)

- Nhánh: `feat/implementation` (sau commit S02 `ee9ccbacb770ebacec345674491bfe3180e184fc`).
- File tạo/sửa: `charts.py`, `app.py`, `tests/test_analysis.py`, `docs/PLAN.md`, `README.md`, `docs/STATUS_HANDOFF.md`.
- Lệnh & kết quả kiểm thử thực tế:
  - `MPLCONFIGDIR=/tmp/mpl PYTHONPATH=/Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/.venv/bin/python -m pytest -v /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/tests/test_analysis.py` → `10 passed in 1.67s` (exit 0), bao phủ `OR-01..15` và `IO-01..10`, cùng kiểm tra import `app.py`.

## Bằng chứng thực thi S04 (2026-11-16)

- Nhánh: `feat/implementation` (sau commit S03 `1911d3455fe1ace3fb7ecb517a93344e1c75fbfc`).
- File cập nhật: `tests/test_analysis.py`, `docs/PLAN.md`, `README.md`, `docs/STATUS_HANDOFF.md`.
- Lệnh & kết quả kiểm thử thực tế:
  - `MPLCONFIGDIR=/tmp/mpl PYTHONPATH=/Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/.venv/bin/python -m pytest -v /Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/tests/test_analysis.py` → `11 passed in 2.39s` (exit 0), bao phủ `OR-01..15`, `IO-01..10`, `UI-01..06` và `EV-12`.
  - `/Users/hoanglamtung/.gemini/antigravity/scratch/dataforge-mini/.venv/bin/python -m pip check` → `No broken requirements found.` (exit 0).
- Minh chứng `EV-01..13`: xuất 3 biểu đồ PNG chuẩn (`ev07_histogram.png`, `ev08_group_bar.png`, `ev09_scatter.png`) và hồ sơ số liệu `evidence_summary.json` từ commit đóng băng vào thư mục scratch ngoài repo để phục vụ soạn báo cáo PDF ở `S05`.

## Bằng chứng thực thi S05 (2026-11-16)

- File tạo ngoài repo: `DataForge_Mini_Bao_Cao_18_Trang.pdf` (382.252 bytes, 18 trang vật lý đã kiểm tra trực quan từng trang PNG) và tài liệu hướng dẫn nộp bài `GOI_NOP_BAI_DATAFORGE_MINI.md`.
- Tài liệu repo cập nhật: `docs/PLAN.md`, `README.md`, `docs/STATUS_HANDOFF.md` (giữ nguyên Code & Dataset Baseline SHA `8f49332b69dc8eeddfc902b098d120cfef74e15a`).

## Điều còn chưa xác minh

Deadline, video length bắt buộc, việc phải làm PPT, PDF template chi tiết, chính sách xem private repo của thầy. Không đoán, kiểm lại trước thời điểm nộp.

## Hành động tiếp theo duy nhất

**Chủ dự án tải/kéo repo từ GitHub về máy chạy thử (`.venv/bin/python -m streamlit run app.py`), quay video YouTube demo, bổ sung thông tin cá nhân/link YouTube vào PDF (nếu muốn) và tự bấm nộp Google Form.**

## Handoff template

Phase/date, branch/PR, HEAD SHA before/after, files changed, exact commands/results or NOT RUN, blockers/UNKNOWN, next task.

# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Bài học:** Chương 5.5 — NumPy, Pandas, Matplotlib.  
**Mục tiêu:** một ứng dụng nhỏ, đúng trọng tâm, dễ demo; sinh viên giải thích được **toàn bộ code**.

**Trạng thái:** **Bước 2 (`S02`: `T02–T05`) đã hoàn thành** trên nhánh `feat/implementation` — đã tạo bộ dữ liệu mẫu [sample_data.csv](sample_data.csv), module lõi [analysis.py](analysis.py) và bộ test [tests/test_analysis.py](tests/test_analysis.py) (8/8 bài test `pytest` PASS). **Chưa có `charts.py`, `app.py`, PDF hay video.**

## Môi trường đã kiểm chứng (T01 — macOS 26.6.2 / CPython 3.13.16)

- `numpy==2.5.4`, `pandas==3.1.1`, `matplotlib==3.11.2`, `streamlit==1.67.0`, `pytest==9.2.0`
- Khởi tạo và kiểm tra nhanh:

~~~bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
~~~

*(Sau khi các file code và test được tạo ở các bước tiếp theo, chạy kiểm thử bằng `.venv/bin/python -m pytest -q` và chạy ứng dụng bằng `.venv/bin/python -m streamlit run app.py`.)*

## Bắt đầu / AI tiếp quản

1. [AGENTS.md](AGENTS.md) — làm gì ngay khi tiếp quản, cổng quyền.
2. [RULEBOOK.md](RULEBOOK.md) — quy tắc không được vi phạm.
3. [docs/STATUS_HANDOFF.md](docs/STATUS_HANDOFF.md) — trạng thái mới nhất, nhiệm vụ duy nhất tiếp theo.
4. [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) — yêu cầu giảng viên có bằng chứng.
5. [PROJECT_SPEC.md](PROJECT_SPEC.md) — MVP, dữ liệu, hợp đồng hàm, oracle và test.
6. [docs/PLAN.md](docs/PLAN.md) — roadmap và các task giao lập trình sau khi được phép.
7. [docs/DELIVERABLES.md](docs/DELIVERABLES.md) — báo cáo PDF, video, tự chấm, minh chứng.

**Nguồn sự thật hiện tại:** nhánh mặc định **`main`**. Đọc `AGENTS.md`, `docs/STATUS_HANDOFF.md` và các tài liệu tại đây; PR #1 đã merge và lưu lịch sử R01–R07/FINAL. Khi có nhánh triển khai mới, đọc trạng thái và các thay đổi mới nhất trước khi thao tác. Không coi thiết kế/test case là ứng dụng đã chạy.

## Cấu trúc code tối thiểu

~~~text
app.py                 # UI Streamlit một trang (sắp làm ở Bước 3)
analysis.py            # Pandas + NumPy (đã tạo ở Bước 2)
charts.py              # Matplotlib Figure (sắp làm ở Bước 3)
sample_data.csv        # bộ dữ liệu tổng hợp 12×4 (đã tạo ở Bước 2)
requirements.txt       # phiên bản khóa thực tế (đã tạo ở Bước 1)
tests/test_analysis.py # unit test tập trung (đã tạo và PASS ở Bước 2)
~~~

Tài liệu quản lý hiện nằm ngay root và trong `docs/`. **Không thêm `src/`, `services/`, CI/Docker, database hoặc các hệ thống phức tạp.**

## DataForge gốc

[Data-Forge](https://github.com/rikkurea-boop/Data-Forge) là dự án xử lý dữ liệu huấn luyện AI độc lập. **Không import, sửa hoặc phụ thuộc vào Data-Forge gốc** để hoàn thành bài tập này.

## Tiến độ triển khai hiện tại

Theo lộ trình 5 bước tinh gọn trong [docs/PLAN.md](docs/PLAN.md): **Bước 1 (`S01`)** và **Bước 2 (`S02`: `sample_data.csv` + `analysis.py` + `tests/test_analysis.py`)** đã hoàn tất. Nhiệm vụ tiếp theo là **Bước 3 (`S03`: viết `charts.py` và `app.py`)**. Không tự tạo framework bổ sung.

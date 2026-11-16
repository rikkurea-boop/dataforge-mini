# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Chủ đề học phần:** Chương 5.5 — Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib.

## 1. Giới thiệu & Chức năng chính

**DataForge Mini** là ứng dụng web một trang viết bằng Python (Streamlit), được thiết kế tối giản và dễ hiểu để minh họa quy trình phân tích dữ liệu bảng CSV:

- **Đọc & kiểm tra dữ liệu CSV:** Hỗ trợ tải lên file CSV (UTF-8, phân cách dấu phẩy `,`, tối đa 2 MiB) hoặc dùng sẵn bộ dữ liệu giả lập [`sample_data.csv`](sample_data.csv) (12 dòng × 4 cột gồm 2 dòng trùng toàn phần và 2 ô trống).
- **Khám phá & làm sạch dữ liệu:** Hiển thị số dòng, số cột, ô thiếu và dòng trùng lặp. Khi bật công tắc làm sạch, ứng dụng luôn sao chép từ bảng gốc (không làm thay đổi dữ liệu gốc), **xóa dòng trùng toàn phần trước** (`12 → 10` dòng) rồi **điền trung vị theo từng cột số sau** (`Minh.gio_hoc = 4.0`, `Ngoc.diem = 8.0`).
- **Thống kê mô tả (NumPy) & Phân tích nhóm (Pandas):** Tính `count`, `min`, `max`, `mean` (`7.80`), `median` (`8.00`) và độ lệch chuẩn tổng thể `ddof=0` (`≈ 1.2490`), đồng thời tính điểm trung bình theo nhóm bằng `groupby(..., dropna=True)` (Lớp A = `8.0`, Lớp B = `7.6`).
- **Trực quan hóa dữ liệu (Matplotlib):** Vẽ 3 biểu đồ `Figure` độc lập gồm Histogram phân phối tần suất (5 bins), Biểu đồ cột trung bình nhóm (trục tung bắt đầu từ 0) và Biểu đồ phân tán ghép cặp cùng hàng.
- **Xuất dữ liệu:** Tải về file CSV của bảng đang xem (gốc hoặc đã làm sạch) với định dạng UTF-8-SIG, không thêm cột index thừa.

## 2. Cấu trúc dự án

```text
dataforge-mini/
├── app.py                  # Giao diện Streamlit một trang điều phối luồng chạy
├── analysis.py             # Xử lý đọc, kiểm lỗi, làm sạch và thống kê (Pandas + NumPy)
├── charts.py               # 3 hàm tạo biểu đồ độc lập (Matplotlib Figure)
├── sample_data.csv         # Bộ dữ liệu mẫu giả lập (12 dòng × 4 cột)
├── requirements.txt        # Phiên bản thư viện đã kiểm chứng
└── tests/
    └── test_analysis.py    # 11 bài kiểm thử tự động (dữ liệu, thống kê, biểu đồ & UI)
```

## 3. Hướng dẫn cài đặt và chạy ứng dụng

Môi trường đã kiểm chứng trên **macOS (Python 3.13.16)** với các phiên bản thư viện khóa trong [`requirements.txt`](requirements.txt) (`numpy==2.5.4`, `pandas==3.1.1`, `matplotlib==3.11.2`, `streamlit==1.67.0`, `pytest==9.2.0`).

### Bước 1: Tạo môi trường ảo và cài đặt thư viện

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
```

*(Nếu trên máy bạn `python3` đã là Python 3.11–3.13, có thể thay `python3.13` bằng `python3`.)*

### Bước 2: Chạy ứng dụng Streamlit

```bash
.venv/bin/python -m streamlit run app.py
```

Sau khi chạy lệnh trên, trình duyệt sẽ tự mở địa chỉ `http://localhost:8501`.

### Bước 3: Chạy bộ kiểm thử tự động

```bash
.venv/bin/python -m pytest -v
```

# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Chủ đề học phần:** Chương 5.5 — Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib.

## 1. Giới thiệu & Chức năng chính

**DataForge Mini** là ứng dụng web một trang viết bằng Python (Streamlit), được thiết kế tối giản và dễ hiểu để minh họa quy trình phân tích dữ liệu bảng CSV:

- **Đọc & kiểm tra dữ liệu CSV:** Giao diện chỉ hiện phần tải file ban đầu; sau khi người dùng tải lên file CSV (UTF-8, phân cách dấu phẩy `,`, tối đa 2 MiB — ví dụ [`sample_data.csv`](sample_data.csv) có sẵn trong thư mục dự án), chọn tùy chọn làm sạch và nhấn nút **Xác nhận xử lý dữ liệu**, ứng dụng mới tiến hành xử lý và hiển thị kết quả.
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
├── run_app.bat             # Tệp nhấp đúp khởi động nhanh ứng dụng trên Windows
├── run_app.command         # Tệp nhấp đúp khởi động nhanh ứng dụng trên macOS
├── sample_data.csv         # Bộ dữ liệu mẫu giả lập (12 dòng × 4 cột)
├── requirements.txt        # Phiên bản thư viện đã kiểm chứng
└── tests/
    └── test_analysis.py    # 11 bài kiểm thử tự động (dữ liệu, thống kê, biểu đồ & UI)
```

## 3. Hướng dẫn cài đặt và chạy ứng dụng

Môi trường đã kiểm chứng trên **macOS (Python 3.13.16)** với các phiên bản thư viện khóa trong [`requirements.txt`](requirements.txt) (`numpy==2.5.4`, `pandas==3.1.1`, `matplotlib==3.11.2`, `streamlit==1.67.0`, `pytest==9.2.0`).

### Cách 1 (Khuyên dùng — Nhấp đúp không cần gõ lệnh)

- **Trên Windows:** Mở thư mục dự án và **nhấp đúp vào tệp `run_app.bat`**.
- **Trên macOS:** Mở thư mục dự án trong Finder và **nhấp đúp vào tệp `run_app.command`** *(nếu tải `.zip` từ GitHub và macOS hỏi xác nhận lần đầu, nhấp chuột phải vào tệp → chọn **Open / Mở**)*.

Tệp sẽ tự tạo môi trường ảo `.venv`, cài thư viện (nếu chưa có) và tự mở trình duyệt tại `http://localhost:8501`.

### Cách 2 (Chạy thủ công qua Terminal / PowerShell)

#### Bước 1: Tạo môi trường ảo và cài đặt thư viện

- **Windows (Command Prompt / PowerShell):**
```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pip check
```

- **macOS / Linux:**
```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
```

#### Bước 2: Chạy ứng dụng Streamlit

- **Windows:** `.venv\Scripts\python.exe -m streamlit run app.py`
- **macOS / Linux:** `.venv/bin/python -m streamlit run app.py`

Sau khi chạy lệnh trên, trình duyệt sẽ tự mở địa chỉ `http://localhost:8501`.

#### Bước 3: Chạy bộ kiểm thử tự động

- **Windows:** `.venv\Scripts\python.exe -m pytest -v`
- **macOS / Linux:** `.venv/bin/python -m pytest -v`

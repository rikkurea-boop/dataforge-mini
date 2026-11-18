# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Chủ đề học phần:** Chương 5.5 — Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib.  
**Sinh viên thực hiện:** Nguyễn Đức Hải (`B26DCTN046` — Lớp `T26CQHT01-B`).  
**Giảng viên hướng dẫn:** Nguyễn Quang Huy.

## 1. Giới thiệu & Chức năng chính

**DataForge Mini** là ứng dụng web một trang viết bằng Python (Streamlit), được thiết kế tối giản và dễ hiểu để minh họa quy trình phân tích dữ liệu bảng CSV — đồng thời học hỏi các tính năng hữu ích từ những công cụ EDA phổ biến như `ydata-profiling`, `Sweetviz` và `PyGWalker`:

- **Đọc & kiểm tra chất lượng dữ liệu CSV:** Giao diện ẩn kết quả trước khi tải file; sau khi tải lên file CSV (UTF-8, phân cách dấu phẩy `,`, tối đa 2 MiB — ví dụ [`sample_data.csv`](sample_data.csv) hoặc các file trong [`samples/`](samples)), ứng dụng kiểm tra lỗi cấu trúc/giá trị vô cực (`±inf`) và cung cấp bảng hồ sơ chi tiết từng cột (`Kiểu dữ liệu`, `Hợp lệ`, `Ô thiếu`, `Tỷ lệ thiếu %`, `Giá trị duy nhất`).
- **Làm sạch dữ liệu có nút xác nhận:** Hỗ trợ tùy chọn xóa dòng trùng toàn phần (`keep="first"`) và chọn chiến lược xử lý ô số thiếu (**Giữ nguyên**, **Điền trung vị (Median)**, **Điền trung bình (Mean)** hoặc **Xóa dòng bị thiếu (`dropna`)**), chỉ thực thi khi người dùng nhấn **Xác nhận xử lý dữ liệu**. Luôn tạo bản sao độc lập nên không làm thay đổi bảng gốc.
- **Lọc tương tác, sắp xếp & Top 5:** Lọc trực tiếp theo nhiều nhóm (`multiselect`), thanh trượt khoảng giá trị số (`slider`), sắp xếp tăng/giảm dần và xem nhanh **Top 5 cao nhất / thấp nhất** theo cột đang phân tích.
- **Thống kê mô tả (NumPy) & Phân tích nhóm (Pandas):** Tính `count`, `min`, `max`, `mean` (`7.8`), `median` (`8`), độ lệch chuẩn tổng thể `ddof=0` (`≈ 1.25`), các tứ phân vị **Q1 (25%), Q3 (75%), IQR** và số **ngoại lai (Outliers)** theo quy tắc `1.5 × IQR`, cùng điểm trung bình theo nhóm qua `groupby(..., dropna=True)`.
- **Trực quan hóa dữ liệu (4 biểu đồ Matplotlib `Figure` độc lập):**
  1. **Histogram** (5 khoảng tần suất).
  2. **Biểu đồ cột** trung bình theo nhóm (trục tung bắt đầu từ 0).
  3. **Biểu đồ phân tán (Scatter)** ghép cặp cùng hàng kèm hệ số tương quan Pearson `r`.
  4. **Biểu đồ hộp (Boxplot)** quan sát phân vị và điểm ngoại lai theo nhóm.
- **Giao diện 3 tab gọn nhẹ, dùng thử 1 chạm & tự động cập nhật:** Bố cục chia 3 tab tách biệt (`1. Dữ liệu & Làm sạch`, `2. Thống kê mô tả`, `3. Biểu đồ trực quan`), bộ lọc thu gọn trong khung gấp, nút dùng thử nhanh `sample_data.csv` ngay khi mở app; tải về file CSV (UTF-8-SIG, `index=False`) và báo cáo `.txt`; nút **↻ Cập nhật** ở góc trên bên phải cạnh **Deploy** tự kiểm tra và cập nhật bản mới từ GitHub.

## 2. Cấu trúc dự án

```text
dataforge-mini/
├── app.py              # Giao diện Streamlit một trang điều phối luồng chạy
├── analysis.py         # Xử lý đọc, kiểm lỗi, làm sạch, lọc và thống kê (Pandas + NumPy)
├── charts.py           # 4 hàm tạo biểu đồ độc lập (Matplotlib Figure)
├── run_app.bat         # Tệp nhấp đúp khởi động nhanh ứng dụng trên Windows
├── run_app.command     # Tệp nhấp đúp khởi động nhanh ứng dụng trên macOS
├── sample_data.csv     # Bộ dữ liệu mẫu giả lập (12 dòng × 4 cột)
├── samples/            # 10 file CSV mẫu đa dạng (8 bộ hợp lệ/biên + 2 file test báo lỗi)
├── requirements.txt    # Phiên bản thư viện đã kiểm chứng
├── Bao_Cao.docx        # Báo cáo tổng hợp bản Word (chỉnh sửa được)
└── tests/
    └── test_analysis.py  # 13 bài kiểm thử tự động (dữ liệu, thống kê, biểu đồ, UI & auto-update)
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

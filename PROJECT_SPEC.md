# Project Spec – Bản tối giản

## Thông tin được người dùng chốt
- Tên đề tài: **Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python**.
- Tách DataForge Mini ra khỏi DataForge gốc.
- Ưu tiên **càng tối giản, càng đúng trọng tâm**; phải giải thích được **toàn bộ cấu trúc và code**.

## Bối cảnh học phần
Chương 5.5: Phân tích dữ liệu cơ bản với NumPy, Pandas, Matplotlib (theo bối cảnh chat PPT). **Chưa đối chiếu rubric/đề bài chính thức**.

## Người dùng làm được gì (MVP)
1. Chọn file CSV hoặc dataset mẫu (không upload Excel ở MVP).
2. Xem 5 dòng đầu, kích thước, tên/kiểu cột, số giá trị thiếu, số dòng trùng.
3. Nhấn thao tác làm sạch minh bạch: bỏ dòng trùng; điền giá trị thiếu cột số bằng trung vị. Được xem thay đổi trước/sau, dữ liệu gốc vẫn giữ nguyên.
4. Chọn cột số để xem min/max/mean/median/std; nhóm theo cột phân loại nếu dataset có; dùng NumPy trong tính toán thực.
5. Vẽ histogram một cột số, biểu đồ cột theo nhóm, scatter hai cột số bằng Matplotlib (chỉ kích hoạt khi cột hợp lệ).
6. Tải dữ liệu đã làm sạch dạng CSV.

## Công nghệ
Python, NumPy, Pandas, Matplotlib, Streamlit (UI), pytest (kiểm thử). **Không thêm SciPy, sklearn, Plotly, Altair, SQL, database, PDF library** nếu không có yêu cầu đã xác minh.

## Thiết kế tối giản
`app.py` giao diện; `analysis.py` xử lý/đo lường; `charts.py` tạo hình; `tests/test_analysis.py` đối chiếu logic. Không cần factory pattern, service/repository layer hay plugin system.

## Chất lượng & nghiệm thu
- Toàn bộ flow hoạt động offline trên máy đã cài dependency.
- Kết quả fixture 5 sinh viên: điểm `[8,6,9,7,10]` mean = 8, lớp A = 9, lớp B = 6.5; 3 sinh viên đạt >= 8.
- Dữ liệu lỗi: có ít nhất một NaN và một dòng trùng; thể hiện thay đổi trước/sau; không đổi dữ liệu gốc.
- Empty CSV/invalid column/series không có số: có thông báo dễ hiểu thay vì crash.
- Người thuyết trình giải thích được từng file, function chính, input/output và thư viện dùng.
- Một người mới clone repo có thể làm theo README và chạy demo (chỉ xác nhận sau khi thực tế triển khai).

## Không làm
AI training, ML prediction, advanced PCA, streaming, REST backend, deployment phức tạp, multi-user, phân quyền, tự động sinh slide, DOCX/PDF từ app, data warehouse, báo cáo enterprise.

## Bàn giao môn học (kế hoạch, chưa xác minh)
Dự kiến: code/demo, slide giới thiệu flow/code, báo cáo và video nếu thầy yêu cầu. Không đặt số trang, số slide hay deadline khi chưa có nguồn.

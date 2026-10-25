# Project Spec – Bản tối giản

**Trạng thái:** DRAFT, chuẩn bị trước implementation. R01 đã xác minh các yêu cầu nộp bài; các quyết định MVP sẽ được rà soát và khóa ở R02–R03.

## Quyết định của người dùng
- **Tên đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.
- **DataForge Mini độc lập** với Data-Forge gốc; không phụ thuộc hoặc làm thay đổi source của dự án gốc.
- **Tối giản, đúng trọng tâm; người học phải trình bày lại được toàn bộ code.**
- Giai đoạn hiện tại **chỉ research/chuẩn bị 7 lượt + 1 lượt kiểm định**, không phát triển ứng dụng khi chưa có lệnh bắt đầu.

## Yêu cầu thầy đã xác minh từ ảnh (xem docs/REQUIREMENTS.md)
- Chọn chủ đề **Chương 5.5: NumPy, Pandas và Matplotlib**.
- Bài nộp **cá nhân**.
- **Bắt buộc**: link mã nguồn GitHub hoặc tương đương; link video YouTube demo; PDF báo cáo **15–20 trang** tối đa **100 MB**; đoạn tự nhận xét và tự chấm theo 5 tiêu chí.
- Thang **tự đánh giá**: hoàn thành chức năng 3; kỹ thuật Python 2; chất lượng code 2; giao diện/trực quan 1; báo cáo/minh chứng 2.
- Deadline, thời lượng video, yêu cầu PPT, template PDF: **chưa xác minh**.

## Luồng MVP đang đề xuất – CHƯA KHÓA
1. Chọn file CSV hoặc dataset mẫu.
2. Xem vài dòng đầu, kích thước, kiểu cột, số giá trị thiếu và trùng.
3. Làm sạch minh bạch: loại bản ghi trùng, tùy chọn điền thiếu ở cột số (trung vị); dữ liệu gốc giữ nguyên.
4. Thống kê min/max/mean/median/std trên cột số, nhóm theo lớp nếu phù hợp, có phép toán NumPy thực sự.
5. Biểu đồ Matplotlib: histogram, bar theo nhóm, scatter hai cột số khi đủ điều kiện.
6. Tải CSV sau xử lý.

**Phân biệt:** các bước trên do AI đề xuất để chứng minh ba thư viện; biểu mẫu của thầy **không chỉ định chính xác Streamlit/CSV/3 biểu đồ**. R02–R03 phải đánh giá lại độ tối giản trước khi chốt.

## Stack dự kiến – CHƯA KHÓA
Python, Pandas, NumPy, Matplotlib; Streamlit nếu cần GUI web tối giản; pytest để test. Không đưa SciPy/sklearn/Altair/Plotly/SQL/DB/AI backend hoặc PDF engine vào app nếu không có lý do trực tiếp từ yêu cầu.

## Cấu trúc đề xuất – CHƯA KHÓA
- app.py: UI mỏng (nếu dùng Streamlit).
- analysis.py: đọc/làm sạch/thống kê dữ liệu.
- charts.py: 2–3 biểu đồ Matplotlib.
- tests/test_analysis.py: test logic đối chứng.
Không sử dụng service/repository/factory layer, không trộn DataForge core gốc.

## Tiêu chí nghiệm thu nội bộ – thiết kế dự kiến
- Dữ liệu mẫu 5 sinh viên có điểm [8,6,9,7,10], mean 8.0, lớp A 9.0, lớp B 6.5, số điểm >=8 là 3.
- Dữ liệu lỗi (fixture độc lập) có NaN và duplicate; kết quả cleaning được đối chiếu, dữ liệu gốc không mutate.
- Trường hợp CSV rỗng, không có cột số hoặc cột vẽ biểu đồ không hợp lệ phải được xử lý.
- Có code chạy thật dùng từng thư viện NumPy/Pandas/Matplotlib; có bằng chứng test, ảnh biểu đồ, video demo.
- Người học hiểu từng file/hàm, không chỉ bấm chạy UI.

## Không làm khi chưa có yêu cầu mới
ML training/prediction; hệ thống pipeline dữ liệu lớn; login/auth; API/backend; database; đa người dùng; cloud deployment; PCA; hệ thống report PDF trong app; automation/AI/chatbot.

## Sản phẩm nộp chính thức
**GitHub code link + YouTube demo link + PDF 15–20 trang (<=100 MB) + đoạn tự đánh giá 5 tiêu chí.** Việc tạo slide PPT để hỗ trợ cá nhân là tùy chọn cho đến khi có thêm nguồn từ thầy.

**Cổng bắt đầu code:** chỉ sau R01–R07 và lượt kiểm định cuối đạt READY FOR IMPLEMENTATION, và user yêu cầu bắt đầu.

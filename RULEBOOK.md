# Rulebook v1.0 – DataForge Mini

**Định hướng khóa ngày 2026-10-25:** **Tối giản – Đúng trọng tâm – Hiệu quả – Dễ giải thích toàn bộ code.**

1. **SSOT:** Repository này chứa nguồn sự thật về mã nguồn, tiến độ, quyết định, bài tập và handoff. Chat cũ chỉ là bối cảnh, không thay bằng chứng trong repo.
2. **Phạm vi:** Ứng dụng nhỏ cho NumPy, Pandas, Matplotlib. Không kế thừa kiến trúc Data-Forge gốc. Không cần mô hình AI, machine learning, đăng nhập, database, cloud, API, plugin, đa tiến trình, pipeline framework.
3. **Chức năng MVP tối thiểu:** nhập **CSV** → xem dữ liệu → kiểm tra/làm sạch dữ liệu thiếu và trùng → thống kê số → vẽ 2–3 kiểu biểu đồ **Matplotlib** → tải CSV kết quả. Excel, report PDF, undo nhiều bước, biểu đồ nâng cao là **không bắt buộc**.
4. **Giải thích được code:** mỗi file có vai trò rõ; ưu tiên hàm đơn giản thay class/framework; không tạo quá nhiều file; chú thích ngắn tại phần logic quan trọng; tránh code dài khó thuyết trình.
5. **Dùng đúng thư viện:** Pandas để đọc/lọc/làm sạch/groupby; NumPy có ít nhất 2 phép tính số thực sự dùng và có thể chứng minh; Matplotlib tạo biểu đồ thực sự; Streamlit chỉ đảm nhận UI.
6. **An toàn dữ liệu:** không thay đổi dữ liệu gốc khi làm sạch; hiển thị trước/sau; không tự động xóa hàng/cột không thông báo; không dùng dữ liệu cá nhân thực.
7. **Độ chính xác:** tính toán có test đối chiếu dữ liệu mẫu; xử lý NaN, file rỗng, cột không phù hợp; không diễn giải tương quan thành nhân quả; không bịa kết quả.
8. **Tài liệu gọn:** tránh sinh 20–30 tài liệu, các hệ thống rule trùng lặp hoặc ma trận status quá mức. Chỉ cập nhật đúng các file điều phối hiện tại.
9. **Không nâng scope:** Nếu tính năng không trực tiếp giúp chứng minh Pandas/NumPy/Matplotlib hoặc giải thích trước thầy thì bỏ. Yêu cầu mới phải có lý do và user duyệt.
10. **Git:** feature branch/PR; không force push/xóa lịch sử/merge code chưa test; tránh sửa file của phiên khác; mọi claim "đã xong" phải có commit hoặc output test.
11. **Nguồn gốc:** không clone code của bên thứ ba rồi nói là tự viết; giữ license và trích nguồn khi dùng.
12. **Handoff:** kết phiên cập nhật `docs/STATUS_HANDOFF.md` với nhiệm vụ hoàn thành/chưa hoàn thành, mã commit, test và bước tiếp theo.
13. **Đồng bộ bài thuyết trình:** PPT/video/report chỉ giới thiệu những tính năng đã chạy; biểu đồ và con số khớp dataset/commit demo.
14. **Thiếu yêu cầu chính thức:** không suy diễn deadline, rubric, độ dài slide/video/báo cáo; ghi trong `docs/REQUIREMENTS.md`.
15. **Definition of Done:** code chạy được, test logic đạt, demo được, giải thích được vai trò từng hàm/thư viện; không coi tài liệu lập kế hoạch là sản phẩm.

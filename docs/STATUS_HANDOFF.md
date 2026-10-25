# Status & AI Handoff — 2026-10-25, Research 01

## Repo và luồng làm việc
- Repo: https://github.com/rikkurea-boop/dataforge-mini (private).
- main hiện chỉ có README khởi tạo.
- Tài liệu gốc thuộc nhánh docs/project-charter-ai-handoff, PR #1: https://github.com/rikkurea-boop/dataforge-mini/pull/1.
- Lượt R01 cập nhật tài liệu **trên cùng branch/PR #1**, không merge vào main.
- **Chưa tạo source app, tests, dataset hay dependency file. Chưa chạy ứng dụng/pytest.**

## Progress
- **R01: HOÀN THÀNH nghiên cứu, chờ owner nghiệm thu nếu cần.**
- R02–R07: NOT STARTED.
- FINAL review: NOT STARTED.
- Implementation P0–P4: **BLOCKED — user chưa cho phép; không tự triển khai.**

## Research 01 — phát hiện đã đối chiếu nguồn gốc
Hai ảnh form người dùng gửi 2026-10-25 xác minh:
- Dự án cá nhân Chương 5, chủ đề 5.5 "Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib".
- Bắt buộc link GitHub, link YouTube demo, file PDF 15–20 trang <=100MB, đoạn tự nhận xét và tự chấm theo 3+2+2+1+2.
- Người nộp kiểm tra thông tin cá nhân.
- Deadline, PPT, thời lượng video chưa thấy trong vùng ảnh; không khẳng định không có.
- Repo hiện private: phải xác minh quyền xem lúc nộp.
- YouTube private hạn chế chia sẻ, nên cần phương án video có thể mở được bằng link.

**Lỗi tài liệu cũ đã sửa:** đánh dấu video/PDF "nếu thầy yêu cầu" hoặc "UNKNOWN" — giờ xác định là BẮT BUỘC. Đồng thời sửa kế hoạch để AI không tự bắt đầu P0/P1 khi owner đang yêu cầu research 7+1.

## Quyết định/ranh giới
- Đề tài: "Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python".
- Tối giản và giải thích được toàn bộ code; không tích hợp Data-Forge gốc.
- **Gợi ý** Streamlit/CSV/3 biểu đồ chưa được coi là yêu cầu chính thức, sẽ được R02/R03 kiểm tra.
- Không tự xuất bản repo public hoặc thay visibility, không tự viết app/video/PDF.

## Việc tiếp theo duy nhất
**R02 — Nghiên cứu MVP và dataset.** Đọc docs/REQUIREMENTS.md, đánh giá kỹ 5 tiêu chí tự chấm và lựa chọn đúng mức độ chức năng tối thiểu, dataset minh chứng, luồng demo. Kết quả R02 cập nhật PROJECT_SPEC.md/PLAN.md và handoff; không code.

## Định dạng handoff về sau
- Lượt, ngày, branch/PR, commit SHA, changed files:
- Nguồn đã xác minh / suy luận / đề xuất:
- Checklist nghiệm thu của lượt:
- Không làm / chưa làm:
- Nhiệm vụ kế tiếp duy nhất:
- Có cần owner quyết định ngoài phạm vi không:

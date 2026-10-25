# STATUS_HANDOFF — FINAL COMPLETE · 2026-10-25

**FINAL PASS — READY FOR IMPLEMENTATION (PLAN ONLY).** **NOT AUTHORIZED TO CODE**: chờ lệnh mới của chủ dự án. Không có app/code Python, sample CSV, dependencies, tests, PDF, video hay evidence thực.

## GitHub và source of truth
- Repo private: https://github.com/rikkurea-boop/dataforge-mini
- Docs branch: `docs/project-charter-ai-handoff`, open PR #1: https://github.com/rikkurea-boop/dataforge-mini/pull/1
- `main` vẫn chỉ có README ban đầu. Toàn bộ tài liệu đang ở PR; AI mới phải nhận URL nhánh/PR cho đến khi owner cho phép merge. **Không tự merge hoặc đổi visibility**.
- Nhánh research gồm **9 file** (8 Markdown và .gitignore), chưa có code. Data-Forge gốc không được đụng tới.

## Trạng thái
| Phase | Trạng thái |
|---|---|
| R01–R07 | DONE — research/spec only |
| FINAL | **PASS — plan ready**, independent cross-review complete |
| P0–P4 (T01–T10) | **NOT STARTED; PERMISSION BLOCKED** |

## Kết quả kiểm định FINAL
- Đọc 9 file, PR/head/tree, crossrefs và nội dung thầy đã được trích từ ảnh ở R01: F01–F06, link mã nguồn, YouTube, PDF 15–20 trang ≤100MB, tự đánh giá 3+2+2+1+2. **Chưa có ảnh gốc lưu trong repo**; nếu thầy cập nhật form phải kiểm trực tiếp.
- Kiểm đủ MVP 7 chức năng M01–M07, ba file Python dự kiến, 5+3 hợp đồng hàm, test behaviors 15 OR + 10 IO + 6 UI, 10 tasks T01–T10 và 16 evidence EV. Đề cương PDF đúng 18 trang dự kiến.
- **Kiểm tính toán độc lập, không chạy app:** pandas 2.2.3 / NumPy 2.3.5, raw12x4, duplicate2, NA2; cleaned10x4, median giờ4/điểm8, grade mean7.8, variance1.56, population std≈1.24899959968, groups A8/B7.6, histogram 5 bins [2,2,3,2,1], scatter 10 pairs. Median fill cũng có thể tạo duplicate mới trên input khác.
- Đã sửa thực tế: tham chiếu § cũ trong DELIVERABLES, T02 không thể phụ thuộc OR-01 trước T03, tách exception loader khỏi lỗi UI, kiểm URL repo trong T10, và quy tắc pandas 2/3 dtype + header trùng. Ghi baseline SHA cho code/data riêng các commit chỉ sửa README/STATUS.
- Markdown/link nội bộ và cây 9 file hợp lệ; không phát hiện phụ thuộc code/app bên ngoài. **Không chạy pytest, chưa pin packages, chưa kiểm tương thích chạy app hoặc xuất PDF/video.**

## Những việc còn mở — không cản chuẩn bị coding
Deadline, PPT có bắt buộc không, thời lượng video, PDF template chi tiết, quyền xem code khi repo private, OS thực và chính xác bộ phiên bản package (xác minh trong P0). Nội dung trong form chưa thấy hết: kiểm lại trước khi nộp.

## Bước tiếp theo duy nhất
**Owner xem xét việc merge PR #1 vào `main`** để AI mới mở repo mặc định thấy tài liệu, hoặc tiếp tục dùng trực tiếp docs branch. Sau đó **owner chủ động giao lệnh bắt đầu T01** nếu muốn triển khai. Quyết định FINAL PASS không phải lệnh viết app.

## Update format khi có tiến độ mới
Phase, date, branch/PR, SHA trước/sau, file sửa, lệnh test đã chạy và kết quả hoặc NOT RUN, blocker, next single task.

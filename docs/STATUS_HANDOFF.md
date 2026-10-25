# STATUS_HANDOFF — DataForge Mini · 2026-10-25 · End of R07

**Trạng thái:** **RESEARCH 7/7 DONE — FINAL CROSS-QA NEXT. NOT READY FOR IMPLEMENTATION.** Không có source app/test/CSV thật, không có PDF/video/EV thật; test app chưa chạy.

## Repo và bằng chứng hiện tại
- Repo: https://github.com/rikkurea-boop/dataforge-mini (**private**).
- Nguồn tài liệu: branch `docs/project-charter-ai-handoff`, PR #1 https://github.com/rikkurea-boop/dataforge-mini/pull/1 (**open, chưa merge** tại thời điểm R07).
- `main` lúc bắt đầu R07 vẫn chỉ có README ban đầu. PR là nơi chứa toàn bộ tài liệu.
- **Hạn chế tiếp quản:** URL repo nhánh mặc định có thể không hiển thị tài liệu khi PR chưa merge. Cho AI mới URL nhánh/PR; FINAL xem xét đề xuất hợp nhất vào `main`, **không tự merge khi chưa có chấp thuận của chủ dự án**.
- R07: chuẩn hóa `README.md`, `AGENTS.md`, `RULEBOOK.md`, `PROJECT_SPEC.md`, `docs/REQUIREMENTS.md`, `docs/PLAN.md`, `docs/STATUS_HANDOFF.md`; giữ `docs/DELIVERABLES.md` làm nguồn kế hoạch nộp. Không đổi Data-Forge gốc.
- HEAD SHA chính xác: kiểm tra trực tiếp PR trước khi làm, không tái sử dụng SHA ghi trong chat.

## Trạng thái giai đoạn
| Phase | Status | Evidence |
|---|---|---|
| R01 | DONE (docs) | Đề/biểu mẫu và tiêu chí tự đánh giá |
| R02 | DONE (docs) | MVP scope + một dataset 12→10 |
| R03 | DONE (docs) | 3 file Python được đề xuất + 8 hợp đồng hàm |
| R04 | DONE (docs) | Oracle toán, std ddof0, NaN/inf/duplicates |
| R05 | DONE (docs) | 31 test cases dạng **đặc tả**, env chỉ là đề xuất |
| R06 | DONE (docs) | PDF/video/EV evidence plan, **không sản xuất** |
| R07 | **DONE (docs)** | Rulebook, AI handoff, task packets và các quyết định hợp nhất |
| FINAL | **NEXT, NOT STARTED** | Kiểm định độc lập trước khi cho phép coding |
| P0–P4 | **BLOCKED** | Chỉ bắt đầu nếu FINAL đạt READY và owner có lệnh mới |

## R07 audit, sửa đổi
- Giảm nội dung trùng giữa tài liệu. Mỗi nhóm thông tin có một file chủ: requirement / spec / plan / deliverable / status.
- Bảo toàn sample 12 records và oracle, 5+3 hợp đồng hàm, 31 test IDs, yêu cầu PDF/YouTube/self-eval và EV IDs.
- Giữ **9 file tổng** (8 Markdown + .gitignore), không sinh docs mới/đường dẫn phức tạp; lịch sử nghiên cứu cũ có thể truy ở commit của PR.
- Làm rõ các điểm dễ hiểu nhầm: plan kiểm thử không phải test pass; thư viện mới chỉ ứng viên; PDF bắt buộc nhưng PDF generator không bắt buộc; R07 DONE không phải READY.
- Không có runtime/pytest outputs; không hứa đã chạy code hoặc nộp form.

## Việc tiếp theo DUY NHẤT: FINAL CROSS-QA
1. Đọc toàn bộ 9 file, kiểm tra GitHub PR/head, crossrefs, Markdown và không có source app.
2. Đối chiếu yêu cầu giảng viên F02–F06 với spec/task/deliverables; kiểm oracle/tính đúng và thuật ngữ.
3. Kiểm không có phát biểu chưa xác minh được diễn đạt thành yêu cầu thầy hoặc "đã chạy".
4. Kiểm tính khả thi của P0–P4 và hướng dẫn resume cho AI mới, không mở rộng scope.
5. Sửa có chọn lọc lỗi thật, ghi kết quả PASS/BLOCKED vào STATUS; chỉ khi đủ điều kiện có thể đặt `READY FOR IMPLEMENTATION` về **tài liệu**, không phải code.
6. **Vẫn chưa code trong FINAL.** Sau FINAL, chờ owner chủ động giao việc mới.

## Những điều còn UNKNOWN
Deadline, độ dài video bắt buộc, PPT, template PDF, tên/chi tiết các trường form ngoài vùng ảnh; hệ điều hành máy sẽ chạy app; tổ hợp phiên bản packages cuối sau cài đặt. Không suy đoán.

## Mẫu cập nhật bàn giao
- Date / task-phase / branch / PR / before→after SHA:
- Files changed & justification:
- Evidence commands/tests run and exact outcomes (hoặc "not run"):
- DONE/PARTIAL/BLOCKED + unresolved/UNKNOWN:
- Next single task and permission gate:

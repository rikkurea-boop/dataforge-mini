# AGENTS.md — Giao thức tiếp quản bắt buộc

## 0. START HERE — trước mọi thay đổi

1. Đọc `README.md` → `RULEBOOK.md` → `docs/STATUS_HANDOFF.md` → `docs/REQUIREMENTS.md` → `PROJECT_SPEC.md` → `docs/PLAN.md` → `docs/DELIVERABLES.md`. **Đọc file thật từ GitHub**, không suy luận chỉ từ tên file hoặc thông tin chat.
2. Xác minh repo, visibility, **nhánh mặc định `main` và nhánh làm việc hiện hành**, HEAD SHA, PR liên quan, tree và tình trạng các file/test **thực sự tồn tại**. PR #1 là lịch sử đã merge, không phải nhánh cần đọc để lấy đặc tả mới nhất.
3. Xác định phase **R01–R07 / FINAL / P0–P4** trong STATUS_HANDOFF; không tự nhảy phase.
4. Thông báo ngắn: trạng thái có chứng cứ, nhiệm vụ tiếp theo duy nhất, điều còn bất định, và loại thay đổi được phép làm.
5. Nếu gặp mâu thuẫn: **yêu cầu thầy có bằng chứng > yêu cầu mới nhất của chủ dự án > RULEBOOK > REQUIREMENTS/PROJECT_SPEC/DELIVERABLES theo đúng phạm vi > PLAN > gợi ý AI cũ**. Ghi vấn đề tại STATUS_HANDOFF, không âm thầm bỏ qua.

## 1. CỔNG QUYỀN — quan trọng hơn mọi đề xuất

**CURRENT: R01–R07 + FINAL PASS, bộ tài liệu đã được merge vào `main` qua PR #1 — READY FOR IMPLEMENTATION (chỉ kế hoạch).** Đây **không phải lệnh lập trình**. Chờ chủ dự án chủ động giao bắt đầu T01 hoặc triển khai ứng dụng. Hiện chưa có app, CSV thực, dependencies, source test, PDF hay video.

**Chỉ được bắt đầu P0 khi BOTH:**
- FINAL hoàn tất, ghi `READY FOR IMPLEMENTATION` trong STATUS_HANDOFF kèm checklist/commit có căn cứ; **và**
- chủ dự án **chủ động giao lệnh bắt đầu viết ứng dụng** sau FINAL.

Nếu chưa thỏa cả hai: chỉ được làm research/QA/documentation, không tự giải thích việc "AI mới tiếp quản" là lệnh coding.

## 2. Quy trình một nhiệm vụ sau khi được phép

1. Lấy **một task nhỏ** từ `docs/PLAN.md`, kiểm các phụ thuộc đã đạt; chỉ sửa file trong phạm vi task, không tự mở scope.
2. Thực hiện; chạy command/test thích hợp; ghi **lệnh, Python/packages thực tế, kết quả và SHA**. Không coi test *được mô tả* là test *đã chạy*.
3. Đối chiếu `PROJECT_SPEC.md` (oracle OR/IO/UI) và `docs/DELIVERABLES.md` (EV evidence). Sửa đúng lỗi thay vì thêm tầng trừu tượng.
4. Commit/PR thay đổi trên branch riêng; không force push, không tự merge, không xóa lịch sử, không sửa repo Data-Forge gốc.
5. Cập nhật `docs/STATUS_HANDOFF.md`: task DONE/PARTIAL/BLOCKED, file đã sửa, command/test output, commit/PR, điều chưa đạt, **next single task**.
6. Nếu code đổi sau khi thu minh chứng, rà lại EV/PDF/video có bị lệch phiên bản hay không.

## 3. Giới hạn code và minh chứng

- Ứng dụng **chỉ ba file Python chính**: `app.py` (UI), `analysis.py` (data/stats), `charts.py` (figures). Chỉ một dataset CSV tổng hợp. Không class/service/repository/cache/session-state tùy biến/ML/database.
- NumPy, Pandas, Matplotlib phải **được thực thi thật**, Streamlit chỉ là giao diện. Test dùng pytest; không cần browser automation.
- Tính toán: xem PROJECT_SPEC về `ddof=0`, NA/infinity, group, duplicate, histogram, scatter. Không bịa kết quả hoặc tuyên bố QA pass khi chưa chạy.
- Sản phẩm nộp bắt buộc: mã nguồn người chấm truy cập được, video YouTube, PDF 15–20 trang ≤100 MB, đoạn tự chấm theo 3+2+2+1+2. Không sinh PDF từ chính ứng dụng.
- Không lộ thông tin cá nhân/token trong GitHub, video hoặc screenshots. Chủ dự án quyết định public/private và nộp bài.

## 4. Prompt kích hoạt coding sau FINAL (TEMPLATE — KHÔNG phải lệnh hiện tại)

> Tiếp tục DataForge Mini từ repo trên. Xác minh FINAL = READY FOR IMPLEMENTATION và lệnh user cho phép coding đã được đưa ra. Đọc AGENTS, RULEBOOK, STATUS_HANDOFF, REQUIREMENTS, PROJECT_SPEC, PLAN, DELIVERABLES và source hiện có. Chỉ thực hiện task **[mã task trong PLAN]** theo đúng file scope, acceptance, unit tests và handoff. Không thêm tính năng hay framework ngoài phạm vi. Nếu thiếu gate, chỉ báo blocker, không code.

**Cách kiểm tra tiến độ:** mở STATUS_HANDOFF và PR; task chưa có file/test/commit thì chưa thể nói "đã hoàn thành".

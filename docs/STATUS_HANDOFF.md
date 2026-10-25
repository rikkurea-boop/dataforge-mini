# STATUS_HANDOFF — DataForge Mini · Sau FINAL và PR #1 merge

**CURRENT STATE: READY FOR IMPLEMENTATION (PLAN ONLY) — AWAITING OWNER'S CODING ORDER.** R01–R07 và FINAL đã hoàn thành. **Chưa triển khai T01/P0; không được tự bắt đầu code chỉ vì đọc được file này.**

## Repository và phiên bản nguồn sự thật

- Repository: https://github.com/rikkurea-boop/dataforge-mini (**private**, không đổi quyền).
- Nhánh mặc định và **source of truth hiện tại: `main`**.
- PR #1 https://github.com/rikkurea-boop/dataforge-mini/pull/1 **đã merge**; merge commit `c3d979c20a8a49493139d195130713097ae77b83`. Những commit sau đó chỉ đồng bộ thông tin hậu merge; **luôn kiểm tra HEAD mới nhất**, không coi SHA trong tài liệu là HEAD hiện tại.
- 9 file tài liệu/cấu hình (8 Markdown + `.gitignore`) là bộ nền hiện tại; lịch sử nghiên cứu có ở PR #1.
- **Chưa có** `app.py`, `analysis.py`, `charts.py`, `sample_data.csv`, `requirements.txt`, tests, PDF, video hay bằng chứng chạy ứng dụng. Không sửa Data-Forge gốc.

## Tiến độ

| Phase | State | Ghi chú |
|---|---|---|
| R01–R07 | DONE — research | Form, MVP, architecture, math, QA, deliverables, AI handoff |
| FINAL | PASS — plan ready | Kiểm độc lập, sửa mâu thuẫn, khóa scope |
| Publication of docs | DONE — PR #1 merged | Bộ tài liệu đọc được trực tiếp trên `main` |
| P0–P4 / T01–T10 | **NOT STARTED — PERMISSION BLOCKED** | Chờ lệnh cụ thể của chủ dự án |

## Quyết định đã khóa

- Ứng dụng 1 trang Streamlit, ba source files Python, một dataset CSV tổng hợp, không thêm DB/ML/CI.
- M01–M07; năm hàm analysis và ba hàm Matplotlib Figure; oracle `12→10`, mean `7.8`, std tổng thể `ddof=0`, GroupBy A8/B7.6, ba biểu đồ.
- Test plan OR-01..15, IO-01..10, UI-01..06 **chưa phải test đã chạy**.
- Gói nộp: GitHub URL giảng viên xem được, YouTube demo, PDF 15–20 trang ≤100 MB, tự đánh giá 3+2+2+1+2. Chi tiết `docs/DELIVERABLES.md`; chưa có sản phẩm nộp.
- Python 3.13 và package versions là mục tiêu kiểm nghiệm ở T01, chưa phải environment verified.

## Bằng chứng hoàn thành FINAL (docs, không phải app)

- Đã đọc và đối chiếu 9 file, liên kết nội bộ, 7 M / 8 contracts / 15 OR / 10 IO / 6 UI / 10 T / 16 EV / đề cương 18 trang.
- Tính lại dataset tạm bằng Pandas/NumPy: raw 12 dòng, 2 duplicate, 2 thiếu; clean10, medians4/8, mean7.8, variance1.56, std≈1.249, nhóm A8/B7.6, histogram 5 bins [2,2,3,2,1].
- Đã sửa tham chiếu mục cũ, dependency T02/T03, cột text pandas 2/3, header trùng và minh chứng Git SHA baseline.
- **Không chạy app, pytest, môi trường cài đặt thực, không tạo PDF hoặc video.**

## Điều còn chưa xác minh

Deadline, video length bắt buộc, việc phải làm PPT, PDF template chi tiết, chính sách xem private repo của thầy và phiên bản thư viện/máy triển khai. Không đoán, kiểm lại trước thời điểm nộp.

## Hành động tiếp theo duy nhất

**Chờ chủ dự án giao lệnh bắt đầu T01 (P0: chuẩn bị môi trường và kiểm tương thích các thư viện).** Sau khi có lệnh, thực hiện đúng `docs/PLAN.md` và cập nhật file này bằng command/test evidence, trạng thái và SHA của commit.

## Handoff template

Phase/date, branch/PR, HEAD SHA before/after, files changed, exact commands/results or NOT RUN, blockers/UNKNOWN, next task.

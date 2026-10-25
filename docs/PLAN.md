# PLAN — research-first, minimal-first

**Tiến độ:** R01–R06 hoàn thành về mặt nghiên cứu; **R07 là lượt tiếp theo**. Đang ở pha CHỈ NGHIÊN CỨU, không được tạo code cho đến R01–R07 + FINAL và owner giao bắt đầu.

## A. 7 research sessions + 1 final review

| Lượt | Phạm vi, sản phẩm | Trạng thái |
|---|---|---|
| R01 | Đối chiếu form thầy, requirement IDs F01–F06, gates, điểm tự đánh giá → docs/REQUIREMENTS.md | DONE |
| R02 | Khóa **MVP design baseline và dataset chính 12→10**, sơ đồ use case, so sánh công nghệ → PROJECT_SPEC.md | DONE |
| R03 | Thiết kế **3 file Python**, hợp đồng 5 hàm analysis + 3 chart, một trang Streamlit rerun không custom state, kiến trúc một chiều | DONE |
| R04 | Độc lập xác minh CSV & oracle, ddof0, NA/inf, new duplicates after fill, histogram5, bar/scatter, OR-01..15 | DONE |
| R05 | Đặc tả OR-01..15 + IO-01..10 + UI-01..06; Python 3.13, dependency candidate bounds, P0 exact-pin gate, fresh venv & smoke | DONE |
| R06 | docs/DELIVERABLES.md: report 18-page target, ~7-minute video, EV-01..16, self-eval and PDF/link checks | DONE |
| R07 | Hoàn thiện rules/handoff, coding tasks & prompt cho AI sau này; tránh trùng tài liệu | NEXT |
| FINAL | Đối chiếu chéo mọi tài liệu; khóa baseline trước coding | NOT STARTED |

Không cần 7 file research riêng: kết quả mỗi lượt được hòa vào **PROJECT_SPEC.md**, **docs/REQUIREMENTS.md**, **docs/PLAN.md**, **RULEBOOK.md**, **AGENTS.md** và **docs/STATUS_HANDOFF.md**. R06 đã tạo `docs/DELIVERABLES.md`; không sinh thêm tài liệu trùng nội dung.

## B. R02: danh sách chức năng / thứ tự demo đã lựa chọn

**MVP CORE:** 
1. Upload CSV hoặc tự nạp `sample_data.csv`.
2. Hiển thị 12 dòng, 4 cột, 2 duplicate, 2 missing; xem vài dòng đầu.
3. Một công tắc Clean: exact drop duplicates → numeric median fill, không sửa bảng raw; xem so sánh 12→10, NaN 2→0.
4. Numeric mean/median/std/min/max; groupby `lop`–`diem`; NumPy có tính toán thực.
5. Matplotlib: histogram `diem`, bar `lop`–điểm TB, scatter `gio_hoc`–`diem`.
6. Download CSV đang xem.

**Ngoài phạm vi:** Excel, biểu đồ nâng cao/custom theme, phân trang, login, database, machine learning, Data-Forge gốc, Undo history, PDF generator **trong app**. Báo cáo **PDF bên ngoài app** vẫn bắt buộc khi nộp.

**R03 đã quyết:** app.py / analysis.py / charts.py (3 files); 5 analysis functions + 3 Matplotlib Figure functions; không dùng st.session_state custom; `st.pyplot(fig)` với Figure tạo trực tiếp. Chi tiết hợp đồng ở PROJECT_SPEC §10. **R04 đã khóa toán; R05 đã lập QA/env plan**; xem PROJECT_SPEC §§11–12.

## C. Dataset (đặc tả duy nhất; chưa tạo file)

Dữ liệu CSV giả lập 12 hàng / 4 cột nằm nguyên văn tại **PROJECT_SPEC.md §5**. Chỉ tạo một file `sample_data.csv` ở P0; không phân tách clean/dirty CSV.

**Oracle R02 (tự tính từ specification, chưa test implementation):**

| Chỉ số | Raw | Sau clean |
|---|---:|---:|
| Row count | 12 | 10 |
| Exact duplicates | 2 | 0 |
| Missing cells | 2 | 0 |
| Mean điểm | 85/11 ≈ 7.7272727 | 78/10 = 7.8 |
| Median fill giờ học | — | 4 |
| Median fill điểm | — | 8 |
| Mean điểm A | — | 8.0 |
| Mean điểm B | — | 7.6 |
| Số điểm >=8 | — | 6 |

Ứng dụng/hàm tính dùng dataset này làm nguồn tham chiếu duy nhất khi quay video/báo cáo; 5-row fixture cũ chỉ dùng inline test nếu cần. R04/R05 tiếp tục độc lập xác minh số liệu, không sao chép ngầm các oracle chưa được kiểm tra.

## D. Giai đoạn implementation — chưa kích hoạt

| Bước | Việc | Gate |
|---|---|---|
| P0 | Khi được giao: khóa spec, requirements, tạo CSV giả lập từ PROJECT_SPEC và môi trường | Dữ liệu chuẩn có nguồn, chạy import module |
| P1 | Code logic read/clean/stats Pandas + NumPy | Test oracle + error cases |
| P2 | Code 3 Matplotlib figures | Chart theo đúng nguồn/nhãn |
| P3 | Streamlit một trang, upload, preview/toggle, charts, export | Full demo end-to-end |
| P4 | Test, README thực thi, quay YouTube, PDF 15–20 trang <=100MB, tự chấm, kiểm quyền xem links | Gates G-APP..G-SUBMIT |

## E. Tiêu chí nghiệm thu R02
- [x] Rà soát tất cả file và trạng thái repo/PR.
- [x] Đối chiếu ngược với thang tự đánh giá của thầy.
- [x] So sánh ít nhất bốn cách triển khai và lý do chọn UI 1 trang.
- [x] Giới hạn rõ CORE/OUT và tính năng báo cáo trong app ≠ PDF nộp.
- [x] Dataset 4 cột, trường hợp missing/duplicate, các phép tính oracle số học cụ thể.
- [x] Nêu rõ rủi ro median fill, all-NaN, st rerun và khả năng trình bày.
- [x] Ghi source docs chính thức, không bịa yêu cầu hay kết quả chạy code.
- [x] Ghi R03 là nhiệm vụ kế tiếp duy nhất.

**Gate để thông báo project đã xong sẽ hoàn toàn khác với gate nghiên cứu.** Không đánh dấu checklist implementation là pass ở lượt R02.


## F. Kết quả R03 / checklist kiểm định trước khi bàn giao R04
- [x] So sánh một file, ba file, nhiều lớp; chọn đúng ba file Python.
- [x] Xác định một chiều import, 5 hàm analysis, 3 hàm chart có input/output cụ thể.
- [x] Thiết kế 1 file CSV, ưu tiên upload có sẵn nếu có, checkbox làm sạch từ raw và không cần session state tự viết.
- [x] Mô tả 3 selectbox tối đa để histogram, bar, scatter chia sẻ cột thay vì 6+ tùy chọn.
- [x] Chọn Matplotlib Figure tường minh thay global pyplot; phân loại các lựa chọn chưa xác minh.
- [x] Dẫn tài liệu chính thức, **không có implementation/tests**.
- [x] Ghi bước kế tiếp duy nhất: R04 – toán, NaN, statistics, correctness.


## H. R04 verified mathematical baseline
- [x] Recalculate canonical 12→10 dataset, raw/clean stats and groups.
- [x] Choose population std ddof=0 = sqrt(1.56), sample std comparison only.
- [x] Define numeric all-NA, one valid value, non-finite infinity policy.
- [x] Document group missing names, generated duplicates after median fill and non-idempotence.
- [x] Specify histogram five bins, group means bar axis baseline zero, paired scatter semantics.
- [x] Deliver oracle cases **OR-01 through OR-15** in PROJECT_SPEC §11.
- [x] Record independent temporary numerical validation but **no app tests/code**.
- [x] Next only **R05 QA / testing / versions**.


## I. R05 — QA/environment design review checklist (2026-10-25)
- [x] Read all 8 repository files and confirmed docs branch PR#1 remains open.
- [x] Recommended CPython 3.13 and checked releases/PyPI; did NOT declare untested exact package combo "working".
- [x] R05 spec §12 documents candidate dependency bounds, venv commands for Windows and macOS/Linux, pip check, exact-pins-after-smoke policy.
- [x] OR-01..OR-15 converted into test method/expected assertions with priority; added IO-01..10 + UI-01..06, without test code.
- [x] Identified Pandas 3.0 new default str dtype (regression for `lop`), Streamlit explicit Figure requirement, file_uploader 200MB default vs 2MiB project cap, and potential download rerun.
- [x] Designed fail-fast for empty/malformed/invalid-UTF8/oversize CSV and +/-infinity without sophisticated validation framework.
- [x] Defined smoke/manual tests and acceptance gates before YouTube/report; no fake pass claims.
- [x] Chose R06 (report/video/evidence plan) as sole next task. R05 did not create .py / .csv / requirements or run application.


## K. R06 — hồ sơ nộp và minh chứng (DONE 2026-10-25)
- [x] PDF **18 trang vật lý dự kiến**, tính bìa/mục lục; phù hợp giới hạn 15–20, ≤100MB, không lấp bằng source code.
- [x] YouTube demo storyboard ~7 phút (khuyến nghị, chưa có thời lượng bắt buộc).
- [x] EV-01..EV-16 liên kết cùng Git SHA, phiên bản thư viện/dataset, ảnh và code/test đúng sự thật.
- [x] Tự đánh giá 5 mục **3+2+2+1+2**, chưa gán điểm trước khi làm app.
- [x] Kiểm link GitHub private/YouTube visibility, chất lượng HD, PDF trang/kích thước/Unicode/hình/bảng.
- [x] Toàn bộ hướng dẫn chi tiết ở **docs/DELIVERABLES.md**; chỉ research, không tạo code/report/video.
- [x] Nhiệm vụ duy nhất tiếp theo R07, sau đó FINAL; P0–P4 bị BLOCKED.

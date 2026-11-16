# PLAN — DataForge Mini · R01–R07 + FINAL PASS · PLAN READY

**CHỈ TÀI LIỆU**. Đây là kế hoạch có thể giao cho AI sau khi nghiên cứu hoàn tất. **Không khởi chạy các task coding bên dưới trước khi FINAL ghi READY FOR IMPLEMENTATION VÀ chủ dự án yêu cầu bắt đầu.**

## 1. Tổng quan nghiên cứu 7 + 1

| Lượt | Vai trò | Trạng thái | Nguồn chi tiết |
|---|---|---|---|
| R01 | Xác minh yêu cầu và thang điểm | DONE | `docs/REQUIREMENTS.md` |
| R02 | Chọn MVP + dataset | DONE | `PROJECT_SPEC.md` |
| R03 | Kiến trúc 3 file + 8 hợp đồng hàm | DONE | `PROJECT_SPEC.md` |
| R04 | Kiểm chứng số và edge cases | DONE | `PROJECT_SPEC.md` |
| R05 | Thiết kế test/env/IO | DONE | `PROJECT_SPEC.md` |
| R06 | PDF/video/self-eval/evidence | DONE | `docs/DELIVERABLES.md` |
| R07 | Rulebook, AI bootstrap, task packets | **DONE** | `AGENTS.md`, `RULEBOOK.md`, file này |
| **FINAL** | **Kiểm định chéo độc lập**, sửa mâu thuẫn cuối và quyết định READY/BLOCKED | **PASS — READY (PLAN ONLY)** | `docs/STATUS_HANDOFF.md` |

### FINAL independent QA gate — PASS, 2026-10-25
- [x] Tại FINAL, đọc 9 file và ghi nhận tài liệu **chưa nằm trên `main`**. **Sau FINAL đã merge PR #1 vào `main`**; đây là bước phân phối tài liệu, không phải coding.
- [x] FORM-CONFIRMED F02–F06 đối chiếu với PDF/video/GitHub/tự chấm.
- [x] Cấu trúc 3 file và 8 hợp đồng hàm nhất quán, không có logic test khống.
- [x] Oracle sample 12→10, median 4/8, mean 7.8, ddof0 std≈1.249, group means A8/B7.6, histogram đúng.
- [x] 15 OR + 10 IO + 6 UI được thiết kế đủ, không bắt phải viết 31 test functions.
- [x] Chuỗi task P0–P4 có thứ tự, outputs, cổng bằng chứng, chỉ một next task.
- [x] Hướng dẫn mở PR, cập nhật status, cấm code trong FINAL đúng rõ ràng.
- [x] Link tài liệu và Markdown được kiểm tra, không có file/claim giả.
- [x] Đã xem xét cách đưa tài liệu lên nhánh mặc định. Sau khi chủ dự án đồng ý, **PR #1 đã được merge vào `main`**, nên AI mới đọc trực tiếp nhánh mặc định.
- [x] Lưu bản kiểm định FINAL trong STATUS_HANDOFF/commit, đặt **READY FOR IMPLEMENTATION** chỉ nếu thực sự đạt. **Chưa được phép code dù READY** cho tới khi owner ra lệnh.

## 2. Lộ trình triển khai tinh gọn: 5 bước (được chủ dự án phê duyệt 2026-11-16)

Theo yêu cầu tối giản hóa của chủ dự án (`AGENTS.md` §0 mục 5: yêu cầu mới nhất của chủ dự án > PLAN cũ), 10 task chi tiết `T01–T10` được gộp thành **5 bước thực thi (`S01–S05`)** mà vẫn giữ nguyên 100% hợp đồng hàm, bài kiểm thử `OR/IO/UI` và bằng chứng `EV-01..16`.

| Bước | Gộp từ | Trạng thái | File / đầu ra | Cổng nghiệm thu |
|---|---|---|---|---|
| **S01** | T01 | **DONE** (`011320c`) | `.venv/`, `requirements.txt`, `README.md`, `docs/STATUS_HANDOFF.md` | Python 3.13.16, `pip check` PASS, smoke import PASS |
| **S02** | T02 + T03 + T04 + T05 | **DONE** (`ee9ccba`) | `sample_data.csv`, `analysis.py`, `tests/test_analysis.py` | 12×4 chuẩn + 5 hàm `analysis.py` + `pytest` PASS `OR-01..06, 09..13, 15` & `IO-01..10` |
| **S03** | T06 + T07 + T08 | **DONE** (`1911d34`) | `charts.py`, `app.py`, `tests/test_analysis.py` | 3 Figure (`OR-07/08/11/14`), UI Streamlit 1 trang, bắt lỗi ≤2 MiB, export CSV (`10 passed`) |
| **S04** | T09 | **DONE** (hiện tại) | `tests/test_analysis.py`, `README.md`, `docs/STATUS_HANDOFF.md` | `pytest` 11/11 PASS (`OR/IO/UI-01..06`), `pip check` PASS, đóng băng baseline SHA & thu `EV-01..13` |
| **S05** | T10 | **NEXT** | PDF 15–20 trang ≤100 MB, YouTube demo, tự chấm F06 | Kiểm đủ `EV-14..16`, link người chấm mở được, không tự gửi form |

### Bảng đối chiếu 10 task gốc (tham chiếu chi tiết từng gate)

Các task `T01–T10` dưới đây là bản phân rã gốc dùng để đối chiếu chi tiết các tiêu chí trong `PROJECT_SPEC.md`:

| Mã | Giai đoạn / task | File/đầu ra cho phép | Gate nghiệm thu — bằng chứng phải có |
|---|---|---|---|
| **T01** | **P0** — khởi tạo venv Python 3.13, chọn và cài bốn thư viện, chốt version sau smoke | `requirements.txt`, README hướng dẫn chạy | Fresh venv, `pip check`, import libs, ghi versions/OS thật; không tuyên bố release combo tương thích chỉ dựa PyPI |
| **T02** | **P0** — tạo duy nhất dataset tổng hợp | `sample_data.csv` | Khớp chính xác **12 bản ghi, 4 cột, 2 dòng trùng, 2 ô trống** theo PROJECT_SPEC §2 (kiểm trực tiếp văn bản/CSV bằng cách đơn giản); **OR-01 đầy đủ chỉ thực hiện ở T03 sau khi có loader/profile** |
| **T03** | **P1** — loader và mô tả dữ liệu | `analysis.py`, `tests/test_analysis.py` | `load_csv` + `inspect_data`; **OR-01** và loader-side IO-01..07; nêu rõ exceptions hợp lệ. **Thông báo lỗi bằng Streamlit để kiểm ở T08**, không yêu cầu UI trước T07 |
| **T04** | **P1** — thao tác làm sạch minh bạch | `analysis.py`, test | `clean_data`: 12→10, fill 4/8, raw không đổi; OR-02/03/09/12/13/15; điền median **sau** drop duplicates |
| **T05** | **P1** — thống kê NumPy/Pandas | `analysis.py`, test | `numeric_stats`/`mean_by_group`; OR-04/05/06/10/11; count0=None, std ddof0, dtype string Pandas3 |
| **T06** | **P2** — ba Matplotlib Figure | `charts.py`, tests khi cần | `histogram`/`group_bar`/`scatter` trả Figure, labels và counts đúng OR-07/08/11/14; không dùng pyplot global |
| **T07** | **P3** — Streamlit một trang và chuyển trạng thái raw/clean | `app.py` | sample fallback, uploader, preview, toggle, numeric & category selects, Figure, download; UI-01..06; không custom session state |
| **T08** | **P3/P4** — xử lý lỗi tích hợp và kiểm xuất CSV | `app.py`, sửa **có phạm vi** trong analysis/charts/tests | IO-01..10, UI-01..06, upload ≤2MiB, valid input không crash, export từ active_df, không extra index |
| **T09** | **P4** — QA, tài liệu chạy và đóng băng release | README, tests, sửa lỗi source có bằng chứng, STATUS | Exact test command + pass/fail, pip check, GUI smoke, **mã nguồn trên Git đúng release branch**, chốt **code/data baseline SHA** và thu EV-01..13; quyền xem repo của giảng viên kiểm cuối ở T10 |
| **T10** | **P4** — sản phẩm nộp bài | PDF/video/evidence **sản xuất ngoài app**, cập nhật link README/STATUS khi có thật | PDF 15–20 pages ≤100MB render QA, YouTube **và GitHub source URL** người chấm xem được (EV-14..16), tự chấm 3+2+2+1+2; không tự gửi form |

**Không cần một nhánh cho từng hàm nhỏ** nếu làm trên một nhánh implementation theo một PR; nhưng mỗi task phải có commit có thể kiểm tra và STATUS được cập nhật. Nếu nhiều AI làm song song, tạo branches/PR riêng và owner review trước khi merge; tránh cập nhật đồng thời chung file.

## 3. Hướng dẫn đóng task: Definition of Done
Một task chỉ DONE khi:
1. File đúng phạm vi tồn tại trên branch/commit.
2. Chức năng đáp ứng **các input/output/hành vi của PROJECT_SPEC**.
3. Test/GUI smoke áp dụng đã **thực sự chạy**; có command, results, OS/Python/libs/commit. Không bỏ qua lỗi rồi tự báo đạt.
4. Chức năng được giải thích bằng lời đơn giản, không xuất hiện dependency/tầng không cần thiết.
5. STATUS_HANDOFF cập nhật task, changed files, SHA, failed/skipped tests và **next single task**.
6. Với P4 phải thêm verification PDF/video/link/self-eval từ DELIVERABLES, không chấm khi chưa có sản phẩm.

### Nếu kẹt
- Chỉ sửa lỗi đúng task, bảo toàn scope.
- Đánh dấu **BLOCKED** với lệnh lỗi, nguyên nhân chứng minh được, cách xử lý đề xuất; không tuyên bố DONE.
- Nếu cần thiết kế khác PROJECT_SPEC/RULEBOOK hoặc mở scope, cần chủ dự án đồng ý.

## 4. Mẫu prompt giao task khi implementation được mở (không kích hoạt sớm)

> Đọc và xác minh AGENTS.md, RULEBOOK.md, STATUS_HANDOFF.md, REQUIREMENTS.md, PROJECT_SPEC.md, PLAN.md, DELIVERABLES.md trên GitHub. Chỉ khi FINAL=READY và chủ dự án đã giao coding, thực hiện **T[xx]**. Không đổi các task khác, không thêm công nghệ. Chạy test theo gate của T[xx], ghi output/commit, cập nhật STATUS_HANDOFF. Nếu vướng cổng quyền hoặc test fail, báo BLOCKED với bằng chứng.

## 5. Phạm vi bị loại khỏi roadmap
Machine learning, clone/nhúng Data-Forge gốc, dashboard đa trang, Excel, database, cloud, AI agent, REST/API, custom frontend, tài khoản, hệ thống report PDF bên trong ứng dụng, undo history, chart builder, 10+ biểu đồ, CI/Docker/browser automation. **Tránh task về các phần trên** trừ khi giảng viên có chỉ dẫn mới có bằng chứng và chủ dự án phê duyệt.

## 6. FINAL audit — PASS (2026-10-25)
- READY FOR IMPLEMENTATION áp dụng **cho hồ sơ tài liệu**, chưa có lệnh coding và không có app/test chạy.
- Đã đọc 9 file; đối chiếu yêu cầu F01–F06; 7 M, 8 hàm, 15 OR/10 IO/6 UI, 10 T, 16 EV và PDF dự kiến 18 trang. Nguồn ảnh form là bản trích xuất R01, chưa có bản gốc trong repo.
- Kiểm lại độc lập dataset 12→10, median4/8, mean7.8, variance1.56, std≈1.249, A8/B7.6, hist [2,2,3,2,1], và edge case fill tạo duplicate bằng pandas/NumPy tạm (KHÔNG phải app runtime).
- Đã sửa tham chiếu PROJECT_SPEC trong DELIVERABLES, T02/T03 acceptance dependency, dtype pandas, header trùng, tách SHA baseline code+dataset khỏi update docs.
- Cả 9 file/Markdown/links đã kiểm. **Cập nhật sau FINAL:** PR #1 đã merge vào `main`, tiếp quản từ nhánh mặc định thay vì PR cũ.
- **Next: chờ chủ dự án giao lệnh coding T01.** Việc merge PR #1 chỉ công bố bộ tài liệu, không tự mở khóa triển khai.

## 7. Handoff sau merge (chỉ tài liệu)
- PR #1 đã merge; commit merge: `c3d979c20a8a49493139d195130713097ae77b83`.
- Các hướng dẫn hiện hành có trên `main`; AI tiếp quản đọc `AGENTS.md`, `RULEBOOK.md`, `docs/STATUS_HANDOFF.md` trước khi đọc spec và tasks.
- **T01–T10 chưa thực hiện**. Mỗi task yêu cầu bằng chứng chạy thực tế theo bảng tại §2; không tạo app trong pha chuẩn bị.

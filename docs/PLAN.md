# PLAN — DataForge Mini · R07 complete, FINAL NEXT

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
| **FINAL** | **Kiểm định chéo độc lập**, sửa mâu thuẫn cuối và quyết định READY/BLOCKED | **NEXT, NOT STARTED** | `docs/STATUS_HANDOFF.md` |

### FINAL independent QA gate
- [ ] Đọc 9 file, xác minh HEAD/PR, không có source app.
- [ ] FORM-CONFIRMED F02–F06 đối chiếu với PDF/video/GitHub/tự chấm.
- [ ] Cấu trúc 3 file và 8 hợp đồng hàm nhất quán, không có logic test khống.
- [ ] Oracle sample 12→10, median 4/8, mean 7.8, ddof0 std≈1.249, group means A8/B7.6, histogram đúng.
- [ ] 15 OR + 10 IO + 6 UI được thiết kế đủ, không bắt phải viết 31 test functions.
- [ ] Chuỗi task P0–P4 có thứ tự, outputs, cổng bằng chứng, chỉ một next task.
- [ ] Hướng dẫn mở PR, cập nhật status, cấm code trong FINAL đúng rõ ràng.
- [ ] Link tài liệu và Markdown được kiểm tra, không có file/claim giả.
- [ ] Lưu bản kiểm định FINAL trong STATUS_HANDOFF/commit, đặt **READY FOR IMPLEMENTATION** chỉ nếu thực sự đạt. **Chưa được phép code dù READY** cho tới khi owner ra lệnh.

## 2. Future implementation: 5 giai đoạn, 10 task nhỏ

**Mỗi task** có file được phép sửa và test nghiệm thu. Các task này là **lệnh mẫu sau khi được phê duyệt**, không phải nhiệm vụ đang chạy.

| Mã | Giai đoạn / task | File/đầu ra cho phép | Gate nghiệm thu — bằng chứng phải có |
|---|---|---|---|
| **T01** | **P0** — khởi tạo venv Python 3.13, chọn và cài bốn thư viện, chốt version sau smoke | `requirements.txt`, README hướng dẫn chạy | Fresh venv, `pip check`, import libs, ghi versions/OS thật; không tuyên bố release combo tương thích chỉ dựa PyPI |
| **T02** | **P0** — tạo duy nhất dataset tổng hợp | `sample_data.csv` | Khớp **chính xác** 12 dòng/4 cột trong PROJECT_SPEC; raw missing2/duplicates2; OR-01 |
| **T03** | **P1** — loader và mô tả dữ liệu | `analysis.py`, `tests/test_analysis.py` | `load_csv` + `inspect_data`; OR-01, IO-01..07 (các lỗi liên quan); không mutate, có lỗi rõ |
| **T04** | **P1** — thao tác làm sạch minh bạch | `analysis.py`, test | `clean_data`: 12→10, fill 4/8, raw không đổi; OR-02/03/09/12/13/15; điền median **sau** drop duplicates |
| **T05** | **P1** — thống kê NumPy/Pandas | `analysis.py`, test | `numeric_stats`/`mean_by_group`; OR-04/05/06/10/11; count0=None, std ddof0, dtype string Pandas3 |
| **T06** | **P2** — ba Matplotlib Figure | `charts.py`, tests khi cần | `histogram`/`group_bar`/`scatter` trả Figure, labels và counts đúng OR-07/08/11/14; không dùng pyplot global |
| **T07** | **P3** — Streamlit một trang và chuyển trạng thái raw/clean | `app.py` | sample fallback, uploader, preview, toggle, numeric & category selects, Figure, download; UI-01..06; không custom session state |
| **T08** | **P3/P4** — xử lý lỗi tích hợp và kiểm xuất CSV | `app.py`, sửa **có phạm vi** trong analysis/charts/tests | IO-01..10, UI-01..06, upload ≤2MiB, valid input không crash, export từ active_df, không extra index |
| **T09** | **P4** — QA, tài liệu chạy và đóng băng release | README, tests, sửa lỗi source có bằng chứng, STATUS | Exact test command + pass/fail, pip check, GUI smoke, F03 link access, commit SHA freeze và thu EV-01..13; không claim pass khi chưa chạy |
| **T10** | **P4** — sản phẩm nộp bài | PDF/video/evidence **sản xuất ngoài app**, cập nhật link README/STATUS khi có thật | PDF 15–20 pages ≤100MB render QA, video YouTube truy cập được, EV-14..16, tự chấm 3+2+2+1+2; không tự gửi form |

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

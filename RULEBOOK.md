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
13. **Đồng bộ bài nộp:** video YouTube và báo cáo PDF 15–20 trang <=100 MB **bắt buộc theo form**, cùng với link code và đoạn tự đánh giá. Nội dung chỉ giới thiệu tính năng đã chạy; biểu đồ và số liệu khớp dataset/commit demo. PPT chưa xác minh là bắt buộc.
14. **Bằng chứng & điều chưa biết:** form đã xác nhận chủ đề 5.5, code link, YouTube link, PDF 15–20 trang, giới hạn 100 MB, điểm **tự đánh giá 3+2+2+1+2**. Không suy diễn deadline, thời lượng video, slide, định dạng chi tiết hay rubric chấm cuối. Tách `FORM-CONFIRMED`, `USER-DECIDED`, `DESIGN-PROPOSED`, `UNKNOWN` như `docs/REQUIREMENTS.md`.
15. **Definition of Done:** khi được phép coding mới yêu cầu code chạy được, test logic đạt, demo được, giải thích được từng hàm/thư viện; không coi kế hoạch là sản phẩm.
16. **Research-only gate:** 7 lượt nghiên cứu và 1 lượt QA cuối được làm tuần tự. **Cấm khởi tạo source code, dependencies, dataset thực tế hoặc nộp sản phẩm trước khi owner giao lập trình.**
17. **Bảo mật & nộp bài:** repo đang private; kiểm tra quyền truy cập người chấm trước khi gửi, không tự chuyển public. YouTube link phải xem được bởi người chấm; thử qua phiên không đăng nhập.


## Quy tắc kiến trúc bổ sung từ Research 03 (ưu tiên kỹ thuật; chưa code)
- Với MVP, **giới hạn 3 file Python ứng dụng**: `app.py` (UI), `analysis.py` (Pandas/NumPy), `charts.py` (Matplotlib). Test được tách riêng. Muốn thêm file ứng dụng phải giải thích được phần phức tạp bị loại bỏ và được owner đồng ý.
- `analysis.py` không import Streamlit/Matplotlib; `charts.py` không import Streamlit hoặc đọc file; `app.py` không nhân đôi logic cleaning/stats.
- **Không cần `st.session_state` tùy biến, cache, callback, class, Undo/Redo** cho phiên bản mẫu 12 dòng. Các lựa chọn được tính lại từ raw khi widget đổi.
- Chart tạo **Figure tường minh** và trả về; Streamlit nhận Figure; không sử dụng global `plt.show()`, `plt.gcf()` hay charting library khác.
- Đặc tả hợp đồng hàm tại `PROJECT_SPEC.md §10`. **R04–R05 được quyền sửa chi tiết toán/test để đảm bảo đúng**, không tự mở rộng tính năng.


## R04 numerical safeguards
- Descriptive **population std** uses explicit `ddof=0`. Never silently mix it with Pandas default `ddof=1`.
- If numeric column has 0 valid values, return count0 and other stats None, not NaN or zero. One valid value has population std0.
- Keep raw unchanged; drop whole-row duplicates once, **then** fill numeric NA by column median. Median fill can create duplicates; do not run another automatic dedup pass.
- Categorical NA is not filled; missing GroupBy keys are excluded and must be described. A missing group mean is not 0.
- Numeric infinity is unsupported; report rather than plotting/computing it. NA for the demo remains allowed.
- Histogram 5 equal-width bins, `density=False`, bar mean begins Y at 0, scatter drops NA as **row pairs**; no causal claims.
- Numerical comparisons in tests use tolerances; rounding only in UI. See PROJECT_SPEC `11 for OR-01..OR-15.


## R05 QA and reproducibility rules
- Runtime target **CPython 3.13**; verify exact top-level dependency versions on owner's actual computer at P0, **then pin what passed**. Never present PyPI classifiers as proof a full environment is functional.
- Pandas ≥3 string columns may be `str` rather than `object`; group selection must recognize both, including `lop`.
- One canonical CSV file only; in-memory CSV test inputs allowed. No elaborate mock fixtures, browsers, Docker, CI, Selenium or frontend testing framework unless a concrete blocker requires them.
- Use `pytest.approx` for floating results; inspect Matplotlib Figure attributes rather than image pixels; manual browser smoke for Streamlit.
- On invalid bytes, empty/broken UTF-8 CSV, unsupported columns or ±infinity, show clear message; never silently discard errors.
- **Upload <=2 MiB** for small-data classroom MVP. This is independent from **teacher PDF upload <=100MB**.
- Before "DONE": venv fresh install + pip check + test outputs + chart/UI smoke + source/video/PDF agreement. OR-/IO-/UI- IDs in PROJECT_SPEC `12 are **plans until executed**.


## R06 deliverable controls
- **PDF 15–20 pages ≤100MB is an academic report**, not an app PDF-export feature.
- Target 18 physical pages and a ~7-min video are design preferences, not additional instructor rules; detailed plan at `docs/DELIVERABLES.md`.
- All real screenshots, numeric claims, pytest output, charts, PDF and YouTube must match one final source SHA, dataset and environment; EV-* IDs are plans until captured.
- Never self-score 10/10 by default; fill 3+2+2+1+2 only after app actually passes QA; show true strengths and limitations.
- Do not add features to fill pages. Preserve private data, do not auto-publicize repo or upload video.
- Before submission inspect full PDF render, physical page count, size, glyphs, captions and links; validate YouTube and GitHub viewing permissions.

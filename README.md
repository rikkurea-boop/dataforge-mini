# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Bài học:** Chương 5.5 — NumPy, Pandas, Matplotlib.  
**Mục tiêu:** một ứng dụng nhỏ, đúng trọng tâm, dễ demo; sinh viên giải thích được **toàn bộ code**.

**Trạng thái:** **R01–R07 + FINAL đã PASS — READY FOR IMPLEMENTATION (chỉ kế hoạch)**. Bộ tài liệu đã được hợp nhất vào **`main` qua PR #1**. **Chưa có ứng dụng Python, CSV mẫu thực, test thực thi, PDF hay video**. Chỉ bắt đầu viết code khi chủ dự án có lệnh triển khai mới.

## Bắt đầu / AI tiếp quản

1. [AGENTS.md](AGENTS.md) — làm gì ngay khi tiếp quản, cổng quyền.
2. [RULEBOOK.md](RULEBOOK.md) — quy tắc không được vi phạm.
3. [docs/STATUS_HANDOFF.md](docs/STATUS_HANDOFF.md) — trạng thái mới nhất, nhiệm vụ duy nhất tiếp theo.
4. [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) — yêu cầu giảng viên có bằng chứng.
5. [PROJECT_SPEC.md](PROJECT_SPEC.md) — MVP, dữ liệu, hợp đồng hàm, oracle và test.
6. [docs/PLAN.md](docs/PLAN.md) — roadmap và các task giao lập trình sau khi được phép.
7. [docs/DELIVERABLES.md](docs/DELIVERABLES.md) — báo cáo PDF, video, tự chấm, minh chứng.

**Nguồn sự thật hiện tại:** nhánh mặc định **`main`**. Đọc `AGENTS.md`, `docs/STATUS_HANDOFF.md` và các tài liệu tại đây; PR #1 đã merge và lưu lịch sử R01–R07/FINAL. Khi có nhánh triển khai mới, đọc trạng thái và các thay đổi mới nhất trước khi thao tác. Không coi thiết kế/test case là ứng dụng đã chạy.

## Cấu trúc code tối thiểu được lên kế hoạch — CHƯA TẠO

~~~text
app.py                 # UI Streamlit một trang
analysis.py            # Pandas + NumPy
charts.py              # Matplotlib Figure
sample_data.csv        # một bộ dữ liệu tổng hợp
requirements.txt       # phiên bản chỉ chốt sau smoke test
tests/test_analysis.py # test tập trung, cho phép tách charts khi có lý do
~~~

Tài liệu quản lý hiện nằm ngay root và trong `docs/`. **Không thêm `src/`, `services/`, CI/Docker, database hoặc các hệ thống phức tạp.**

## DataForge gốc

[Data-Forge](https://github.com/rikkurea-boop/Data-Forge) là dự án xử lý dữ liệu huấn luyện AI độc lập. **Không import, sửa hoặc phụ thuộc vào Data-Forge gốc** để hoàn thành bài tập này.

## Bắt đầu triển khai trong tương lai

Khi chủ dự án **chủ động giao việc**, AI đầu tiên thực hiện **T01** trong [docs/PLAN.md](docs/PLAN.md), tiếp tục từng task T02–T10 với kiểm thử/commit/handoff đầy đủ. Không tự tạo framework bổ sung, không cần hỏi thiết kế lại từ đầu. **Hiện trạng: T01 chưa bắt đầu.**

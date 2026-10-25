# DataForge Mini

**Đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Bài học:** Chương 5.5 — NumPy, Pandas, Matplotlib.  
**Mục tiêu:** một ứng dụng nhỏ, đúng trọng tâm, dễ demo; sinh viên giải thích được **toàn bộ code**.

**Trạng thái:** R01–R07 đã hoàn thành **nghiên cứu/tài liệu**; **FINAL CROSS-QA CHƯA THỰC HIỆN**. Chưa có ứng dụng Python, file CSV mẫu, test thực thi, PDF hay video. **Không bắt đầu viết code** cho đến khi FINAL cho phép READY FOR IMPLEMENTATION **và** chủ dự án giao lệnh triển khai.

## Bắt đầu / AI tiếp quản

1. [AGENTS.md](AGENTS.md) — làm gì ngay khi tiếp quản, cổng quyền.
2. [RULEBOOK.md](RULEBOOK.md) — quy tắc không được vi phạm.
3. [docs/STATUS_HANDOFF.md](docs/STATUS_HANDOFF.md) — trạng thái mới nhất, nhiệm vụ duy nhất tiếp theo.
4. [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) — yêu cầu giảng viên có bằng chứng.
5. [PROJECT_SPEC.md](PROJECT_SPEC.md) — MVP, dữ liệu, hợp đồng hàm, oracle và test.
6. [docs/PLAN.md](docs/PLAN.md) — roadmap và các task giao lập trình sau khi được phép.
7. [docs/DELIVERABLES.md](docs/DELIVERABLES.md) — báo cáo PDF, video, tự chấm, minh chứng.

**Nguồn sự thật:** đọc đúng nhánh/PR hiện hành, không lấy `main` đang chưa merge làm bản đầy đủ. Lịch sử các phiên R01–R06 có trong git commits của PR #1. Không được báo code/test đã xong khi mới chỉ có tài liệu.

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

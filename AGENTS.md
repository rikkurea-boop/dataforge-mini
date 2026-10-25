# AGENTS.md – Quy trình tiếp quản cho mọi AI

## Bắt buộc trước khi sửa
1. Đọc `README.md`, `RULEBOOK.md`, `PROJECT_SPEC.md`, `docs/REQUIREMENTS.md`, `docs/PLAN.md`, `docs/STATUS_HANDOFF.md`.
2. Kiểm tra branch, tree, commit/PR, code và các test **thực sự tồn tại**.
3. Nêu ngắn gọn: đã xác minh gì, việc ưu tiên kế tiếp là gì, rủi ro nào chưa rõ.
4. Đọc **cổng giai đoạn** trong `docs/STATUS_HANDOFF.md`. Khi đang R01–R07/FINAL, chỉ nghiên cứu, sửa tài liệu và kiểm chứng nguồn; **không tạo code ứng dụng, dependency, dataset hay slide/video/PDF**.
5. Khi owner cho phép triển khai P0–P4, mới làm từng lát cắt chức năng nhỏ, chạy thử và ghi kết quả. Không tự mở rộng phạm vi.

## Nguyên tắc thuyết trình
User phải hiểu và giải thích **toàn bộ** code, nên số lượng file, thư viện, hàm, trừu tượng phải có lý do trực tiếp. Chỉ dùng NumPy, Pandas, Matplotlib và Streamlit (UI); pytest phục vụ test. Không thêm công nghệ khác nếu không thiết yếu. Tránh module nhiều tầng và code máy sinh khó giải thích.

## Workflow bắt buộc
- Lấy **lượt hiện hành** từ `docs/STATUS_HANDOFF.md`, đối chiếu kế hoạch `docs/PLAN.md`. Không lấy P0/P1 nếu nghiên cứu chưa hoàn thành và chưa có lệnh từ user.
- Làm trên branch; tạo PR; không ghi đè code của AI khác.
- Ở giai đoạn nghiên cứu: viết **đặc tả test, expected values** nhưng không chạy hoặc tạo app. Sau khi được phép coding: viết test cho logic số, dùng dataset nhỏ có đáp án đúng.
- Cập nhật `docs/STATUS_HANDOFF.md` với commit/PR, changed files, test command, kết quả thật và next step.
- Những yêu cầu có bằng chứng nằm trong `docs/REQUIREMENTS.md`: link GitHub, link YouTube, báo cáo PDF **15–20 trang, <=100 MB**, tự đánh giá 5 tiêu chí. Deadline, thời lượng video, PPT và chi tiết khác không thấy trên ảnh thì ghi `UNKNOWN`.

## Hệ ưu tiên
Đề bài chính thức của thầy (đã kiểm chứng) > yêu cầu mới nhất của user > RULEBOOK > PROJECT_SPEC > PLAN > gợi ý từ AI trước đó.

## Không được
Không sửa repo Data-Forge gốc; không xây AI/ML model hay architecture pipeline/cache; không dùng Altair/Plotly thay Matplotlib; không tự nhận ứng dụng/test/video đã hoàn tất; không thêm tính năng để gây ấn tượng nhưng không thuộc đề bài.

## Cổng quyền bắt đầu code
**KHÔNG CODE cho đến khi cả R01–R07 và FINAL kiểm định hoàn thành, kế hoạch được đánh dấu READY FOR IMPLEMENTATION, và user chủ động giao bắt đầu.** Một AI đến repo mà không thấy lệnh mới chỉ được tiếp tục lượt research hiện hành hoặc review chứng cứ. Không tự merge PR, đổi repo private thành public hay đánh dấu sản phẩm đã nộp.

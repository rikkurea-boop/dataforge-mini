# AGENTS.md – Quy trình tiếp quản cho mọi AI

## Bắt buộc trước khi sửa
1. Đọc `README.md`, `RULEBOOK.md`, `PROJECT_SPEC.md`, `docs/REQUIREMENTS.md`, `docs/PLAN.md`, `docs/STATUS_HANDOFF.md`.
2. Kiểm tra branch, tree, commit/PR, code và các test **thực sự tồn tại**.
3. Nêu ngắn gọn: đã xác minh gì, việc ưu tiên kế tiếp là gì, rủi ro nào chưa rõ.
4. Chỉ làm một lát cắt chức năng nhỏ, chạy thử, ghi kết quả; không tự mở rộng phạm vi.

## Nguyên tắc thuyết trình
User phải hiểu và giải thích **toàn bộ** code, nên số lượng file, thư viện, hàm, trừu tượng phải có lý do trực tiếp. Chỉ dùng NumPy, Pandas, Matplotlib và Streamlit (UI); pytest phục vụ test. Không thêm công nghệ khác nếu không thiết yếu. Tránh module nhiều tầng và code máy sinh khó giải thích.

## Workflow bắt buộc
- Lấy việc từ `docs/PLAN.md`.
- Làm trên branch; tạo PR; không ghi đè code của AI khác.
- Viết test cho logic số; kiểm tra bằng dataset nhỏ có đáp án đúng.
- Cập nhật `docs/STATUS_HANDOFF.md` với commit/PR, changed files, test command, kết quả thật và next step.
- Nếu rubric của thầy chưa có bằng chứng, đánh dấu `CHƯA XÁC MINH`, không bịa.

## Hệ ưu tiên
Đề bài chính thức của thầy (đã kiểm chứng) > yêu cầu mới nhất của user > RULEBOOK > PROJECT_SPEC > PLAN > gợi ý từ AI trước đó.

## Không được
Không sửa repo Data-Forge gốc; không xây AI/ML model hay architecture pipeline/cache; không dùng Altair/Plotly thay Matplotlib; không tự nhận ứng dụng/test/video đã hoàn tất; không thêm tính năng để gây ấn tượng nhưng không thuộc đề bài.

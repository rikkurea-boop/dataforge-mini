# STATUS_HANDOFF — DataForge Mini, 2026-10-25

## Trạng thái có căn cứ
- Repository private: https://github.com/rikkurea-boop/dataforge-mini
- **Branch làm việc:** \`docs/project-charter-ai-handoff\`; **PR #1 đang mở:** https://github.com/rikkurea-boop/dataforge-mini/pull/1
- **main** chỉ có \`README.md\` ban đầu. Các tài liệu chuẩn hiện sống trên nhánh PR #1, **chưa merge main**.
- Repo nhánh nghiên cứu có 8 file: \`README.md\`, \`AGENTS.md\`, \`RULEBOOK.md\`, \`PROJECT_SPEC.md\`, \`docs/REQUIREMENTS.md\`, \`docs/PLAN.md\`, \`docs/STATUS_HANDOFF.md\`, \`.gitignore\`.
- **Chưa có app.py, analysis.py, charts.py, sample_data.csv, requirements.txt, test hoặc video/PDF. Không có runtime/pytest report.**
- Không đổi visibility, không merge tự động, không sửa Data-Forge gốc.

## Tiến độ nghiên cứu (7+1)
| Lượt | Kết quả | Trạng thái |
|---|---|---|
| R01 | Xác minh hai ảnh form; F01–F06, self-assessment 3+2+2+1+2 | DONE |
| R02 | Phân tích & chọn MVP scope; một dataset 12→10, oracle; đánh giá 5 phương án UI; đối chiếu docs API | **DONE — chỉ research** |
| R03 | Code architecture/function signatures/UI state/cách chia file gọn | NEXT |
| R04 | Mathematical correctness, NaN/std, chart validation | NOT STARTED |
| R05 | QA/test plan/dependency/fresh clone | NOT STARTED |
| R06 | PDF 15–20 trang/video YouTube/tự đánh giá | NOT STARTED |
| R07 | AGENTS/RULEBOOK/handoff hoàn thiện | NOT STARTED |
| FINAL | Review mọi research và khóa READY FOR IMPLEMENTATION | NOT STARTED |
| P0–P4 | Viết app, chạy test, báo cáo, video, nộp bài | **BLOCKED — user chưa giao** |

## R02 đã làm gì (không gộp với code)
1. Đọc toàn bộ các file thực tồn tại của nhánh docs và trạng thái PR.
2. Đối chiếu hướng MVP với chính xác yêu cầu thầy: chủ đề NumPy/Pandas/Matplotlib, repo/video/PDF, 5 tiêu chí.
3. Nghiên cứu API tài liệu chính thức Pandas, NumPy, Matplotlib và Streamlit, liên kết đầy đủ trong docs/REQUIREMENTS.md.
4. So sánh Jupyter, CLI, Tkinter, Flask và Streamlit; khuyến nghị Streamlit một trang, không multi-page/frontend riêng.
5. Xây đặc tả **một dataset CSV tổng hợp**, 12 hàng raw, 2 exact duplicates, 2 numeric NaNs, sau cleaning 10 hàng (median 4/8).
6. Tính đối chứng từ đặc tả: mean điểm 7.8; A 8.0; B 7.6; giờ học mean 4.4; >=8 là 6/10.
7. Ghi rõ không làm Excel/ML/PCA/Undo/cloud/database/PDF engine trong app.
8. Chưa tạo file CSV hay code; số liệu oracle **chưa phải kết quả chạy app**.

## Tài liệu quyền lực
\`docs/REQUIREMENTS.md\`: nguồn từ form + trạng thái chứng cứ; \`RULEBOOK.md\` và \`AGENTS.md\`: quy tắc bất biến; \`PROJECT_SPEC.md\`: phạm vi MVP + source CSV + oracle; \`docs/PLAN.md\`: lượt R03 và các bước sau. Không suy diễn nhiệm vụ từ chat cũ hoặc main trống.

## Những vấn đề đã hoãn có chủ đích
- Chọn file layout, function contracts, UI rerun/session state: **R03**.
- Chốt ddof/std, edge cases, quy tắc xử lý all-NaN: **R04**.
- Chọn Python/runtime versions, test matrix: **R05**.
- Báo cáo ngoài app, video, tự chấm và trích dẫn: **R06**.
- Hạn nộp, PPT, thời lượng video: chưa thấy trong phần ảnh form, **UNKNOWN**.
- App cần public repo hay cấp quyền cho thầy: owner sẽ quyết khi nộp.

## Việc tiếp theo duy nhất
**R03 — Thiết kế kiến trúc và function contracts tối giản** theo PROJECT_SPEC hiện hành: cấu trúc 2–3 file Python, cách phân tách UI/data/chart, chart return Figure, cách tránh trạng thái khó giải thích trong Streamlit. Chỉ viết đặc tả tài liệu, **không code**.

## Handoff format cho phiên sau
Date / research session / branch / PR / commit / files changed / nguồn xác minh / rủi ro / thứ chưa làm / next single task.

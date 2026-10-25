# Plan – Research-first, minimal-first

**Trạng thái:** Research 01/07. **Không viết code ứng dụng trong giai đoạn này.** Người dùng sẽ kích hoạt từng lượt riêng; kết thúc R07 còn 1 lượt final QA trước khi được phép triển khai.

## A. Chuẩn bị trước khi code: 7 lượt nghiên cứu + 1 final review

| Lượt | Phạm vi riêng | Đầu ra phải ghi vào repo | Tiêu chí đóng lượt |
|---|---|---|---|
| R01 | Đối chiếu biểu mẫu thầy, phân loại yêu cầu/đề xuất/unknown, điểm tự đánh giá | docs/REQUIREMENTS.md, PROJECT_SPEC.md, STATUS_HANDOFF | Form requirements → artifact → evidence/gate truy vết được |
| R02 | Lựa chọn chức năng MVP tối giản, dataset và luồng demo | PROJECT_SPEC.md + docs/PLAN.md | Chỉ giữ chức năng phục vụ 5.5, dataset có đáp án đối chứng |
| R03 | Thiết kế kiến trúc/code gọn, UI, API/function contract | PROJECT_SPEC.md + RULEBOOK.md | Sinh viên có thể giải thích toàn bộ file và luồng dữ liệu |
| R04 | Kiểm định thuật toán, thống kê, NaN, biểu đồ và các giả định toán | PROJECT_SPEC.md + docs/REQUIREMENTS.md | Công thức chính xác, kết quả fixture đối chiếu |
| R05 | Bộ test, lỗi input, môi trường/cách chạy; phương án demo không lỗi | docs/PLAN.md + RULEBOOK.md | Test cases có input/expected; không khẳng định đã chạy |
| R06 | Thiết kế báo cáo PDF 15–20 trang, video YouTube, tự đánh giá và bằng chứng | docs/DELIVERABLES.md (chỉ tạo khi bắt đầu R06) | Tất cả mục FORM-CONFIRMED có vị trí/đầu ra minh chứng |
| R07 | Quy tắc AI handoff, coding scope, prompt/task và chống overengineering | AGENTS.md, RULEBOOK.md, docs/STATUS_HANDOFF.md | AI mới đọc repo là biết bắt đầu từ đâu và không làm gì |
| FINAL | Rà soát chéo 7 lượt, loại trùng, khóa specification | Các file trên | Đánh dấu READY FOR IMPLEMENTATION chỉ khi đủ chứng cứ |

**Sau mỗi lượt:** 1 commit hoặc PR có bằng chứng, cập nhật STATUS_HANDOFF; không chuyển bước tiếp theo chỉ vì có draft. Không thêm hàng loạt folder nghiên cứu nếu có thể hợp nhất vào file hiện có.

## B. Quy trình triển khai — ĐÃ LÊN KẾ HOẠCH, CHƯA ĐƯỢC KÍCH HOẠT

| Bước | Dự kiến | Bằng chứng hoàn tất cần có |
|---|---|---|
| P0 | Khi user cho phép: xác minh đề, khóa MVP, venv, requirements.txt, sample_data.csv | Repo files tồn tại, dữ liệu mẫu có đáp án |
| P1 | analysis.py: CSV, profile, missing/duplicates, basic stats Pandas/NumPy | Test đối chứng + edge cases pass |
| P2 | charts.py: Matplotlib plots | Figures hợp lệ, labels đầy đủ, chart data chính xác |
| P3 | app.py: Streamlit UI, preview, thao tác clean/stats/chart/download | Demo end-to-end chạy được |
| P4 | QA cuối, README, video YouTube, PDF 15–20 trang, tự đánh giá, nộp form | Gate G-APP/G-CODE/G-VALID/G-REPO/G-VIDEO/G-PDF/G-SELF/G-SUBMIT đạt |

Các chi tiết P0–P4 là dự kiến; khóa lại sau R02–R07. **Không được viện P0 là task tiếp theo để tự bắt đầu code ở giai đoạn research.**

## C. Định hướng dữ liệu đối chứng (đề xuất, R02 sẽ khóa)
```csv
ten,lop,gio_hoc,diem
An,A,4,8
Binh,B,2,6
Chi,A,6,9
Dung,B,3,7
Ha,A,7,10
```
- mean(diem) = 8.0; nhóm A = 9.0; B = 6.5; số điểm >=8 là 3; mean(gio_hoc) = 4.4.
- Fixture lỗi có dòng trùng/NaN **riêng**; không được thay đổi đáp án chuẩn.

## D. Chống phát sinh ngoài phạm vi
Ưu tiên CSV → profile → clean → basic stats → Matplotlib → CSV export. Không mở rộng Excel, database, AI, advanced statistical models, nhiều chart engine, PDF export từ app, auth/cloud. Các quyết định về số biểu đồ/UI còn thuộc R02–R03, không được mô tả là yêu cầu của thầy.

## E. Checklist nộp bài (cho giai đoạn cuối, chưa hoàn thành)
- [ ] Đã có repo code thực tế, link cho người chấm mở được
- [ ] Video YouTube xem được từ tài khoản khác/chưa đăng nhập, nội dung đúng sản phẩm
- [ ] PDF báo cáo đúng 15–20 trang, đúng định dạng, <=100 MB
- [ ] Có đoạn nhận xét/ưu nhược/tự chấm 5 mục theo 3+2+2+1+2
- [ ] Tự điền và xác minh thông tin cá nhân trong form
- [ ] Code/test/biểu đồ/báo cáo/video nhất quán
- [ ] Mọi thông tin UNKNOWN được đối chiếu khi có nguồn mới

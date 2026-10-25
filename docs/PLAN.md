# Plan – Triển khai theo 5 lượt nhỏ

> Chỉ đi từ đơn giản đến vừa đủ; không làm bước tiếp theo nếu bước trước chưa chạy và test được.

| Lượt | Việc cần làm | Điều kiện hoàn thành |
|---|---|---|
| P0 | Kiểm tra đề gốc, khóa MVP, tạo môi trường `requirements.txt`, fixture CSV | Đã xác nhận phạm vi hoặc ghi rõ chỗ chưa xác nhận |
| P1 | `analysis.py`: read CSV, profile, loại trùng, fill NaN trung vị, stats Pandas/NumPy | Pytest các phép tính và edge cases chạy đạt |
| P2 | `charts.py`: 3 biểu đồ Matplotlib dễ hiểu: histogram, bar, scatter | Đúng cột hợp lệ; trả Figure; test không crash |
| P3 | `app.py`: Streamlit UI với upload, preview, clean, stats, charts, download CSV | Demo end-to-end chạy trên dataset mẫu/lỗi |
| P4 | QA, README chạy app, script trình bày code, slide/video/report theo yêu cầu thật | Test pass + checklist demo + sản phẩm thống nhất |

## Thứ tự ưu tiên nếu thiếu thời gian
**Cốt lõi:** CSV → profile → clean → stats → Matplotlib → CSV output. **Bỏ** nhóm nâng cao, chart customization, Excel, PDF report trong app, animation, auth/deploy.

## Tiêu chí PR
Mỗi PR: một chức năng, tập file ngắn; mô tả input/output; giải thích ít nhất một chỗ dùng thư viện học phần; bằng chứng test; cập nhật STATUS_HANDOFF.

## Dataset đối chứng nhỏ
```csv
ten,lop,gio_hoc,diem
An,A,4,8
Binh,B,2,6
Chi,A,6,9
Dung,B,3,7
Ha,A,7,10
```
- Trung bình điểm: 8.0
- Lớp A: 9.0; lớp B: 6.5
- >= 8: 3/5
- Giờ học trung bình: 4.4

Dataset 'dirty' bổ sung NaN và dòng duplicate **riêng**, không làm thay đổi fixture chuẩn.

## Checklist trước khi báo cáo đã xong
- [ ] Đề chính thức đã được đối chiếu hoặc ghi UNKNOWN
- [ ] App chạy được từ fresh clone
- [ ] Pandas, NumPy, Matplotlib đều dùng trong luồng demo thực
- [ ] Dữ liệu gốc không bị mutate
- [ ] Kiểm tra lỗi file rỗng/thiếu số/cột không hợp lệ
- [ ] Pytest pass (kèm lệnh và output thật)
- [ ] Người trình bày hiểu từng file/hàm
- [ ] Các tài liệu nộp khớp với app

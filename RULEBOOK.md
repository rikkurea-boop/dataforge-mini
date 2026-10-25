# RULEBOOK — DataForge Mini (quy tắc đang có hiệu lực)

**Ưu tiên của chủ dự án:** **TỐI GIẢN → ĐÚNG TRỌNG TÂM 5.5 → CHẠY ĐÚNG → TỰ GIẢI THÍCH ĐƯỢC TOÀN BỘ CODE**. Tài liệu lịch sử R01–R06 ở git history, không nhân bản quy tắc theo từng research session.

## A. Phạm vi và kiến trúc (BẮT BUỘC)
1. Dự án **độc lập** với Data-Forge gốc; không import hoặc thay đổi nó.
2. Chức năng đúng `PROJECT_SPEC.md`: CSV sample/upload → kiểm tra → một thao tác clean → thống kê → 3 Matplotlib figures → tải CSV hiện hành. **Không thêm tính năng để gây ấn tượng hoặc kéo dài PDF/video.**
3. Chỉ **3 Python source chính** (app/analysis/charts); tối đa một file test ban đầu; không `src/`, class service, API, frontend riêng, database, AI/ML, Excel, cache, cloud, auth, workflow/undo nhiều bước.
4. Hợp đồng 5 hàm analysis và 3 hàm Figure nằm ở PROJECT_SPEC; mọi logic xử lý số ở analysis, vẽ ở charts, điều phối/UI ở app; phụ thuộc một chiều.
5. `st.session_state` tùy biến, cache và callbacks không cần cho sample nhỏ. Tính lại cleaned từ raw sau mỗi rerun. Không đột biến raw input.
6. Thư viện ứng dụng trực tiếp: NumPy, Pandas, Matplotlib, Streamlit; pytest chỉ test. Không thêm dependency nếu không có lý do trực tiếp và được owner chấp thuận.

## B. Số liệu và an toàn dữ liệu
7. **Drop duplicate toàn dòng (keep first) trước median-fill theo cột số**; chỉ làm một vòng, không sửa raw; cảnh báo nếu sau điền còn duplicate hoặc thiếu.
8. NaN numeric có thể fill nếu còn giá trị hữu hạn; all-NA giữ thiếu; NA nhóm không tự điền; GroupBy missing keys không tính, mean thiếu không thay bằng 0.
9. Numeric ±∞ **không hỗ trợ**: báo lỗi rõ ràng, không vẽ/tính sai. CSV lỗi/thiếu cột phải có thông báo; không lặng lẽ bỏ dòng hoặc ép text thành số.
10. Std là **độ lệch chuẩn tổng thể, `ddof=0`**; không sử dụng mặc định Pandas `ddof=1`. Với count0 các chỉ số số là None; với count1 std0; không làm tròn nội bộ, dùng sai số khi test.
11. Histogram **5 bins, frequency**; bar biểu diễn mean và Y bắt đầu 0; scatter ghép X/Y theo **cùng hàng**. Không trình bày tương quan thành quan hệ nhân quả; dữ liệu sinh viên chỉ là **giả lập**.

## C. Kiểm chứng và tính tương thích
12. Runtime mục tiêu **CPython 3.13 là đề xuất**, chưa có exact locked versions; ở P0 chọn và pin sau cài đặt/kiểm thử thật. Pandas 3.x cần nhận text dtype `str`/category, không chỉ `object`.
13. CSV upload giới hạn **2 MiB** (project policy); **khác** giới hạn **100 MB cho PDF của thầy**. Nêu rõ chỉ hỗ trợ CSV UTF-8 dấu phẩy, dataset nhỏ; không hứa mọi CSV đều được parse chính xác.
14. Kiểm thử oracle/edge tại PROJECT_SPEC: **OR-01..15, IO-01..10, UI-01..06**. Tests và log **chưa có** trong giai đoạn nghiên cứu. Không dùng code/test giả, không thay thế GUI smoke bằng số liệu tính tay.
15. Không gọi DONE nếu không có bằng chứng thực: commit + commands + test outputs + screenshot, không chỉ có kế hoạch trên giấy.

## D. Quyền, Git và sản phẩm nộp
16. Giai đoạn **R01–R07 + FINAL chỉ nghiên cứu**. P0–P4 bắt đầu **sau FINAL đạt READY FOR IMPLEMENTATION và chủ dự án chủ động giao**. Không tự merge PR, force push, xóa branch/history hay đổi visibility.
17. Không đưa PII, credential, API token hoặc dữ liệu sinh viên thật vào repo/video; dẫn nguồn hợp pháp khi dùng tài liệu bên ngoài.
18. Bắt buộc theo form: link GitHub, YouTube demo, PDF **15–20 trang ≤100 MB**, tự chấm 5 tiêu chí **3+2+2+1+2**. **18 trang và video ~7 phút chỉ là khuyến nghị**, không được gán cho giảng viên. Không có module tạo PDF trong ứng dụng.
19. Minh chứng EV-01..16 ở `docs/DELIVERABLES.md` phải khớp **cùng commit SHA/dataset/versions**; PDF render và kiểm từng trang/Unicode/links; người chấm mở được repo/video. Không tự chấm 10/10.
20. Mỗi phiên chỉ cập nhật **source of truth** tương ứng, tránh sao chép nội dung qua nhiều Markdown. Cuối phiên cập nhật `docs/STATUS_HANDOFF.md`; nếu một yêu cầu chưa có căn cứ ghi `UNKNOWN`, không bịa.

**Vị trí chi tiết:** yêu cầu và trích nguồn → `docs/REQUIREMENTS.md`; chức năng/đầu vào/đầu ra/oracle → `PROJECT_SPEC.md`; task & gates → `docs/PLAN.md`; PDF/video/EV → `docs/DELIVERABLES.md`; tiến độ thực tế → `docs/STATUS_HANDOFF.md`.

# PLAN — research-first, minimal-first

**Tiến độ:** R01 và R02 hoàn thành về mặt nghiên cứu; **R03 là lượt tiếp theo**. Đang ở pha CHỈ NGHIÊN CỨU, không được tạo code cho đến R01–R07 + FINAL và owner giao bắt đầu.

## A. 7 research sessions + 1 final review

| Lượt | Phạm vi, sản phẩm | Trạng thái |
|---|---|---|
| R01 | Đối chiếu form thầy, requirement IDs F01–F06, gates, điểm tự đánh giá → docs/REQUIREMENTS.md | DONE |
| R02 | Khóa **MVP design baseline và dataset chính 12→10**, sơ đồ use case, so sánh công nghệ → PROJECT_SPEC.md | DONE |
| R03 | Thiết kế hàm/API, số file code tối thiểu, giao diện Streamlit 1 trang, cơ chế không cần state phức tạp | NEXT |
| R04 | Kiểm tra công thức, thống kê, thao tác cleaning và 3 chart; NaN/std (ddof), tránh kết luận nhân quả | NOT STARTED |
| R05 | Soạn test cases, kỹ thuật chạy offline, Python/package versions, lỗi file và QA checklist | NOT STARTED |
| R06 | Outline PDF 15–20 trang, storyboard video YouTube, evidence và mẫu tự chấm 5 tiêu chí | NOT STARTED |
| R07 | Hoàn thiện rules/handoff, coding tasks & prompt cho AI sau này; tránh trùng tài liệu | NOT STARTED |
| FINAL | Đối chiếu chéo mọi tài liệu; khóa baseline trước coding | NOT STARTED |

Không cần 7 file research riêng: kết quả mỗi lượt được hòa vào **PROJECT_SPEC.md**, **docs/REQUIREMENTS.md**, **docs/PLAN.md**, **RULEBOOK.md**, **AGENTS.md** và **docs/STATUS_HANDOFF.md**. Chỉ tạo `docs/DELIVERABLES.md` tại R06.

## B. R02: danh sách chức năng / thứ tự demo đã lựa chọn

**MVP CORE:** 
1. Upload CSV hoặc tự nạp `sample_data.csv`.
2. Hiển thị 12 dòng, 4 cột, 2 duplicate, 2 missing; xem vài dòng đầu.
3. Một công tắc Clean: exact drop duplicates → numeric median fill, không sửa bảng raw; xem so sánh 12→10, NaN 2→0.
4. Numeric mean/median/std/min/max; groupby `lop`–`diem`; NumPy có tính toán thực.
5. Matplotlib: histogram `diem`, bar `lop`–điểm TB, scatter `gio_hoc`–`diem`.
6. Download CSV đang xem.

**Ngoài phạm vi:** Excel, biểu đồ nâng cao/custom theme, phân trang, login, database, machine learning, Data-Forge gốc, Undo history, PDF generator **trong app**. Báo cáo **PDF bên ngoài app** vẫn bắt buộc khi nộp.

**Không quyết trước R03:** số lượng file Python chính xác, chữ ký hàm, cách tổ chức st.session_state và cách render figure. Chọn hướng một trang nhưng R03 mới chốt contract.

## C. Dataset (đặc tả duy nhất; chưa tạo file)

Dữ liệu CSV giả lập 12 hàng / 4 cột nằm nguyên văn tại **PROJECT_SPEC.md §5**. Chỉ tạo một file `sample_data.csv` ở P0; không phân tách clean/dirty CSV.

**Oracle R02 (tự tính từ specification, chưa test implementation):**

| Chỉ số | Raw | Sau clean |
|---|---:|---:|
| Row count | 12 | 10 |
| Exact duplicates | 2 | 0 |
| Missing cells | 2 | 0 |
| Mean điểm | 85/11 ≈ 7.7272727 | 78/10 = 7.8 |
| Median fill giờ học | — | 4 |
| Median fill điểm | — | 8 |
| Mean điểm A | — | 8.0 |
| Mean điểm B | — | 7.6 |
| Số điểm >=8 | — | 6 |

Ứng dụng/hàm tính dùng dataset này làm nguồn tham chiếu duy nhất khi quay video/báo cáo; 5-row fixture cũ chỉ dùng inline test nếu cần. R04/R05 tiếp tục độc lập xác minh số liệu, không sao chép ngầm các oracle chưa được kiểm tra.

## D. Giai đoạn implementation — chưa kích hoạt

| Bước | Việc | Gate |
|---|---|---|
| P0 | Khi được giao: khóa spec, requirements, tạo CSV giả lập từ PROJECT_SPEC và môi trường | Dữ liệu chuẩn có nguồn, chạy import module |
| P1 | Code logic read/clean/stats Pandas + NumPy | Test oracle + error cases |
| P2 | Code 3 Matplotlib figures | Chart theo đúng nguồn/nhãn |
| P3 | Streamlit một trang, upload, preview/toggle, charts, export | Full demo end-to-end |
| P4 | Test, README thực thi, quay YouTube, PDF 15–20 trang <=100MB, tự chấm, kiểm quyền xem links | Gates G-APP..G-SUBMIT |

## E. Tiêu chí nghiệm thu R02
- [x] Rà soát tất cả file và trạng thái repo/PR.
- [x] Đối chiếu ngược với thang tự đánh giá của thầy.
- [x] So sánh ít nhất bốn cách triển khai và lý do chọn UI 1 trang.
- [x] Giới hạn rõ CORE/OUT và tính năng báo cáo trong app ≠ PDF nộp.
- [x] Dataset 4 cột, trường hợp missing/duplicate, các phép tính oracle số học cụ thể.
- [x] Nêu rõ rủi ro median fill, all-NaN, st rerun và khả năng trình bày.
- [x] Ghi source docs chính thức, không bịa yêu cầu hay kết quả chạy code.
- [x] Ghi R03 là nhiệm vụ kế tiếp duy nhất.

**Gate để thông báo project đã xong sẽ hoàn toàn khác với gate nghiên cứu.** Không đánh dấu checklist implementation là pass ở lượt R02.

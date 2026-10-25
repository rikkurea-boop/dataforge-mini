# STATUS_HANDOFF — DataForge Mini, 2026-10-25, Research 03

## Trạng thái thực tế
- Repo private: https://github.com/rikkurea-boop/dataforge-mini
- Docs branch: `docs/project-charter-ai-handoff`; PR #1: https://github.com/rikkurea-boop/dataforge-mini/pull/1 (open, **chưa merge**).
- `main` vẫn chỉ có initial README (kiểm tra lúc bắt đầu R03).
- **Chỉ tài liệu được cập nhật**. Không có `app.py`, `analysis.py`, `charts.py`, `sample_data.csv`, `requirements.txt`, tests, app chạy, YouTube hay PDF. Không có test runtime/pytest pass.
- Mọi tài liệu nằm ở branch của PR #1; các repo khác (đặc biệt Data-Forge gốc) không bị thay đổi.

## 7 lượt research + FINAL

| Phiên | Trạng thái | Quyết định / ranh giới |
|---|---|---|
| R01 | DONE | Thầy yêu cầu mã nguồn, YouTube demo, PDF 15–20 trang <=100MB, tự chấm 3+2+2+1+2 |
| R02 | DONE | Một MVP CSV 12 hàng, làm sạch 2 duplicates và 2 missing → 10 hàng, thống kê, 3 biểu đồ |
| R03 | **DONE — SPEC ONLY** | **3 file Python** `app.py`, `analysis.py`, `charts.py`; 5 function contracts analysis, 3 Figure charts; Streamlit 1 trang, checkbox từ raw, không custom Session State |
| R04 | **NEXT** | Độc lập xác minh toán, `ddof`, NaN, median fill/duplicates, biểu đồ/interpretation |
| R05 | NOT STARTED | Test cases, Python/Streamlit versions, fresh install/run, lỗi đầu vào |
| R06 | NOT STARTED | Outline báo cáo PDF 15–20 trang, YouTube storyboard, tự đánh giá |
| R07 | NOT STARTED | Cập nhật quy tắc/handoff/prompt triển khai cuối |
| FINAL | NOT STARTED | QA chéo và quyết định READY FOR IMPLEMENTATION |
| P0–P4 | **BLOCKED** | **Không code cho tới FINAL và lệnh mới từ owner** |

## R03 nghiên cứu gì và đã ghi ở đâu?
1. Đọc 8/8 file hiện có trên nhánh docs và trạng thái GitHub/PR.
2. Từ R02 so sánh 1-file / 3-file / multi-layer; chọn 3 file cho dễ test và thuyết trình, không tạo folder `src/`.
3. Định nghĩa các hàm `load_csv`, `inspect_data`, `clean_data`, `numeric_stats`, `mean_by_group` trong `PROJECT_SPEC.md §10.3`.
4. Chart contracts `histogram`, `group_bar`, `scatter` trả `matplotlib.figure.Figure`, không dùng pyplot global (PROJECT_SPEC §10.4).
5. Thiết kế flow uploader, sample fallback, clean toggle, selectboxes, conditional plot, CSV export; Streamlit rerun không yêu cầu `st.session_state` tùy biến.
6. Kiểm tra tài liệu chính thức cho file uploader BytesIO, st.pyplot(Figure), widgets/rerun, Matplotlib Figure và pandas CSV; nguồn tại PROJECT_SPEC §10.8.
7. Không quyết `ddof` hoặc ép mọi CSV phải không còn NaN; R04 cần chốt cách xử lý toán học.
8. **Chưa có code/test**, không biến outline thành tính năng đã tồn tại.

## Quyết định UX quan trọng và rủi ro đã kiểm soát
- Chỉ 3 cột được chọn: cột số chính, cột nhóm, cột số X (tối đa 3 selectboxes).
- Bảng raw không mutate; checkbox cleaned gọi `clean_data(raw_df)` mỗi rerun, không tự lưu lịch sử.
- Dùng `Path(__file__).with_name("sample_data.csv")` tránh lỗi khác thư mục chạy lệnh.
- Upload là buffer, **không** dùng filename để truy cập tệp trên host.
- Scatter loại NA theo **cặp hàng**, không drop riêng từng trục.
- Nếu upload thiếu cột tương thích thì chỉ ẩn plot liên quan; không crash/không tự bịa cột.
- UI bắt lỗi dữ liệu nhập; không dùng `except Exception` bỏ qua.

## R04 — nhiệm vụ tiếp theo duy nhất
**Research 04: toán học và tính đúng đắn dữ liệu** theo `PROJECT_SPEC.md §§5,10`: xác nhận oracle của 12 hàng; thống kê NumPy/Pandas và `ddof`; all-NaN, nonnumeric, duplicates sinh sau imputation; quy tắc vẽ histogram, bar mean, scatter pairs; phát biểu kết luận hợp lệ. Ghi các expected values và edge-case decisions trong tài liệu **không code**.

## Metadata handoff
- Ngày: 2026-10-25.
- Branch: `docs/project-charter-ai-handoff`; PR #1.
- Chỉ docs: `PROJECT_SPEC.md`, `docs/PLAN.md`, `RULEBOOK.md`, `docs/REQUIREMENTS.md`, `docs/STATUS_HANDOFF.md` (+ README nếu cần).
- Commit SHA của R03: xem branch head/PR #1 tại GitHub; không suy đoán.
- Nghiệm thu R03 là **tài liệu thiết kế**, không phải test app.

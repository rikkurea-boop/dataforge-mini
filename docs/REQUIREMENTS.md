# REQUIREMENTS — yêu cầu có bằng chứng và nguồn tham chiếu

**Mục tiêu:** phân biệt **thầy thực sự yêu cầu**, **user quyết định**, **AI đề xuất**, và **chưa biết**. Đây là hồ sơ truy xuất nguồn, không phải danh sách tính năng tự tưởng tượng. R01 xác minh **hai ảnh biểu mẫu do user cung cấp trong chat ngày 2026-10-25**, R02–R06 bổ sung giải pháp kỹ thuật và tài liệu bên ngoài. **Ảnh gốc chưa có trong repo**, không được tuyên bố đã kiểm lại nguyên ảnh chỉ nhờ file này; nếu có form cập nhật, đối chiếu trực tiếp và sửa các mục liên quan.

## 1. Bốn mức bằng chứng

- **FORM-CONFIRMED:** nhìn thấy trực tiếp trong vùng ảnh biểu mẫu; không suy diễn toàn bộ form đã được quan sát.
- **USER-DECIDED:** yêu cầu/ưu tiên do chủ dự án trực tiếp chốt.
- **DESIGN-PROPOSED:** giải pháp để đạt mục tiêu, **không phải** yêu cầu từ thầy.
- **UNKNOWN:** ảnh hiện có không đủ xác minh, không tự coi là "không bắt buộc".

## 2. Ma trận yêu cầu đã xác nhận

| ID | Loại | Nội dung và giới hạn bằng chứng | Cổng bằng chứng khi hoàn thành |
|---|---|---|---|
| **F01** | FORM-CONFIRMED | Bài tập **cá nhân** trong Chương 5, chọn **5.5 – Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib** | Mã nguồn/README và demo đúng đề tài |
| **F02** | FORM-CONFIRMED | Tự điền và kiểm tra **thông tin cá nhân** trên form | Người nộp xác minh trong form, không commit PII lên repo |
| **F03** | FORM-CONFIRMED | **Link mã nguồn GitHub hoặc nền tảng tương đương** (trường bắt buộc) | Link source đúng bản cuối, thầy mở được |
| **F04** | FORM-CONFIRMED | **Link video YouTube demo sản phẩm** (trường bắt buộc) | URL watch mở được với quyền người chấm |
| **F05** | FORM-CONFIRMED | **Một PDF báo cáo 15–20 trang, dung lượng tối đa 100 MB** (trường bắt buộc) | File mở, đếm trang vật lý, kiểm byte/ảnh/link |
| **F06** | FORM-CONFIRMED | **Đoạn văn ngắn tự nhận xét và tự chấm** theo 5 tiêu chí, nêu ưu điểm/hạn chế/lý do | Nội dung có thực chứng, tối đa 10 điểm |
| **U01** | USER-DECIDED | Tên đề tài: “Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python” | Thống nhất trên README/báo cáo/video |
| **U02** | USER-DECIDED | DataForge Mini **độc lập** DataForge gốc; ưu tiên **cực gọn**, user giải thích được toàn bộ code | Không phụ thuộc original repo, source ít tầng |
| **U03** | USER-DECIDED | Nghiên cứu **7 lượt + 1 FINAL** riêng; **chưa viết app** trong research | Git tree research chỉ tài liệu, coding phải có lệnh mới |

**Nguồn gốc:** FORM-01 ảnh đầu chứa thông báo dự án cá nhân và danh sách chủ đề 5.1–5.5; FORM-02 ảnh tiếp theo thể hiện trường link code, video YouTube, PDF 15–20 trang ≤100MB và tự chấm điểm. Hai ảnh đang nằm trong conversation, không có SHA file ảnh ở GitHub. Nếu cần kiểm toán nguyên văn lần sau, chủ dự án cần cung cấp file ảnh/form hoặc quyền xem chat chứa nguồn.

## 3. Cơ cấu TỰ ĐÁNH GIÁ có trong form (không khẳng định là rubric chấm cuối duy nhất)

| Tiêu chí sinh viên tự chấm | Tối đa |
|---|---:|
| Mức độ hoàn thành chức năng | **3** |
| Kiến thức và kỹ thuật Python | **2** |
| Chất lượng mã nguồn | **2** |
| Giao diện/trải nghiệm hoặc trực quan hóa | **1** |
| Báo cáo và minh chứng | **2** |
| **Tổng** | **10** |

**Không điền điểm trước khi kiểm thử sản phẩm.** Khung nhận xét và evidence liên kết với từng tiêu chí nằm trong `docs/DELIVERABLES.md`.

## 4. Điều chưa được ảnh/form chứng minh

- **Deadline**, giờ đóng form, lịch bảo vệ và xử lý nộp muộn.
- **Thời lượng video** và việc có cần facecam/giọng thuyết minh.
- **PPT** có bắt buộc không; ảnh không cho phép kết luận có/không.
- **Template PDF** (font, lề, APA/IEEE, phụ lục có được tính trang không). Đề xuất mặc định đếm trang vật lý cả bìa/mục lục cho an toàn.
- Yêu cầu của thầy về **framework GUI**, CSV/Excel, số biểu đồ, kỹ thuật cleaning cụ thể và những trường form ngoài ảnh.
- Phiên bản Python/package hoặc hệ điều hành máy chủ dự án sẽ sử dụng.

**Khi có nguồn mới:** ghi URL/ảnh/tên file, mục/trang/giờ kiểm; cập nhật Fxx nếu thực sự thêm yêu cầu; kiểm ảnh hưởng lên `PROJECT_SPEC`/`PLAN`/`DELIVERABLES` và ghi quyết định.

## 5. Thiết kế do project tự chọn — không gán cho thầy

| ID | Thiết kế | Tại sao | Nơi dùng |
|---|---|---|---|
| **D01** | Streamlit một trang, file CSV/10–12 record, không backend | Ít code UI, trình bày dễ | PROJECT_SPEC M01–M07 |
| **D02** | Pandas dedup→median fill, NumPy stats ddof0, Matplotlib hist/bar/scatter | Ba thư viện dùng đúng trọng tâm, có expected values | PROJECT_SPEC §§2–5 |
| **D03** | Ba file chính `app.py`/`analysis.py`/`charts.py` | Tách UI/dữ liệu/hình, không overengineering | PLAN T03–T08 |
| **D04** | Target Python3.13, cap CSV upload 2 MiB, QA 15 OR+10 IO+6 UI | Lặp lại được và không khó test | PROJECT_SPEC §5–`6 |
| **D05** | Report đích 18 trang, YouTube demo khoảng 7 phút | Giúp quy trình minh chứng gọn | DELIVERABLES |

**Vấn đề thường nhầm:** thầy yêu cầu **báo cáo PDF**, **không có căn cứ thầy yêu cầu ứng dụng tự xuất PDF**. PDF generator trong app là OUT OF SCOPE.

## 6. Nguồn kỹ thuật tham khảo — API/standard, KHÔNG phải rule của thầy

Nguồn gốc qua R02–R05 được lưu trong git history; dưới đây là các trang **chính thức** có vai trò trong quyết định hiện hành. Đọc lại theo đúng phiên bản dependency khi P0 bắt đầu.

| Nhóm | Nguồn | Dùng để xác minh |
|---|---|---|
| Pandas CSV | https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html | Đọc CSV, parse/file-like |
| Pandas duplicate/NA | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html ; https://pandas.pydata.org/docs/user_guide/missing_data.html | whole-row dedup, missing/fill |
| Pandas GroupBy | https://pandas.pydata.org/docs/user_guide/groupby.html | mean, group key NA handling |
| Pandas std | https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html | mặc định ddof1, phải ghi ddof0 nếu dùng |
| Pandas string dtype 3.0 | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html ; https://pandas.pydata.org/docs/user_guide/migration-3-strings.html | text dtype `str` có thể không là object |
| NumPy std/finite | https://numpy.org/doc/stable/reference/generated/numpy.std.html ; https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html | ddof0; phân biệt NA/inf |
| Matplotlib histogram | https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html | bins/density, last-edge semantics |
| Matplotlib Figure | https://matplotlib.org/stable/api/figure_api.html | trả Figure độc lập |
| Streamlit widgets | https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader ; https://docs.streamlit.io/develop/api-reference/charts/st.pyplot ; https://docs.streamlit.io/develop/api-reference/widgets/st.download_button | upload, explicit Figure, export |
| Streamlit rerun | https://docs.streamlit.io/develop/concepts/architecture/session-state | widget reruns mà không cần custom state |
| Test/venv | https://docs.pytest.org/en/stable/how-to/assert.html ; https://docs.python.org/3/library/venv.html | approx comparison, virtual environments |
| Release candidates | https://www.python.org/downloads/ ; https://pypi.org/project/numpy/ ; https://pypi.org/project/pandas/ ; https://pypi.org/project/matplotlib/ ; https://pypi.org/project/streamlit/ ; https://pypi.org/project/pytest/ | Python3.13 / package candidates; **không phải bằng chứng tổ hợp đã chạy** |

## 7. Nguồn quy trình nộp / quyền truy cập

- YouTube Public/Unlisted/Private: https://support.google.com/youtube/answer/157177 . Unlisted xem được qua URL nhưng có thể chia sẻ lại; Private không chỉ cần link.
- GitHub access: https://docs.github.com/en/repositories/creating-and-managing-repositories/access-to-repositories . Repo hiện private; xác minh quyền người chấm, **không tự thay visibility**.
- Quy trình báo cáo kỹ thuật và nguồn đại học: xem **`docs/DELIVERABLES.md`**.
- 100 MB của PDF **khác** giới hạn CSV upload 2 MiB do project tự đặt.

**Quy tắc trích dẫn:** dẫn đúng trang tài liệu dùng, phiên bản/ngày nếu claim phụ thuộc release; không tuyên bố đã xem một trang cụ thể trong PDF/trang web khi mới xem mục lục. Không bịa URL hoặc ngày.

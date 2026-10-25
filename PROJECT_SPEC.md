# PROJECT SPEC — DataForge Mini, MVP research baseline (R02)

**Trạng thái:** Research 05/07 hoàn thành; **MVP + ARCHITECTURE + MATH + TEST/ENV DESIGN BASELINE**, chưa phải code/final approval. R03 đã khóa sơ đồ module/hợp đồng hàm; R04 đã kiểm định toán; R05 đã thiết kế kiểm thử/môi trường; R06 đồ án nộp bài; R07 handoff; FINAL mới có thể đạt READY FOR IMPLEMENTATION.

## 1. Thông tin khóa từ chủ dự án và giảng viên

- Tên chính thức: **Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python**.
- Mục 5.5: phân tích dữ liệu cơ bản với **NumPy, Pandas, Matplotlib**.
- Bài nộp cá nhân; link mã nguồn, link video YouTube, **báo cáo PDF 15–20 trang không quá 100 MB**, tự nhận xét/tự chấm theo 3+2+2+1+2. Xem `docs/REQUIREMENTS.md`.
- Ưu tiên chủ dự án: **tối giản tối đa nhưng đủ chức năng; giải thích được toàn bộ code khi trình bày**.
- Dự án độc lập; không sửa, không import hoặc bắt phụ thuộc Data-Forge gốc.
- **Không viết code/app/dataset thật trong 7 lượt nghiên cứu và lượt FINAL.**

## 2. Tuyên bố bài toán — cố tình hẹp

Người dùng có bảng kết quả học tập dạng CSV, muốn nhanh chóng xem dữ liệu, phát hiện các lỗi đơn giản, tính thống kê mô tả và xem ba biểu đồ cơ bản. Đây là ví dụ học tập **không nhằm quản lý điểm chính thức, không dùng ML, không khẳng định quan hệ nhân quả**.

**Kịch bản thành công:** mở app → xem dữ liệu sinh viên giả lập → quan sát 12 dòng/2 trùng/2 thiếu → bật làm sạch → được 10 dòng/không còn hai lỗi đó → xem điểm trung bình/lớp → xem histogram/bar/scatter → tải CSV. Mọi con số giải thích lại được bằng tay.

**Quan trọng:** form không bắt buộc một domain dữ liệu, Streamlit hay ba biểu đồ. Đây là **lựa chọn thiết kế** có thể điều chỉnh khi thầy cung cấp thêm hướng dẫn; không gán cho giảng viên.

## 3. Quyết định R02: danh mục chức năng theo mức độ

| ID | Chức năng | Mức | Lý do | Tiêu chí nghiệm thu sau khi có code |
|---|---|---|---|---|
| M01 | Đọc một CSV hoặc mặc định dữ liệu demo có sẵn | CORE | Một luồng dữ liệu, dễ quay video | Hiển thị đúng số hàng/cột và vài hàng mẫu |
| M02 | Quan sát shape, tên cột/kiểu số và số NaN/trùng | CORE | Chứng minh Pandas và lỗi thực | 12 hàng, 4 cột, 2 ô thiếu, 2 dòng trùng ở dữ liệu mẫu |
| M03 | Một thao tác làm sạch: drop exact duplicates (keep first), sau đó điền NaN của cột số bằng median từng cột | CORE | Một quy trình minh bạch, ít UI | 10 hàng, 0 trùng, 0 thiếu trên dữ liệu mẫu; không mutate bản gốc |
| M04 | Thống kê numeric: valid count, min, max, mean, median, std; groupby mean nếu có cột phân loại | CORE | NumPy + Pandas xuất hiện thật | Điểm trung bình 7.8; A 8.0; B 7.6 sau cleaning |
| M05 | Ba biểu đồ Matplotlib: histogram numeric, bar group mean, scatter hai numeric | CORE | Ba cách nhìn dữ liệu, kiến thức khác nhau | Biểu đồ đúng số liệu, title và nhãn, chỉ hiện khi đủ loại cột |
| M06 | Tải CSV của tập đang xem (raw hoặc cleaned) | CORE | Hoàn tất flow input → output | Số dòng và giá trị file tải khớp view |
| M07 | Giao diện một trang: chọn nguồn, preview, công tắc clean, stats, charts, export | CORE | Ít mã hơn multi-page/backend | Demo liền mạch, không có navigation phức tạp |
| S01 | Bộ test đầu vào lỗi, chất lượng số liệu, invalid chart column | REQUIRED FOR QUALITY (không phải tính năng UI) | Dễ bảo vệ khi thầy hỏi code | Test/acceptance ghi nhận trung thực tại R05/P1–P4 |
| X01 | Excel, JSON, Parquet, URL import, hàng triệu dòng | OUT | Không cần thiết, phình scope | Không tạo |
| X02 | Login, cloud, REST, database, multiuser, DataForge core | OUT | Lệch chủ đề | Không tạo |
| X03 | ML dự đoán điểm, PCA, clustering, AI chatbot | OUT | Không cần ở Chương 5.5 | Không tạo |
| X04 | Undo history, rule-based pipeline, advanced chart builder, 10+ plots | OUT | Khó giải thích, tăng mã | Không tạo |
| X05 | PDF report generator **trong ứng dụng** | OUT | PDF 15–20 trang là bài báo cáo nộp bên ngoài | Không tạo |
| X06 | Thiết kế PPT, video, PDF sản phẩm ngay trong giai đoạn nghiên cứu | OUT UNTIL IMPLEMENTATION | Chưa có ảnh/code để đối chiếu | Chỉ xây outline trong R06 |

**Sự phân biệt then chốt:** video YouTube và báo cáo PDF là **bắt buộc cho bài nộp**, còn *chức năng ứng dụng tự sinh báo cáo PDF* không bắt buộc.

## 4. UX tối thiểu từ R02 (R03 đã khóa hợp đồng tại §10)
- **Một trang**, bốn khu vực theo thứ tự: nguồn dữ liệu → xem/clean → thống kê → ba biểu đồ → tải CSV.
- Bắt đầu bằng file demo; cho phép upload CSV thay thế. Không cần bước tạo tài khoản, chọn project, workflow setup.
- Chỉ có **một checkbox/toggle** để xem bảng sạch; mỗi lần chuyển trạng thái tính **từ bảng gốc**, không cộng dồn. Cơ chế rerun tự nhiên của Streamlit cho phép bỏ Undo/Redo; xem docs Streamlit session/rerun. Nếu thực thi cần state, R03 phải giải thích nhu cầu tối thiểu.
- **Làm sạch không âm thầm:** hiển thị số dòng và ô NaN trước/sau, và thao tác đã áp dụng; không tự đổi tên/xóa cột dữ liệu.
- Stats mặc định cột `diem` của bộ demo; người dùng được chọn numeric column nếu upload dữ liệu khác.
- Biểu đồ mặc định: `diem` histogram; `lop` vs mean `diem` bar; `gio_hoc` vs `diem` scatter. Chỉ chọn cột tương thích, nếu không có thì thông báo/ẩn biểu đồ đó; **không** có chỉnh màu, style, palette, animation, hiệu ứng.
- CSV khác được hỗ trợ theo quy tắc chung với numeric/category; **không** hứa hỗ trợ tùy ý mọi định dạng, cột datetime, encoding hiếm hoặc dữ liệu lớn.

## 5. Dataset chính duy nhất — SPEC, KHÔNG PHẢI FILE CSV ĐÃ TẠO

**Tên file dự kiến khi bắt đầu code:** `sample_data.csv`. **Nguồn:** dữ liệu giả lập tự thiết kế, không phải điểm cá nhân có thật; cột `ten, lop, gio_hoc, diem`, dấu phẩy CSV, UTF-8 ASCII values. Dùng **một file duy nhất** để minh họa xem dữ liệu bẩn và sau làm sạch; **không thêm file dirty thứ hai**.

```csv
ten,lop,gio_hoc,diem
An,A,4,8
Binh,B,2,6
Chi,A,6,9
Dung,B,3,7
Ha,A,7,10
Lan,B,5,8
Minh,A,,7
Ngoc,B,4,
Phuc,A,3,6
Quynh,B,6,9
An,A,4,8
Dung,B,3,7
```

Cơ sở lựa chọn: 4 cột dễ hiểu, 2 cột số cho scatter, 1 cột nhóm cho bar/groupby, điểm số có phân bố cho histogram; đúng 2 duplicate **toàn dòng** và đúng 2 NaN trong numeric; 12 dòng đủ nhỏ để kiểm chứng thủ công và hiện rõ trong demo.

### Expected results — tính theo chính dữ liệu trên, trước khi viết app
- **Raw:** 12 dòng, 4 cột; 2 exact duplicate (các dòng lặp `An`/`Dung`), 2 ô trống (`Minh.gio_hoc`, `Ngoc.diem`).
- **Thứ tự làm sạch bắt buộc để đối chiếu:** `drop_duplicates(keep="first")` → median-fill numeric của **10 dòng còn lại**. Median(`gio_hoc`) = 4; median(`diem`) = 8.
- **Clean:** 10 dòng, 4 cột, 0 duplicate, 0 NaN; `Minh.gio_hoc = 4`, `Ngoc.diem = 8`.
- **Clean score:** sum = 78; mean = **7.8**; groupby `lop`: A **8.0** (5 sinh viên), B **7.6** (5 sinh viên); `diem >= 8`: **6/10**; mean `gio_hoc` = **4.4**.
- **Raw score mean** (bỏ NaN, *có* hai dòng trùng): 85/11 = **7.7272727...**. Không so sánh với mean clean như thể dữ liệu được cải thiện theo một thước đo khách quan.
- **Dữ liệu 5 dòng từng dùng trong PPT trước đây** có mean điểm 8.0/A 9.0/B 6.5, là ví dụ khác; **không dùng đáp án đó để đánh giá dataset mới**. Nếu muốn giữ, dùng inline làm test nhỏ, **không tạo fixture CSV thứ hai**.
- Giá trị từ R02 là expected values được tính độc lập từ đặc tả, **chưa chạy pandas/numpy app**. R04 đối chiếu lại bằng công thức, R05 lập unit-test chính thức, implementation mới chạy pytest.

### Chính sách dữ liệu
- Median fill để minh họa phương pháp; với điểm học tập thật, **không được xem đó là điểm được xác minh**. Ghi chú dataset chỉ là mô phỏng.
- Không suy ra giờ học gây ra điểm cao; biểu đồ scatter chỉ trực quan hóa mối liên hệ trong dữ liệu minh họa 10 dòng.
- Dùng `DataFrame.copy()` hoặc cách tương đương để bảo toàn raw input.
- Không ép điền cột phân loại, không xóa rows bị thiếu nếu ngoài 2 bản ghi trùng. Với CSV tùy chọn có cột numeric toàn NaN: giữ nguyên + cảnh báo; không được tuyên bố đã xóa hết NaN.
- Thống kê `std` dùng **độ lệch chuẩn tổng thể, ddof=0**; R04 đã xác minh. Với 0 số hợp lệ: chỉ count=0, các chỉ số khác None; với 1 số hợp lệ std=0.

## 6. Lựa chọn công nghệ — so sánh R02; kết luận kiến trúc chi tiết tại R03 §10

| Phương án | Ưu điểm | Nhược điểm theo mục tiêu user | Kết luận |
|---|---|---|---|
| Jupyter notebook thuần | Ít UI nhất, tốt cho bài học | Không tạo app demo riêng rõ ràng, khó biểu diễn upload/giao diện người dùng | Không chọn cho sản phẩm chính |
| CLI + script Python | Ít dependency, dễ chạy | Khó demo sản phẩm trực quan và tương tác | Không ưu tiên |
| Tkinter | Desktop/offline | Thêm mã GUI/event/nhúng chart; topic 5.1 khác mục 5.5 | Không chọn |
| Flask + HTML/CSS | Linh hoạt | Phát sinh frontend/backend ngoài mục 5.5 | Không chọn |
| **Streamlit một trang** | File upload + UI + Matplotlib Figure + download với ít glue code | Phụ thuộc Streamlit, phải hiểu rerun; rủi ro state nếu overengineer | **Chọn ưu tiên**; R03 xác nhận cấu trúc |

Phụ thuộc ứng dụng dự kiến: **pandas, numpy, matplotlib, streamlit**; kiểm thử **pytest** (development only). Chưa khóa phiên bản; R05 kiểm tra tương thích theo Python runtime được chọn.

## 7. Mapping sang bằng chứng nộp bài

| Tự đánh giá của thầy | Module MVP làm bằng chứng | Báo cáo/video sau này chứng minh |
|---|---|---|
| Chức năng (3) | M01–M07 | Full demo trước/sau, thống kê, chart, export |
| Kỹ thuật Python (2) | M02–M05 | Mã dùng Pandas operations, NumPy mean/median/std, Matplotlib Figure |
| Code (2) | M03–M06 | Tách logic/UI hợp lý, không mutate, input guard, test |
| UX/biểu đồ (1) | M05/M07 | Một trang đơn giản, nhãn/trục đủ, chọn biến đúng loại |
| Báo cáo/minh chứng (2) | Không phải tính năng app | PDF 15–20 trang + YouTube demo + ảnh + tự chấm trung thực |

## 8. Những phần R03–R05 cần xử lý (ghi chú lịch sử nghiên cứu)
- R03: **DONE** — API/function contracts, chính xác 3 file Python, toggle không custom state, uploaded source + sample fallback; xem §10.
- R04: **DONE** — ddof=0, all-NaN, duplicate sau fill, histogram 5 bins và expected values; xem §11.
- R05: test cases, environment/versions, file tải UTF-8, lỗi CSV rỗng/cột không hợp lệ, walkthrough fresh clone.
- R06: PDF nộp bên ngoài app; video phải sử dụng dataset/phiên bản thống nhất.
- R07/FINAL: chống mở rộng phạm vi và đảm bảo chỉ bắt đầu code khi user giao.

## 9. Nguồn docs đã đọc cho quyết định R02
- Pandas CSV: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
- Pandas duplicate: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
- Pandas NaN fill: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
- Pandas groupby: https://pandas.pydata.org/docs/reference/groupby.html
- NumPy NaN mean: https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html
- NumPy NaN median: https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html
- Matplotlib histogram: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
- Streamlit uploader: https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
- Streamlit rerun/state: https://docs.streamlit.io/develop/concepts/architecture/session-state
- Streamlit matplotlib: https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
- Streamlit download: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button

**Không coi docs API là chỉ thị của giảng viên.** Đã đọc docs để kiểm chứng khả năng kỹ thuật, không xác nhận app đang chạy.

---

## 10. Research 03 — Architecture / Function Contracts (2026-10-25)

**Trạng thái: DESIGN BASELINE R03**; đã nghiên cứu tài liệu API chính thức và kiểm tra source tree, **chưa viết/chạy app**. R04 xác thực toán và edge cases, R05 khóa môi trường và test.

### 10.1. Vì sao ba file Python?

| Phương án | Đánh giá |
|---|---|
| `app.py` duy nhất | Ít file nhất nhưng UI, phép tính và chart lẫn nhau; khó test giải thích |
| **`app.py`, `analysis.py`, `charts.py`** | **CHỌN:** ba trách nhiệm rõ, không tầng trung gian; nhóm test được logic độc lập |
| 5–10 module, class/service/repository/pipeline | Lệch yêu cầu đơn giản; bỏ |
| Web frontend + REST backend | Không cần, bỏ |

**Ứng dụng một trang**, một tiến trình Streamlit, dữ liệu nhỏ trong bộ nhớ; không có model class, dataclass, dependency injection, database, cache, network/API, callbacks, global mutable state, class-based service, hệ thống config đa tầng.

**Cây file ứng dụng dự kiến sau khi được giao code (không phải file đang có):**

```text
app.py                  # giao diện Streamlit và điều phối
analysis.py             # 5 hàm đọc / đo / clean / thống kê / group mean
charts.py               # 3 hàm dựng Matplotlib Figure
sample_data.csv         # DUY NHẤT, tạo từ §5 (dữ liệu giả lập)
requirements.txt        # pandas, numpy, matplotlib, streamlit
tests/test_analysis.py  # test chức năng số & cleaning, được lập kế hoạch ở R05
```

### 10.2. Quy tắc phụ thuộc một chiều

```text
                   sample_data.csv       [UploadedFile CSV]
                          \                    /
                           \                  /
                            v                v
                           app.py (Streamlit)
                            |       |      |
                    selects v       |      v  st.pyplot(Figure)
                       analysis.py   |    charts.py
                         DataFrame --+-------^
                         Series -------------^
```

- `analysis.py` chỉ import **pandas, numpy** và chuẩn thư viện nếu cần. **Không import Streamlit/Matplotlib**.
- `charts.py` chỉ import **pandas, matplotlib.figure.Figure** (và các module thật sự cần); **không import Streamlit**, không đọc CSV.
- `app.py` chỉ điều phối widgets, gọi hàm, bắt lỗi đầu vào, hiển thị dữ liệu/Figure, xuất CSV; **không viết lại phép tính median/mean/groupby ở UI**.
- Không cyclic import. Chỉ các hàm public nêu ở 10.3/10.4; thêm helper chỉ nếu loại bỏ lặp mã thật hoặc cần test độc lập.

### 10.3. Hợp đồng 5 hàm trong `analysis.py`

Các chữ ký sau là **spec code cho implementation về sau**, không phải code đã tạo.

| API dự kiến | Nhận | Trả | Ràng buộc / hành vi |
|---|---|---|---|
| `load_csv(source: str | Path | BinaryIO) -> pd.DataFrame` | Đường dẫn file mẫu hoặc file upload nhị phân | DataFrame mới | Dùng `pd.read_csv`, đọc đúng **một file**; chặn header/data rỗng bằng lỗi thân thiện ở UI. Upload cần `seek(0)` trước khi đọc nếu stream đã bị tiêu thụ. Không tự sửa tên/dtype/missing hoặc ghi file; không âm thầm bỏ dòng |
| `inspect_data(df: pd.DataFrame) -> dict[str,int]` | Bảng bất kỳ | `rows, columns, missing_cells, duplicate_rows` | Dùng `shape, isna, duplicated`; không mutate; loại trùng là exact whole-row, không theo tên |
| `clean_data(df: pd.DataFrame) -> pd.DataFrame` | Raw dataframe | Bảng mới | `copy()` → `drop_duplicates(keep="first")` → median điền NaN ở cột số từng cột; **KHÔNG** điền cột text, không tự lọc/drop cột, không mutate đầu vào. Nếu cột số toàn NaN thì giữ nguyên và thông báo phía UI (R04/R05 chốt phương thức cảnh báo). Không hứa clean xong luôn không còn duplicate cho mọi CSV nếu fill tạo ra giá trị trùng mới |
| `numeric_stats(df: pd.DataFrame, column: str) -> dict[str, float | int | None]` | DataFrame + tên cột số | `count, min, max, mean, median, std` | Kiểm tra cột và kiểu; **NumPy thực hiện tính toán số thật**, Pandas chọn cột, loại NA; scalar JSON/Python numbers, không trả `np.generic`; cột thiếu toàn bộ cho `count=0`, số liệu khác `None`/thông báo. **ddof cho std quyết ở R04** |
| `mean_by_group(df: pd.DataFrame, group_column: str, value_column: str) -> pd.Series` | Cột nhóm + cột số | Series điểm TB theo nhóm | Pandas `groupby(...)[value].mean()`, không sửa đầu vào, nhóm không có số hợp lệ xử lý có thông báo. Nhóm kiểu text/category, không dùng số định danh làm group tự động |

**Quy tắc tường minh:** NumPy đảm nhận mean/median/std (sau lọc NaN); Pandas đảm nhận `read_csv`, `drop_duplicates`, `fillna`, `groupby` và tạo cột số. Không thêm một hàm `service` để chỉ gọi lại các hàm khác.

### 10.4. Hợp đồng 3 hàm `charts.py`

| API dự kiến | Nhận | Trả | Nội dung |
|---|---|---|---|
| `histogram(df: pd.DataFrame, column: str) -> Figure` | Cột numeric còn giá trị hợp lệ | `matplotlib.figure.Figure` | Histogram điểm; title + x/y label; `dropna()`; không vẽ biểu đồ rỗng gây hiểu sai |
| `group_bar(means: pd.Series) -> Figure` | Series nhóm và mean từ `mean_by_group` | Figure | Các nhóm và trung bình, nhãn/trục rõ; không tính lại group mean |
| `scatter(df: pd.DataFrame, x_column: str, y_column: str) -> Figure` | Hai cột numeric khác nhau, có ít nhất một cặp quan sát hoàn chỉnh | Figure | Tạo cặp `df[[x,y]].dropna()` **cùng nhau** để giữ đúng hàng; không loại NA từng trục độc lập |

**Chọn Matplotlib object-oriented Figure:** `Figure(figsize=(...))` → `ax = fig.subplots()` → `ax.hist/bar/scatter(...)` → return `fig`. Trong app gọi `st.pyplot(fig)` với đối tượng rõ ràng. Tránh `plt.gcf()`, `st.pyplot()` không có tham số, `plt.show()`, global pyplot state. Đối với Figure không tạo bởi pyplot, không cần registry/close của `pyplot`. Nếu implementation dùng `plt.subplots()` thay thế thì **phải đóng figure** sau render; không tạo thread/lock/backend custom cho demo single-user.

Kiểm tra hợp lệ được làm **một lần theo nhiệm vụ**: UI chọn cột tương thích; hàm xử lý và hàm chart báo lỗi đầu vào sai bằng `ValueError` rõ ràng. Không thêm framework validator nhiều lớp.

### 10.5. Giao diện và tính toán lại không sử dụng session state tự viết

```text
START/RERUN
  1. uploader = st.file_uploader(..., type="csv"), luôn xuất hiện
  2. source = uploader nếu có, ngược lại sample_data.csv theo __file__
  3. raw_df = load_csv(source)               (giữ nguyên trong lần chạy)
  4. raw_profile = inspect_data(raw_df); hiển thị preview + metrics
  5. use_clean = st.checkbox("Làm sạch dữ liệu")
  6. active_df = clean_data(raw_df) if use_clean else raw_df
  7. active_profile = inspect_data(active_df); hiển thị so sánh trước/sau
  8. numeric_cols = list(active_df.select_dtypes(include="number").columns)
  9. selected_value_col = selectbox numeric, ưu tiên "diem" nếu tồn tại
 10. selected_group_col = selectbox cột text/category, ưu tiên "lop"
 11. selected_x_col = selectbox numeric khác selected_value_col, ưu tiên "gio_hoc"
 12. numeric_stats + mean_by_group -> hiển thị
 13. 3 Figure từ charts.py -> st.pyplot(fig); biểu đồ không hợp lệ thì ẩn + giải thích
 14. st.download_button(data=active_df.to_csv(index=False).encode("utf-8-sig"), mime="text/csv")
END; khi upload/checkbox/selectbox thay đổi, Streamlit rerun từ đầu
```

**Không dùng `st.session_state` do ứng dụng không có thao tác cần lưu lịch sử**. Widget tự giữ giá trị trong session; không cần `st.cache_data` cho 12 bản ghi; không tạo reset button, callback hay nhiều trạng thái `raw/cleaned/undo`. Giá trị toggle chỉ quyết định có gọi `clean_data(raw_df)` tại lần chạy đó không.

**Không có upload:** tự lấy file mẫu theo `Path(__file__).with_name("sample_data.csv")`, không dựa vào thư mục shell hiện hành. **Có upload:** ưu tiên uploaded file. Chỉ 1 file, đọc một lần mỗi rerun (vì `UploadedFile` là `BytesIO`, rewind nếu cần). Uploaded file không được dùng làm đường dẫn file trên máy.

**Nếu file không hợp lệ:** thông báo `st.error(...)` và `st.stop()` cho riêng lần chạy đó; bắt lỗi I/O/parsing có phân loại, không dùng `except Exception: pass`. Chỉ hứa **UTF-8 CSV phân cách bằng dấu phẩy, dữ liệu nhỏ**; generic CSV có ít cột/numeric/category chỉ hiện những phần đủ điều kiện.

**Lựa chọn cột:** mặc định bộ demo là `diem`/ `lop`/ `gio_hoc`; khi CSV khác, chọn từ danh sách thực tế. Chỉ cần tối đa 3 selectbox (giá trị numeric, nhóm, numeric trục X). Histogram và stats cùng cột số; bar dùng cột nhóm; scatter dùng X và cột số đã chọn làm Y. Nếu không có category thì bỏ bar; <2 numeric khác nhau thì bỏ scatter; không tự bịa nhóm/cột; không auto convert text thành số.

**Chi tiết demo:** preview ưu tiên 12 hàng dữ liệu mẫu để thấy duplicate cuối file; với upload tùy ý có thể giới hạn `head(20)`. Dù upload mới, checkbox clean xử lý từ raw CSV được đọc lại; không nối/lưu dữ liệu giữa các nguồn. **CSV download luôn lấy `active_df`, không nhầm raw/cleaned.**

### 10.6. Ranh giới các lỗi & nghiên cứu sau
- R04: **DONE** — ddof=0, all-NaN, categorical NA, duplicate sau fill, rounding/UI, histogram 5 bins, density=False; xem §11.
- R05: version Streamlit/Python, file size limit hợp lý, decode/ParserError, CSV vô cột, dtypes lạ, kiểm thử chart, smoke UI.
- Không hỗ trợ general data cleaning pipeline, dữ liệu lớn, inference/AI, frontend phức tạp, sinh PDF từ app.
- Không thêm `st.data_editor` cho sửa bảng bằng tay: sẽ phát sinh state, điều kiện kiểm tra và code vượt phạm vi.

### 10.7. Evidence mapping theo chức năng
- `load_csv` / `inspect_data` → M01/M02; `clean_data` → M03; `numeric_stats`, `mean_by_group` → M04; `histogram`, `group_bar`, `scatter` → M05; `app.py` orchestration → M06/M07.
- Test unit (R05 thiết kế) gọi trực tiếp `analysis.py`, không cần khởi chạy Streamlit; chart tests gọi Figure constructors và kiểm tra type/labels.
- Đầu ra nộp bài F03–F06 vẫn nằm trong **giai đoạn sau**, **không** xây code xuất PDF/YouTube trong ứng dụng.

### 10.8. Nguồn chính thức
- https://docs.streamlit.io/develop/concepts/architecture/session-state — Streamlit rerun và session.
- https://docs.streamlit.io/develop/concepts/architecture/widget-behavior — widget value, identity, rerun.
- https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader — UploadedFile là BytesIO, cần rewind nếu đã đọc.
- https://docs.streamlit.io/develop/api-reference/charts/st.pyplot — yêu cầu truyền Figure rõ ràng.
- https://docs.streamlit.io/develop/api-reference/widgets/st.download_button — truyền dữ liệu download, có thể gây rerun.
- https://matplotlib.org/stable/api/figure_api.html — Figure trực tiếp và Figure.subplots.
- https://matplotlib.org/stable/users/interactive.html — pyplot giữ tham chiếu figure và cần close.
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html — cột số.
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html — bỏ index khi export.

**Các link xác minh được khả năng kỹ thuật, không xác minh code đang chạy.**


---

## 11. RESEARCH 04 — Mathematical correctness and data QA (2026-10-25)

**Scope:** independent arithmetic verification and specification decisions. This is NOT application code, test execution, or a claim that DataForge Mini runs. Verified arithmetic with temporary pandas 2.2.3 / NumPy 2.3.5 outside the repo, cross-checked using exact fractions and documentation. R05 designs tests and versions.

### 11.1. Canonical calculation oracle for dataset in §5

**Order is mandatory:** inspect raw → make a copy → `drop_duplicates(keep="first")` over all columns → take column-wise median among remaining rows → fill only missing numeric cells. Do not re-run deduplication after fill. Keep the original untouched.

| Metric | Raw | Cleaned |
|---|---:|---:|
| Rows / columns | 12 / 4 | 10 / 4 |
| Exact duplicates | 2 | 0 for canonical data |
| Missing numeric cells | 2 | 0 for canonical data |
| Valid `diem` observations | 11 | 10 |
| Score sum | 85 | 78 |
| Score mean | 85/11 ≈ 7.7272727273 | 78/10 = **7.8** |
| Score median / min / max | — | 8 / 6 / 10 |
| Mean hours | — | 4.4 |
| Group A, n/sum/mean | — | 5 / 40 / **8.0** |
| Group B, n/sum/mean | — | 5 / 38 / **7.6** |
| Scores ≥8 | — | 6 / 10 |
| Scatter valid (hours, score) pairs | 10 | 10 |

- Median fill values (computed **after removing duplicates**): `gio_hoc=4` and `diem=8`; specifically `Minh.gio_hoc=4` and `Ngoc.diem=8`.
- Exact cleaned grade sequence, original retained order: **8, 6, 9, 7, 10, 8, 7, 8, 6, 9**.
- Squared deviations from 7.8 sum to **15.6** = 78/5. Population variance is 15.6/10 = **1.56** = 39/25.
- **Population std** = sqrt(1.56) ≈ **1.24899959968** (`ddof=0`). **Sample std** = sqrt(15.6/9) ≈ **1.31656117721** (`ddof=1`) is only a comparison, NOT UI choice.
- Frequency grade 6:2; 7:2; 8:3; 9:2; 10:1. Raw complete scatter pairs 10 are NOT the same set of individual rows as the 10 cleaned pairs.

### 11.2. Mandatory statistical conventions

- **Choose population standard deviation (`ddof=0`)** to describe all valid observations in the currently displayed dataset. State the convention in video/PDF and UI.
- NumPy `np.std` defaults to ddof=0; Pandas `Series.std()` defaults to ddof=1. If implementation uses Pandas for comparison, explicitly pass `ddof=0`. Do not mix defaults.
- `numeric_stats` should select a valid numeric column with Pandas, discard missing values, and use **real NumPy calculations** for mean, median, min, max, std. Do not round before return, or compare floats with exact equality in tests.
- **0 valid numeric values:** result `count=0` and `mean/median/min/max/std=None`; UI says insufficient observations. Never display 0/NaN as computed mean or call unguarded NumPy reductions on empty arrays.
- **1 valid numeric value:** `count=1`, mean=median=min=max=this value, `std(ddof=0)=0`; histogram may render one observation.
- **n≥2 valid values:** compute statistics over nonmissing finite values; only format decimals when displaying (suggest 2 decimals). Tests use numeric tolerance.
- **Entire numeric column NaN:** median is undefined; clean leaves NA and UI reports remaining missing cells. No "everything cleaned" guarantee for arbitrary CSV.
- Numeric ±infinity is **different from missing**. For simplicity MVP declares numeric inputs containing ±∞ unsupported: show a clear error and stop the analysis rather than silently clipping, including infinity in median, or plotting wrong values. NA remains supported for cleaning. R05 decides exact location to implement this input guard.

### 11.3. Cleaning and duplicate subtleties

1. `duplicated` and `drop_duplicates` use *whole-row equality*, not repeated student names or index values; keep the first exact row. Do NOT manually test missingness by `value == np.nan`.
2. Median must be calculated on 10 deduplicated rows of the canonical fixture. Changing operation order can change the expected result on other inputs.
3. Do not mutate original `DataFrame`. Every checkbox rerun starts from raw, not previous cleaned table.
4. **Median imputation can CREATE duplicates**. Counterexample: rows `(X,1), (X,NA), (Y,1)` have 0 exact duplicates originally; median=1, so cleaned rows have duplicate `(X,1)`. After cleaning, report actual duplicate count; do NOT automatically drop again just to claim zero.
5. Because of #4, `clean_data(clean_data(df))` is **not guaranteed** equal to `clean_data(df)` for arbitrary input. Do not assert general idempotency in tests. Single-run-from-raw behavior is intentional.
6. Category/text missing values are **left missing**, not filled with mode/zero. GroupBy's default NA key handling excludes them; display that group keys with NA were excluded (rather than pretending they have group names).
7. For uploaded CSVs containing no numeric columns, display inspection and a message; omit numeric stats and incompatible charts; do not coerce text fields silently.

### 11.4. GroupBy correctness

- `mean_by_group(df, group_col, value_col)` requires a group/category column and a numeric value column. Use Pandas GroupBy mean while excluding NA keys by policy (`dropna=True`).
- Missing numeric *values* do not count in that group's mean; groups with zero valid values yield NaN, **not 0**. Do not plot such a group as a bar of height zero.
- If every group label is NA or no valid group mean exists: skip the bar with a clear message.
- Canonical fixture uses group A mean 40/5=8.0, B 38/5=7.6. Do not present their 0.4 gap as statistically significant or causal.

### 11.5. Matplotlib Figure semantics

**Histogram**: for one numeric Series after dropping missing values, choose `bins=5, density=False`; Y axis "Số quan sát"/"Tần suất", X actual column name. No percentile/normalized density. For cleaned grade values 6–10, five equal bins have edges [6, 6.8, 7.6, 8.4, 9.2, 10] and counts **[2, 2, 3, 2, 1]**, summing to 10. Last bin includes its right endpoint. A histogram groups intervals, not necessarily one bar per unique value. Skip if zero valid values.

**Group bar**: Figure consumes `mean_by_group` Series (no duplicate computations) and plots A=8.0, B=7.6; Y axis "Điểm trung bình" (NOT row count); **Y-axis starts at 0** to avoid visually exaggerated differences. Omit NA means, don't substitute 0.

**Scatter**: Figure consumes columns `x=gio_hoc` / `y=diem` by default; eliminate NA using **one joint two-column dropna**, not two independent dropped series; require distinct numeric columns and at least one complete pair. There are 10 valid pairs in canonical cleaned data (also 10 in raw but rows differ). Titles and axes must label units; overlapped points may exist. No regression line, correlation significance claim or inference of causality.

For any Figure: never draw made-up points for missing observations, and never use a plotted count different from the active DataFrame. R05 will define how to test labels and counts without generating app now.

### 11.6. ORACLE → future R05 test matrix

| ID | Input condition | Expected result |
|---|---|---|
| OR-01 | Canonical raw CSV spec | 12x4, 2 duplicates, 2 missing |
| OR-02 | Clean canonical CSV | 10x4, original unchanged, no remaining missing/duplicate |
| OR-03 | Individual fill | Minh hours 4, Ngoc grade 8 |
| OR-04 | Cleaned numeric statistics | count10, min6, max10, median8, mean7.8 |
| OR-05 | Population std | sqrt(1.56) ≈ 1.24899959968; ddof0 |
| OR-06 | A/B group means | n5 mean8.0 / n5 mean7.6 |
| OR-07 | Histogram | bins5, count [2,2,3,2,1], total10 |
| OR-08 | Scatter | raw10/clean10 paired points; no mismatch of rows |
| OR-09 | All-NaN numeric column | preserve missing; count0; all other stats None; skip numeric plots |
| OR-10 | Single numeric observation | population std0; mean equals value |
| OR-11 | Missing group name / all-NA value group | missing keys excluded; NaN group mean omitted from bar, NOT 0 |
| OR-12 | Duplicate created by median fill | actual duplicate count reports 1; no second cleanup |
| OR-13 | Numeric ±inf | unsupported input warning, do not plot/compute |
| OR-14 | No numeric or incompatible chart columns | skip functions/plot with clear message |
| OR-15 | Arbitrary clean_data called twice | no **global** idempotency assertion; Streamlit always calls from raw |

**Implementation status:** None of the OR-* are project tests yet. R05 designs the actual test suite, and only implementation may run tests and report pass/fail.

### 11.7. Evidence / official API references

- NumPy std/ddof https://numpy.org/doc/stable/reference/generated/numpy.std.html
- NumPy nanstd warnings https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html
- NumPy isfinite https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html
- Pandas sample std default https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html
- Pandas duplicate https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
- Pandas missing data https://pandas.pydata.org/docs/user_guide/missing_data.html
- Pandas GroupBy missing key handling https://pandas.pydata.org/docs/user_guide/groupby.html
- Matplotlib hist bins and density https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html

These are documentation references, not evidence that the project is implemented.


---

## 12. RESEARCH 05 — Testing, environment and reproducibility (2026-10-25)

**STATUS: QA SPEC DONE, NOT TESTED IN APP.** No Python application/source/fixtures/dependency files created. R05 researched release records and docs, designed test cases, and audited consistency. Exact package versions remain **candidate**, not integration-tested; P0 must resolve and verify before pins.

### 12.1. Runtime and dependency policy (candidate, no installation claim)

- Recommended Python: **CPython 3.13 x64 / arm64 as applicable**, **not** Python 3.15 merely because newest. Python 3.13 is supported; package PyPI classifiers include 3.13 for intended choices.
- Application's four **direct** dependencies only: `numpy`, `pandas`, `matplotlib`, `streamlit`. `pytest` is development/test-only; Python standard library is otherwise sufficient.
- Release references **as of 2026-10-25**: Python 3.13.17 (Oct 21); NumPy 2.5.4 (Oct 10); pandas 3.1.0 (Oct 22); Streamlit 1.66.1 (Oct 21); Matplotlib 3.11.x (release family); pytest 9.1.1 (Jun 19). These are **investigated release candidates**, **NOT an installed, proven compatible 5-package lockset**. Version of Matplotlib in implementation must be checked on PyPI when P0 runs. Never paste this paragraph as requirements.txt unchanged.
- Candidate **major-family bounds** for P0 evaluation: Python `>=3.13,<3.14`, NumPy `>=2.4,<3`, Pandas `>=3.0,<4`, Matplotlib `>=3.10,<4`, Streamlit `>=1.60,<2`, pytest `>=9,<10`. These are **selection constraints, not compatibility proof**; pip resolves transitive deps. R05 recommendation, not user/instructor mandate.
- At P0 install/test on the owner's actual OS/Python architecture, run `python -m pip check`, package import/version check, clean env smoke, tests, then pin **verified exact top-level versions** in `requirements.txt`. Avoid manual requirements from hypothetical compatibility; don't add Conda/Poetry/Docker/uv just for packaging.
- **Important Pandas 3.0 change:** inferred text columns use `str` dtype rather than `object`. Never use `dtype == "object"` alone or `select_dtypes(include="object")` alone to find `lop`. Select text/category with a compatible dtype predicate including string and object/category; guard against bool/datetime masquerading as groups. Verify with `sample_data.csv` parsed on chosen Pandas version.
- **Streamlit 1.62+ change:** `st.pyplot(fig)` requires explicit Figure; using `st.pyplot()` with no figure is not supported; custom `savefig` kwargs deprecated. Keep object-oriented Matplotlib contract of R03.
- Streamlit uploader has a large default max (200 MB historically); **project local upload policy: 2 MiB max** because all operations in memory and project intentionally small. Prefer a simple upload-size check (`uploaded_file.size`) plus user-facing message; if chosen Streamlit has a stable per-widget size option it can be used, but still verify semantics in P0. **This 2 MiB limit is unrelated to the teacher's PDF submission maximum of 100 MB.**
- No cloud/server deployment necessary for submission; run locally and capture YouTube video. No network access needed *while running* after dependencies have been installed.

### 12.2. Cross-platform setup procedure for implementation stage (DO NOT execute during research)

From clone root, Python 3.13 available and network available only for install.

Windows PowerShell:
\`\`\`powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pip install pytest
.venv\Scripts\python.exe -m pip check
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m streamlit run app.py
\`\`\`

macOS/Linux:
\`\`\`sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install pytest
.venv/bin/python -m pip check
.venv/bin/python -m pytest -q
.venv/bin/python -m streamlit run app.py
\`\`\`

- These are **future commands**, not evidence they have run; `requirements.txt`, tests and source don't exist during R05.
- Prefer invoking the venv's exact interpreter rather than relying on a shell activation or globally installed `streamlit`/`pytest`. `python -m pytest` and `python -m streamlit` ensure consistent interpreter.
- At P0 check `python --version` and record `python -m pip list` exact installed versions and host OS. Do a **fresh venv smoke check** after locking requirements and a second run from a different working directory if app sample lookup relies on `__file__`.
- If internet is absent before installation, cannot assume library wheels exist locally. Prepare dependency installation once while online, then verify app works offline.
- Do **not** create CI/Docker/GitHub Actions or a lock framework until a real blocker justifies them.

### 12.3. Minimal testing architecture

- **One test file** `tests/test_analysis.py` to hold data/unit/chart contract tests, if this remains readable; add `tests/test_charts.py` **only if** needed to separate Matplotlib assertions from numerical tests and justify during P2. No conftest/plugin/fixtures directory or CI required.
- Pure functions tested without Streamlit server. Use `io.StringIO`/`io.BytesIO` in tests to construct small input cases; **one** canonical dataset file `sample_data.csv` created only at P0. Do not litter repo with 10 physical malformed CSV files.
- `pytest.approx` (and `numpy.testing`/`pandas.testing` where useful) compares floats with tolerance, not direct equality. Compare DataFrames without mutation using Pandas testing helpers.
- Matplotlib tests should assert `Figure`, plot axes labels, histogram patch/bin counts, group bar heights and zero baseline, scatter point offsets/count. Avoid brittle image pixel snapshot comparisons.
- Manual UI smoke is mandatory after P3: these can complement, not replace, unit tests. Streamlit AppTest is an **optional** enhancement if it replaces manual repetitions without many lines of extra test code. It is not mandatory for a 1-page student app.
- In P0/P1... log test command, outcome, Python/package versions and commit SHA; **do not report "pass" if unavailable or skipped**.

### 12.4. OR-01..OR-15 executable test design (source oracle at `11; NOT executed)

| ID | How to construct / call in P1–P3 | Assertion and failure mode | Priority |
|---|---|---|---|
| OR-01 | `load_csv(sample_data.csv)`, `inspect_data` | shape 12x4, duplicates2, missing2; grade/hours parsed as numeric | P0 |
| OR-02 | `raw.copy(deep=True)`; `clean_data(raw)` | cleaned 10x4, no NA/duplicates **for canonical input**, raw deeply equal snapshot | P0 |
| OR-03 | Look up `ten=="Minh"` and `ten=="Ngoc"` post-clean | exact numeric values hours4, grade8 | P0 |
| OR-04 | `numeric_stats(clean,"diem")` | count10, min6/max10, mean7.8 median8; use approx on floats | P0 |
| OR-05 | Same stats | `std == approx(sqrt(1.56))`, **ddof=0**, not Pandas default ddof1 | P0 |
| OR-06 | `mean_by_group(clean,"lop","diem")` | A≈8.0, B≈7.6, each n=5 by separate Pandas group sizes | P0 |
| OR-07 | `histogram(clean,"diem")` | figure, axis labels, 5 bars/interval counts [2,2,3,2,1], total 10 | P0 |
| OR-08 | `scatter(raw,..)` and `scatter(clean,..)` | each 10 complete **paired** points; offsets match paired data, not independently filtered arrays | P0 |
| OR-09 | In-memory numeric column all NA, plus valid group | missing remains; stats count0, others None; no misleading histogram/bar | P0 |
| OR-10 | In-memory one numeric value | std0, mean/median/min/max that value | P0 |
| OR-11 | Text group NA; another group all NA numeric | group key NA excluded; bar omits NaN group mean and doesn't plot zero | P0 |
| OR-12 | `[("X",1),("X",None),("Y",1)]` | no duplicate before, 1 after fill; no second automatic drop | P0 |
| OR-13 | In-memory numeric ±inf with valid other values | input rejected gracefully with clear diagnostic; never figure rendered | P0 |
| OR-14 | DataFrame with no numeric, one numeric, no category | incompatible stats/plots prevented, valid parts remain; no fabricated cols | P0 |
| OR-15 | Call UI cleaning from same raw twice (two independent runs) | reproducible same cleaned view; **do not require** `clean_data(clean_data(df)) == clean_data(df)` for arbitrary datasets | P1 |

**P0/P1 in Priority column refers to test implementation urgency *after* coding is authorized, not to current R05 phase.** 

For OR-13 the source of error may be loader/UI or function guard, but API contracts must agree; avoid silently calling `np.nanmean` with inf.

### 12.5. Input/interaction QA supplement (small, no overengineering)

| ID | Case | Expected minimal UX behavior |
|---|---|---|
| IO-01 | Zero-byte CSV / whitespace-only file | `EmptyDataError` or equivalent caught; user-facing error, stop current render |
| IO-02 | Header-only CSV, 0 data rows | distinguish from no header; explain empty dataset, don't compute stats/charts |
| IO-03 | Malformed quotation / extra fields | `ParserError` or warning if Pandas detects problem; do not silently set `on_bad_lines="skip"`. Some ragged CSV with too few fields may be parsed as missing values: **do not promise all malformed CSVs are rejected by Pandas** |
| IO-04 | UTF-8 with BOM | read as expected (UTF-8-SIG or compatible), preserve column names |
| IO-05 | Invalid UTF-8 bytes | catch `UnicodeDecodeError`, tell user expected UTF-8 |
| IO-06 | Wrong delimiter (`;`), one-column CSV | report format incompatibility if needed; do not guess arbitrary delimiters silently |
| IO-07 | Empty/duplicate/unnamed column headers | require unambiguous header; do not imply renamed Pandas columns have same original meaning (P0 decide simplest guard) |
| IO-08 | Oversized upload >2 MiB | clear stop; does not affect teacher PDF 100MB limit |
| IO-09 | Numeric text values that Pandas infers as string | don't silently coerce; numeric features hidden/explained |
| IO-10 | CSV export raw vs cleaned | file round-trips to current `active_df` with exactly 4 columns in sample, **no extra index**, UTF-8-SIG works in common spreadsheet viewer |
| UI-01 | No upload | bundled sample selected from path relative to `app.py` |
| UI-02 | Upload another valid CSV | uploaded file replaces sample; no residual rows/data |
| UI-03 | Toggle raw → clean → raw | 12→10→12, raw not mutated, metrics and plots reflect same active view |
| UI-04 | Change numeric/group selections | no crashes or mismatched chart labels; invisible plots when inappropriate |
| UI-05 | Only one numeric / no text groups | histogram remains if possible; scatter or bar omitted with helpful note |
| UI-06 | Download before/after clean | currently shown data exported; check parse again and values |

**Validation policy (minimal):** Catch expected `pd.errors.EmptyDataError`, `pd.errors.ParserError`, `UnicodeDecodeError`, `OSError`, `ValueError` (including unsupported schema/inf) and show understandable messages. Do not use broad `except Exception: pass` and do not print a traceback to user. Keep errors localized, not an error-handling framework. Some Pandas malformed inputs may parse with warnings or implicit NA; **test against actual selected Pandas version**.

**Additional Pandas 3.x regression:** `lop` text/category detection must work when dtype is `str`, not merely legacy `object`. Add explicit assertion to OR-01 or IO-09. This is confirmed in pandas 3.0 official migration docs.

### 12.6. Acceptance gates at the end of implementation (future)

**STOP / NO SUBMISSION** if:
1. App crashes on canonical sample or doesn't show correct 12→10 profile;
2. NumPy/Pandas/Matplotlib not actually used in executed workflow;
3. Wrong mean/std/group/histogram/scatter pairing;
4. Imported CSV secretly rewritten or silently discarded;
5. Report/video describe unimplemented functionality or wrong numbers;
6. Source GitHub link inaccessible to teacher; YouTube link cannot be viewed; PDF not 15–20 pages or >100MB; self-assessment incomplete.

**P0–P4 completion evidence record:** commit SHA, exact Python and 4 library versions, `python -m pip check` result, `python -m pytest -q` pass/fail counts, GUI smoke checklist, sample CSV hash/check and screenshots from correct build, PDF pages/bytes, accessibility of links. Treat skipped/unrun tests as unverified.

### 12.7. Evidence / primary sources checked for R05

- Python supported releases: https://www.python.org/downloads/
- PyPI Python requirements / release candidates: https://pypi.org/project/numpy/ ; https://pypi.org/project/pandas/ ; https://pypi.org/project/matplotlib/ ; https://pypi.org/project/streamlit/ ; https://pypi.org/project/pytest/
- Pandas 3.0 string dtype change: https://pandas.pydata.org/docs/whatsnew/v3.0.0.html and https://pandas.pydata.org/docs/user_guide/migration-3-strings.html
- Pandas read_csv & parsing: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html ; https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html ; https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html
- Streamlit releases and `st.pyplot(fig)`: https://docs.streamlit.io/develop/quick-reference/release-notes/2026 ; https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
- Streamlit upload/download and limits: https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader ; https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
- pytest approximate: https://docs.pytest.org/en/stable/how-to/assert.html
- Streamlit AppTest (optional): https://docs.streamlit.io/develop/concepts/app-testing/get-started
- Python virtual environments: https://docs.python.org/3/library/venv.html

**Knowledge boundary:** These URLs verify APIs/releases and constrain the *plan*, NOT proof the specific package combination installs/runs or the app passes tests. As packages change, verify again in P0.

# PROJECT SPEC — DataForge Mini, MVP research baseline (R02)

**Trạng thái:** Research 03/07 hoàn thành; **MVP + ARCHITECTURE DESIGN BASELINE**, chưa phải code/final approval. R03 đã khóa sơ đồ module/hợp đồng hàm; R04 kiểm định toán; R05 test; R06 đồ án nộp bài; R07 handoff; FINAL mới có thể đạt READY FOR IMPLEMENTATION.

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
- Thống kê `std` phải ghi rõ **ddof=0 hay ddof=1**, không trộn NumPy/Pandas mặc định; R04 sẽ khóa.

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
- R04: ddof chuẩn, tính không thiếu của các cột, xử lý NaN/all-NaN, binned histogram, interpretation; xác minh lại expected values.
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
- R04: chọn chính xác `ddof`; all-NaN, categorical NaN, duplicate sau median fill, cách làm tròn; định nghĩa bins, percent? (không thêm nếu không cần).
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

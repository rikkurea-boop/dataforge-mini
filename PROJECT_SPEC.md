# PROJECT_SPEC — DataForge Mini (Active implementation specification)

**Trạng thái:** SPEC ĐÃ TỔNG HỢP R01–R07; **FINAL cross-QA chưa chạy**, **chưa có mã nguồn ứng dụng**. Chỉ mô tả hành vi mà một ứng dụng tối giản phải thực hiện **sau khi được phép bắt đầu**. Lịch sử các research R01–R06 nằm trong git commits của PR #1; không cần sao chép nhật ký nghiên cứu vào spec hiện hành.

**Tên đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Môn/chủ đề:** Chương 5.5, NumPy – Pandas – Matplotlib.  
**Quyết định của user:** DataForge Mini tách khỏi Data-Forge gốc, nhỏ và tự giải thích được toàn bộ code.  
**Yêu cầu thầy có bằng chứng:** ở [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md); **PDF/video là bài nộp bên ngoài app**, xem [docs/DELIVERABLES.md](docs/DELIVERABLES.md).

## 1. Bài toán và chức năng MVP

Một ứng dụng Streamlit **một trang**, dùng **một bộ CSV giả lập có lỗi chủ đích**, hiển thị dữ liệu, làm sạch, tính thống kê và tạo biểu đồ. **Đây là lựa chọn thiết kế để trình bày mục 5.5, không phải chi tiết giảng viên đã quy định.**

| ID | Chức năng tối thiểu | Cơ sở kỹ thuật | Chứng minh khi app tồn tại |
|---|---|---|---|
| **M01** | Đọc file CSV người dùng tải lên hoặc dùng dataset tích hợp | Pandas | Thấy đúng bảng gốc và kích thước |
| **M02** | Xem bảng, hàng/cột, missing cells và duplicate rows | Pandas | Sample 12×4, 2 missing, 2 exact duplicate |
| **M03** | Một công tắc clean: drop whole-row duplicates rồi median-fill numeric | Pandas | Sample còn 10×4, 0 missing/dup; raw vẫn nguyên |
| **M04** | Numeric count/min/max/mean/median/population std và mean theo nhóm | NumPy + Pandas GroupBy | Mean điểm 7.8, std≈1.249, A8.0/B7.6 |
| **M05** | Ba Matplotlib Figure: histogram, bar group means, paired scatter | Matplotlib | Chart đúng số liệu, title/trục |
| **M06** | Tải CSV của bảng đang xem (raw hoặc clean) | Pandas + Streamlit | Roundtrip không thêm index |
| **M07** | Một trang UI với tối đa 3 ô chọn cột và một checkbox clean | Streamlit | Demo liền mạch không điều hướng phức tạp |

**Không làm:** Excel, multi-page dashboard, ML/prediction, AI chatbot, database, login, API/backend, cloud/deployment, PCA, cache/session-state tùy biến, Undo/Redo, pipeline framework, chart editor, sinh báo cáo PDF trong app, lấy code từ Data-Forge gốc.

## 2. Bộ dữ liệu chuẩn duy nhất

**Tên file dự kiến:** `sample_data.csv` — **chưa tạo ở giai đoạn research**. CSV UTF-8 có 4 cột `ten,lop,gio_hoc,diem`, tổng hợp hoàn toàn, không chứa thông tin cá nhân thật.

~~~csv
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
~~~

**Quy tắc làm sạch chuẩn:** sao chép raw → `drop_duplicates(keep="first")` xét **toàn dòng** → trên 10 dòng còn lại tính median **từng cột numeric** từ giá trị hợp lệ → chỉ điền NA numeric, giữ nguyên cột text/nhãn nhóm. **Không drop lần hai.**

| Oracle toán | Raw | Sau clean |
|---|---:|---:|
| Rows/columns | 12/4 | **10/4** |
| Exact duplicates | 2 | **0** (riêng sample chuẩn) |
| Missing numeric cells | 2 | **0** (riêng sample chuẩn) |
| Valid grade observations | 11 | 10 |
| Sum grade | **85** | **78** |
| Mean grade | 85/11≈7.7272727 | **7.8** |
| Median(hours), median(grade) dùng fill | — | **4**, **8** |
| Cụ thể giá trị được điền | — | **Minh.gio_hoc=4**, **Ngoc.diem=8** |
| Grade min / max / median | — | **6 / 10 / 8** |
| Population variance / std `ddof=0` | — | **1.56 / √1.56≈1.24899959968** |
| Group A mean / group B mean | — | **8.0** (5 hàng) / **7.6** (5 hàng) |
| Hours mean; scores ≥8 | — | **4.4**; **6/10** |
| Valid scatter pairs `gio_hoc` and `diem` | **10** | **10** |

**Clean grade sequence theo thứ tự:** 8, 6, 9, 7, 10, 8, 7, 8, 6, 9.  
**Grade frequency:** 6→2, 7→2, 8→3, 9→2, 10→1.  
**Histogram `bins=5`, `density=False`:** bin edges [6,6.8,7.6,8.4,9.2,10], counts [2,2,3,2,1], tổng 10; bin cuối bao gồm điểm cực đại.

**Status của oracle:** phép tính đã được kiểm tra độc lập ở R04 bằng tính toán tạm; **không phải kết quả test ứng dụng**. Khi có code, so sánh bằng `pytest.approx`, không yêu cầu bằng tuyệt đối các số thực.

## 3. Kiến trúc ứng dụng cực gọn

~~~text
sample_data.csv hoặc UploadedFile → app.py (Streamlit)
                                     ├── analysis.py (Pandas + NumPy) → DataFrame/Series/stats
                                     └── charts.py (Matplotlib Figure) ← DataFrame/Series
                                     └── st.pyplot(fig), st.download_button
~~~

**Đúng ba file Python chính:** `app.py` UI/điều phối; `analysis.py` đọc-clean-stats; `charts.py` ba loại Figure. `tests/test_analysis.py` là file kiểm thử, không tính là source app. Không dùng `src/` hoặc hierarchy nhiều lớp.

### 3.1. Hợp đồng 5 hàm analysis.py

| API đề xuất | Input → output | Điều kiện và hành vi bắt buộc |
|---|---|---|
| `load_csv(source: str \| Path \| BinaryIO) -> pd.DataFrame` | File path mẫu hoặc file-like uploaded → DataFrame mới | `pd.read_csv`, mặc định CSV UTF-8 dấu phẩy. Reset stream pointer khi cần. Reject file rỗng/header-only, parse/encoding errors, numeric infinity với thông báo thân thiện; không tự bỏ row hoặc convert text không cần |
| `inspect_data(df) -> dict[str,int]` | DataFrame → `rows, columns, missing_cells, duplicate_rows` | Dùng `shape/isna/duplicated`, whole-row duplicate, không mutate, không tự đổi tên cột |
| `clean_data(df) -> pd.DataFrame` | Raw → cleaned **bản mới** | Copy trước; dedup-first→median numeric; không drop lần 2. Nếu cột numeric all-NA thì giữ NA và báo số missing còn lại; text/group NA không fill. Khi fill tạo duplicate mới phải báo số thật |
| `numeric_stats(df, column) -> dict` | Cột numeric → `count,min,max,mean,median,std` Python scalars/None | Loại NaN, NumPy thực sự tính toán; `ddof=0`; count0 → các chỉ số khác None, count1 → std0. Không làm tròn phép tính; missing/invalid column báo lỗi phù hợp |
| `mean_by_group(df, group_column, value_column) -> pd.Series` | Cột text/category và cột numeric → mean theo nhóm | Pandas GroupBy (missing group key bị loại theo policy); group không có số hợp lệ cho NaN (không phải zero). Không âm thầm đổi text sang number |

**Một trách nhiệm quan trọng:** bên xử lý dữ liệu phải xác định chặn numeric ±∞ trước khi tính median/stats/group, kể cả khi người dùng đưa DataFrame trực tiếp vào hàm chứ không qua upload. R05 đã đặt input guard nhưng **chưa có code**. Việc nào guard ở loader và việc nào ở hàm sẽ quyết ở lúc cài đặt sao cho không lặp quá nhiều.

**Pandas 3.x:** text có thể mang dtype `str` thay vì `object`; bộ chọn nhóm phải nhận cả string/object/category hợp lệ, không chỉ `include="object"`. **Cách tương thích pandas 2.x/3.x được tài liệu Pandas khuyến nghị:** `df.select_dtypes(include=["object", "string", "category"])` (sau đó chỉ giữ cột nhóm hợp lệ). Không dùng `include=["str"]` trên pandas 2.x. Với CSV tùy ý có tên header bị thay đổi/không hợp lệ phải báo lỗi, không giả định có `lop`.

### 3.2. Hợp đồng 3 hàm charts.py

| API đề xuất | Input → Figure | Kiểm đúng |
|---|---|---|
| `histogram(df, column)` | Numeric Series sau bỏ NA → `matplotlib.figure.Figure` | `ax.hist(values,bins=5,density=False)`; Y="Số quan sát", có X/title; ẩn khi không có số |
| `group_bar(means: pd.Series)` | GroupBy mean Series → Figure | Plot A=8/B=7.6, loại NA means, **Y bắt đầu 0**, Y="Trung bình" (không ghi số lượng) |
| `scatter(df, x_column, y_column)` | Hai cột numeric khác nhau → Figure | Dùng `df[[x,y]].dropna()` **theo hàng/cặp**; nếu 0 cặp thì ẩn; không drop riêng/sắp xếp hai trục |

Dùng `Figure(figsize=...)` → `ax=fig.subplots()` rồi `st.pyplot(fig)`. Tránh `plt.show()`, `plt.gcf()`, pyplot toàn cục, 10+ biểu đồ hoặc vẽ đường dự đoán. Trục/tên biểu đồ dễ đọc, biểu diễn đúng dữ liệu **active_df**.

### 3.3. Luồng UI một trang

1. Chọn uploaded CSV nếu có, không có thì mở `sample_data.csv` theo đường dẫn cạnh `app.py` (không phụ thuộc current working directory).
2. Kiểm file format/size **≤2 MiB** và input error, cho hiển thị profile và preview raw.
3. Một checkbox **Làm sạch dữ liệu**: `active_df = clean_data(raw_df)` nếu bật, ngược lại raw; khi widget thay đổi Streamlit rerun, **luôn bắt đầu từ raw**.
4. Hiển thị before/after row/NA/duplicate **bằng số thật**, không mặc định mọi file sạch 100%.
5. Tối đa **3 selectbox**: cột numeric Y/stats (mặc định `diem`), nhóm text/category (mặc định `lop`), numeric X khác Y (mặc định `gio_hoc`). Ẩn tùy chọn không hợp lệ.
6. Hiển thị NumPy stats, GroupBy mean, 3 Figure phù hợp; nếu dữ liệu không có category hoặc <2 cột số, bỏ chart thiếu điều kiện và giải thích.
7. `st.download_button` xuất `active_df.to_csv(index=False).encode("utf-8-sig")`; file tải phải đọc lại đúng rows/cols, không thêm index.

**Không cần `st.session_state`, callbacks, memo/cache** cho dataset nhỏ; không tạo class UI hay trang settings.

## 4. Độ chính xác dữ liệu và trường hợp khó

- **Numeric NA vs ±∞:** NaN là thiếu và có thể điền median; ±∞ không phải giá trị hợp lệ của MVP → báo lỗi/dừng phân tích. Guard `np.isfinite` phải phân biệt NaN để không cấm dataset mẫu.
- **All-NA numeric:** không có median. Giữ nguyên NA, `count=0` và `mean/median/min/max/std=None`. Không gọi NumPy reduce rỗng không guard.
- **Singleton numeric:** n=1 → std tổng thể **0**. Với n≥1, tính float đầy đủ; chỉ làm tròn khi hiển thị, không trong logic.
- **Imputation sinh duplicate:** nếu raw có (X,1), (X,NA), (Y,1), sau fill median1 thành duplicate (X,1), **không drop lần hai**, báo số duplicate mới. Không giả định clean_data idempotent cho mọi CSV.
- **Group NA:** `groupby(...,dropna=True)` bỏ row có nhãn nhóm NA. Nhóm không có giá trị numeric hợp lệ phải bị loại khỏi bar chứ không vẽ mean0. Nếu không còn nhóm hợp lệ, ẩn bar.
- **CSV text-like numeric:** không tự ép "8a" thành số, không tạo cột giả. Các cột không hợp lệ bị loại khỏi selector, hiện thông báo.
- **Histogram khác bar:** histogram là tần suất trong khoảng liên tục, bar là mean từng nhóm. Không gọi histogram là "điểm trung bình" và không kết luận nhân quả từ scatter.
- **Parsing:** Pandas có thể xử lý hàng ngắn bằng NaN và có thể tự đổi tên header trùng; không hứa mọi CSV sai cấu trúc đều bị reject. Không đặt `on_bad_lines="skip"` để âm thầm bỏ dữ liệu. Với header trùng, cần xác minh trực tiếp trước khi Pandas đổi tên nếu cam kết thông báo lỗi.
- **Scope:** CSV UTF-8 phân cách dấu phẩy, nhỏ; không cam kết dữ liệu rất lớn, encoding bất kỳ, JSON/Excel hoặc chart có datetime.

## 5. Oracle tests — đặc tả cho R05/P1–P4, CHƯA CHẠY

Các ID là **test behaviors**, không bắt buộc 31 hàm test riêng biệt. Dùng 1 file `tests/test_analysis.py`, in-memory `StringIO/BytesIO` để tạo edge cases; thêm file test chart khi thật sự cần để dễ đọc. Kết quả số dùng gần đúng (pytest.approx). Matplotlib test inspect Figure/axes/patch/offsets chứ không snapshot pixel.

### 5.1. OR-01..OR-15: logic/stat/figure

| ID | Dữ liệu | Expected |
|---|---|---|
| OR-01 | Canonical raw CSV `2 | 12×4, 2 duplicate, 2 missing; nhận cột grade/hours numeric và `lop` string/category |
| OR-02 | Clean canonical; giữ snapshot raw | 10×4, 0 missing/duplicate; raw bằng snapshot |
| OR-03 | Hai ô thiếu | Minh.hours=4, Ngoc.grade=8 |
| OR-04 | Stats grade clean | count10, min6, max10, mean7.8, median8 |
| OR-05 | Std grade clean | √1.56≈1.24899959968, **ddof0**, không phải Pandas mặc định |
| OR-06 | GroupBy A/B clean | A mean8.0 n5; B mean7.6 n5 |
| OR-07 | Histogram grade clean | 5 bins, count [2,2,3,2,1], total10 và nhãn đúng |
| OR-08 | Scatter raw/clean | mỗi bảng 10 **cặp hợp lệ**; không tráo hàng X/Y |
| OR-09 | Numeric all-NaN | giữ NA, count0, số khác None, không vẽ hist sai |
| OR-10 | Numeric 1 giá trị | std0 và mean=median=min=max=giá trị |
| OR-11 | Nhóm text NA / nhóm không có value | NA key bị loại; NaN mean không thay bằng 0 |
| OR-12 | Duplicate tạo bởi median fill | còn duplicate sau fill và được báo; không drop lần hai |
| OR-13 | Numeric +∞/−∞ | Reject rõ, không compute/plot |
| OR-14 | Không có numeric / thiếu nhóm / 1 numeric | Ẩn stats/plots không khả dụng, chức năng còn lại tiếp tục |
| OR-15 | Checkbox làm sạch chạy lại từ raw | Cùng raw luôn ra cùng cleaned; **không yêu cầu** clean_data(clean_data(df)) bằng clean_data(df) cho mọi input |

### 5.2. IO-01..IO-10: input/export

| ID | Input | Expected |
|---|---|---|
| IO-01 | Empty/whitespace-only CSV | Thông báo file không có dữ liệu; không crash UI |
| IO-02 | Chỉ có header, zero rows | Thông báo dataset không có row; không stats/chart |
| IO-03 | Quoting lỗi, trường extra, record không đều | Lỗi ParserError khi Pandas phát hiện; **không hứa** mọi ragged CSV đều lỗi |
| IO-04 | UTF-8 BOM | Đọc đúng header, không xuất hiện BOM trong tên cột |
| IO-05 | Bytes UTF-8 lỗi | UnicodeDecodeError thành thông báo rõ |
| IO-06 | Dấu phân cách `;` thay dấu phẩy | Báo format unsupported nếu tạo một cột không hợp lý, không tự guess engine |
| IO-07 | Header trống/trùng/không rõ | Pandas có thể tự đổi tên cột trùng khi parse; loader phải phát hiện/từ chối header nhập nhằng **trước khi tự đổi tên**, hoặc không tuyên bố đã phát hiện. Có thể dùng `csv.reader` của Python cho một dòng header, không thêm package |
| IO-08 | Uploaded size > **2 MiB** | Chặn có thông báo (khác PDF 100MB thầy) |
| IO-09 | Numeric-like text không parsed là numeric | Không tự ép; ẩn feature phù hợp và giải thích |
| IO-10 | Download CSV raw/clean | Roundtrip đúng `active_df`, index=False, UTF-8-SIG |

### 5.3. UI-01..UI-06: manual app smoke

| ID | Thao tác | Expected |
|---|---|---|
| UI-01 | Không upload | Tự đọc sample cạnh app.py |
| UI-02 | Upload CSV khác | Dùng dataset mới, không còn số liệu/file cũ |
| UI-03 | Toggle raw→clean→raw | Sample 12→10→12 và biểu đồ/profile đồng bộ |
| UI-04 | Đổi group/Y/X cột | Chart labels/values đúng, không crash; plot invalid ẩn |
| UI-05 | Chỉ một numeric hoặc không có text groups | Chỉ hiện plots hợp lệ |
| UI-06 | Download trong hai trạng thái | CSV xuất đúng raw hoặc cleaned đang xem |

### 5.4. Error and verification policy
Chỉ bắt những lỗi dự kiến: Pandas `EmptyDataError`/`ParserError`, `UnicodeDecodeError`, `OSError`, `ValueError` cho dtype/size/inf. `st.error` và dừng luồng bị lỗi; **không** `except Exception: pass`. Cần kiểm thử cặp raw/clean ở UI. Tests phải cung cấp command, actual pass/fail/skip và SHA; **không tạo báo cáo test giả**.

## 6. Môi trường và khả năng tái lập — đề xuất, chưa tích hợp

- Target: **CPython 3.13** (khuyến nghị cho bài học, không phải yêu cầu thầy).
- Dependencies direct: `numpy`, `pandas`, `matplotlib`, `streamlit`. `pytest` dev/test-only. **Không khóa bản chính xác trong nghiên cứu**; R05 đã đọc thông tin release nhưng compatibility nhiều package chưa kiểm bằng cài đặt thật.
- P0 phải tạo venv trên máy owner, cài tổ hợp tương thích, kiểm `python -m pip check`, import tất cả thư viện và smoke; **sau đó** ghi chính xác versions thật vào `requirements.txt`. Không copy các version giả định trong lịch sử R05.
- Dùng `python -m pytest -q`; Windows có thể gọi `.venv\Scripts\python.exe`, macOS/Linux gọi `.venv/bin/python`; chạy app bằng `python -m streamlit run app.py` với đúng venv.
- Ghi runtime/OS/versions/command/exit result. Thực thi app offline **sau khi dependencies đã được cài sẵn**; không suy ra pip install làm việc nếu chưa có network/wheels.
- Không cần Docker, Conda, CI hay Playwright trừ khi có blocker đã chứng minh và owner đồng ý.

## 7. Gate sau triển khai — tránh nhầm nghiên cứu với sản phẩm

- **Đang research:** chỉ specs, no app/test/figures/evidence.
- **Khi làm P0–P4:** mỗi task có tiêu chí, file scope trong `docs/PLAN.md`; phải ghi evidence thực vào STATUS.
- **Chỉ khi code hoàn thành:** GitHub link thật, demo YouTube thật, PDF 15–20 trang ≤100MB, tự chấm 5 tiêu chí theo `docs/DELIVERABLES.md`; không lấy hình từ oracle tạm làm screenshot app.
- **Block release** nếu app crash với sample, NumPy/Pandas/Matplotlib chỉ import mà không chạy, sai dataset/std/group/plots, test trọng yếu fail, link không truy cập được hoặc báo cáo/video bịa kết quả.

## 8. Tài liệu và nguồn gốc
- Yêu cầu giảng viên/hồ sơ nguồn: [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md).
- Quy tắc và quyền: [RULEBOOK.md](RULEBOOK.md), [AGENTS.md](AGENTS.md).
- Nhiệm vụ P0–P4: [docs/PLAN.md](docs/PLAN.md).
- PDF/YouTube/EV evidence: [docs/DELIVERABLES.md](docs/DELIVERABLES.md).
- Diễn biến lịch sử R01–R06: git commits trong PR #1. Các nguồn API Pandas/NumPy/Matplotlib/Streamlit và tài liệu academic/YouTube được phân loại trong REQUIREMENTS / DELIVERABLES.

# DELIVERABLES — Kế hoạch nộp bài DataForge Mini (Research 06)

**Trạng thái:** R06 chuẩn bị và kiểm định hồ sơ nộp bài; **chưa tạo ứng dụng, PDF, video YouTube hoặc bằng chứng chạy thực tế**. Chỉ được sản xuất sau R07, FINAL và lệnh triển khai của chủ dự án.

**Tên đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.  
**Học phần:** Chương 5.5 — NumPy, Pandas, Matplotlib.  
**Nguyên tắc:** Tối giản, giải thích được toàn bộ code, không phát triển thêm chức năng để lấp trang.

## 1. Các đầu ra phải nộp — từ hai ảnh biểu mẫu của thầy

| ID | Bắt buộc | Chứng cứ nghiệm thu |
|---|---|---|
| F02 | Kiểm tra thông tin cá nhân ở form | Chính sinh viên kiểm tra; **không đưa MSSV, email hay dữ liệu riêng tư lên GitHub** |
| F03 | Link mã nguồn GitHub hoặc nền tảng tương đương | URL đúng code/commit hoàn thành, thầy **xem được** |
| F04 | Link YouTube demo sản phẩm | URL video watch mở được, video trình diễn code/app thật |
| F05 | Một PDF **15–20 trang, tối đa 100 MB** | File cuối mở được, số trang vật lý và dung lượng được kiểm tra |
| F06 | Tự nhận xét và tự chấm theo năm tiêu chí | Lập luận, ưu/nhược và điểm 3+2+2+1+2, tổng tối đa 10 |

**UNKNOWN:** hạn nộp, thời lượng video bắt buộc, PPT có bắt buộc không, template/font/margin và cách thầy tính phụ lục, các trường khác ngoài vùng ảnh. Không suy diễn "không bắt buộc" từ việc không thấy trên ảnh.

**Phân biệt quan trọng:** Thầy yêu cầu **báo cáo PDF bên ngoài app**; **không yêu cầu app tự xuất PDF**. Không thêm PDF generator vào DataForge Mini.

## 2. Đề cương PDF 18 trang — mục tiêu thiết kế, không phải quy định của thầy

Đề xuất **18 trang vật lý**, có bìa và mục lục nằm trong 18 trang. Cho phép chỉnh trong **15–20** nếu nội dung thực khác kỳ vọng. Nội dung phải theo thứ tự **vấn đề → phương pháp → kết quả → kiểm thử → giới hạn**.

| Trang | Nội dung & câu hỏi cần trả lời | Evidence dự kiến |
|---|---|---|
| **01** | **Bìa**: tên đề tài, học phần và thông tin người nộp chỉ trong bản nộp phù hợp; không commit thông tin cá nhân | F02 |
| **02** | **Tóm tắt + mục lục**: mục đích, cách làm, kết quả (chỉ viết kết quả khi app đã chạy); mục lục đúng trang | — |
| **03** | **Bài toán, mục tiêu, phạm vi**: CSV dạng bảng; tại sao xử lý, tính và vẽ; không làm ML/database | M01–M07 |
| **04** | **Thư viện sử dụng**: bảng so sánh Pandas (data), NumPy (thống kê), Matplotlib (Figure), Streamlit (UI) | — |
| **05** | **Dataset**: bảng giả lập 12×4, diễn giải cột ten/lop/gio_hoc/diem, hai dòng trùng và hai ô thiếu; không phải thông tin học sinh thật | EV-03 |
| **06** | **Khám phá dữ liệu**: upload/default, preview, shape, duplicated, isna, trạng thái gốc 12/2/2 | EV-03 |
| **07** | **Làm sạch dữ liệu**: copy raw, bỏ trùng exact whole-row trước, median numeric fill sau, ranh giới all-NA | EV-04/05 |
| **08** | **Kết quả làm sạch**: 12→10, 2 NA→0 cho sample, Minh giờ học 4/Ngoc điểm 8; mô tả ý nghĩa giả lập | EV-04/05 |
| **09** | **Thống kê NumPy**: count, mean, median, min/max, độ lệch chuẩn tổng thể **ddof=0**, công thức chỉ vừa đủ | EV-06 |
| **10** | **Pandas GroupBy**: mean điểm 7.8, A=8.0/B=7.6, mean giờ học 4.4, so với expected values | EV-06 |
| **11** | **Histogram Matplotlib**: năm bins, tần suất [2,2,3,2,1] và chú thích y=tần suất, không phải phần trăm | EV-07 |
| **12** | **Bar mean**: điểm TB A8/B7.6, trục tung bắt đầu từ 0, không suy luận kiểm định thống kê | EV-08 |
| **13** | **Scatter**: X giờ học/Y điểm, ghép các cặp cùng hàng; không kết luận nhân quả | EV-09 |
| **14** | **Kiến trúc ba file**: app.py UI, analysis.py data/stats, charts.py Matplotlib Figure; import một chiều; môi trường | EV-01/02 |
| **15** | **Luồng xử lý code**: tên/vai trò năm analysis functions + ba chart functions, checkbox raw/clean, xuất CSV; trích code NGẮN | EV-10 |
| **16** | **Kiểm thử/độ ổn định**: kết quả pytest THỰC, bản QA OR/IO/UI, kiểm lỗi đầu vào, platform, versions và commit | EV-11/12 |
| **17** | **Đánh giá trung thực**: ưu điểm, hạn chế, phần nào chưa hỗ trợ, tự chấm năm tiêu chí dựa trên evidence | EV-13 |
| **18** | **Kết luận, tài liệu tham khảo, link GitHub/YouTube**: chỉ link thật và nguồn đã đọc/trích | EV-01/15/16 |

**Nguyên tắc dàn trang:**
- Mỗi ảnh có số hình/caption và được nhắc đến trong đoạn văn; bảng có tiêu đề, số liệu khớp app/commit.
- Hình phải gần đoạn giải thích; tránh một mình tiêu đề nằm cuối trang hoặc **bảng bị chia đôi** vô lý.
- Không sao chép toàn bộ source code, không dùng lịch sử Python để lấp trang, không đưa screenshots trùng nhau thành nhiều trang.
- Kết luận và tự chấm dựa trên **kết quả chạy**, không được coi expected oracle R04 là evidence app đã pass.
- Nếu bản nháp ra 15–17 hoặc 19–20 trang và thông tin đầy đủ thì vẫn hợp lệ; **không ép đúng 18**. Nếu >20, cắt lặp và ảnh không giá trị; nếu <15, tăng chiều sâu giải thích kết quả/kiểm thử thật, không thêm tính năng.
- **Bìa/mục lục/phụ lục trong file đều tính vào số trang vật lý** cho tới khi có hướng dẫn đếm trang khác từ giảng viên.
- Giữ định dạng trích dẫn nhất quán; chưa có căn cứ thầy bắt APA hay IEEE, **không áp đặt style**.

### 2.1. PDF Production & Print QA — chỉ thực hiện ở P4
1. Soạn từ **nguồn có thể chỉnh sửa** nếu phù hợp (DOCX, Markdown, v.v.), xuất ra PDF. Không bắt người học phải dùng một công cụ cụ thể khi form chỉ yêu cầu PDF.
2. Kiểm **số trang vật lý 15–20** và file PDF **≤100 MB**; file mở được, chữ tiếng Việt/ký hiệu toán không mất.
3. **Render toàn bộ trang** để xem ảnh, bảng, dòng đầu/cuối, mục lục, header/footer; không chỉ kiểm vài trang đầu.
4. Nhấp thử link GitHub/YouTube trong PDF, bảo đảm công khai/quyền xem đúng; không có URL giả.
5. Đối chiếu mỗi số liệu và biểu đồ với EV thực của cùng bản build; kiểm tên đề tài và mục lục.
6. Nếu xuất bản PDF sau khi quay video, xác nhận không thay đổi logic/dataset trong phiên bản video.

## 3. Video YouTube — storyboard khoảng 7 phút (**6–8 phút là khuyến nghị**)

Chưa biết video phải dài bao lâu theo thầy. Mục tiêu là **quay live demo thật, dễ hiểu, không cần facecam/nhạc**; có thể rút nếu cần.

| Mốc tham khảo | Hình ảnh/hành động | Nội dung thuyết minh & kiểm chứng |
|---|---|---|
| 00:00–00:25 | Tiêu đề/app | Tên đề tài, vai trò ba thư viện |
| 00:25–01:05 | Repo/terminal | Cấu trúc ba file và cách chạy, phiên bản thực tế |
| 01:05–01:45 | Bảng dữ liệu gốc | 12 rows, 2 duplicate, 2 missing |
| 01:45–02:35 | Công tắc làm sạch | 12→10, median=4/8, Minh/Ngoc; raw được giữ |
| 02:35–03:25 | Phần thống kê | Điểm TB 7.8, A8/B7.6, std(ddof0) ≈1.249 |
| 03:25–04:35 | Ba biểu đồ thật | Histogram, bar, scatter; cách đọc nhãn/trục |
| 04:35–05:15 | Download CSV | Xuất đúng active table, không extra index |
| 05:15–06:30 | IDE và test | Đọc ngắn vai trò năm+ba hàm, hiển thị kết quả test nếu ĐÃ PASS THẬT |
| 06:30–07:00 | App và lời kết | Giới hạn CSV nhỏ/dữ liệu giả lập và kết quả đạt được |

**Kỹ thuật gợi ý, không phải quy định thầy:** màn hình 1920×1080, 16:9, 30 fps, MP4/H.264 + AAC; zoom code đủ lớn để đọc ở 720p, quay theo một build/commit đã khóa, không pha screenshots các build khác nhau. Không cần quay 4K hoặc thêm animation.

**YouTube link QA (theo tài liệu chính thức):**
- **Unlisted** (Không công khai) có thể mở và bị chia sẻ lại bởi bất kỳ ai có URL; **Private** cần cấp quyền cụ thể, chỉ gửi link có thể không xem được.
- YouTube có thể xử lý SD trước HD, nên phải kiểm video phát được và chữ đủ nét ở watch page trước khi dán URL vào form.
- Sử dụng link **watch video**, không phải đường dẫn quản trị YouTube Studio; tiêu đề/video phải khớp app và PDF.
- Trước khi quay, đóng email/tab nhạy cảm, che token, tên tài khoản, MSSV và dữ liệu thật. Không dùng nhạc trái bản quyền.

Nguồn: https://support.google.com/youtube/answer/157177 ; https://support.google.com/youtube/answer/57407 ; https://support.google.com/youtube/answer/71674 ; https://support.google.com/youtube/answer/1722171 .

## 4. Evidence Ledger — 16 bằng chứng có ID, thu ở P0–P4

**Chưa tồn tại bất kỳ EV nào ở R06.** Sẽ lưu lại **có chọn lọc**, không tạo 16 thư mục hoặc 16 file ảnh placeholder. Những hình chỉ để chèn báo cáo có thể lưu trong workspace tạo báo cáo ngoài repo; không đưa dữ liệu riêng tư/screenshot account lên GitHub.

| ID | Thời điểm | Bằng chứng phải thu sau khi app có thật | Dùng ở |
|---|---|---|---|
| EV-01 | P0/P4 | Commit SHA/repository URL nguồn code cuối và quyền xem | GitHub, PDF14/18 |
| EV-02 | P0/P4 | Python/pip versions, lệnh run thành công | PDF14–16/video |
| EV-03 | P3 | App raw: 12×4, duplicate2, missing2 | PDF05–06/video |
| EV-04 | P3 | App clean: 10×4, duplicate0, missing0 trên canonical CSV | PDF07–08/video |
| EV-05 | P3 | Minh.gio_hoc=4, Ngoc.diem=8 sau điền trung vị | PDF08/video |
| EV-06 | P1/P3 | NumPy/Pandas stats mean7.8, std population≈1.249, A8/B7.6 | PDF09–10/video |
| EV-07 | P2/P3 | Matplotlib histogram Figure với 5 bins, [2,2,3,2,1] | PDF11/video |
| EV-08 | P2/P3 | Bar mean A8/B7.6, trục Y gốc 0 | PDF12/video |
| EV-09 | P2/P3 | Scatter 10 cặp học–điểm, trục rõ | PDF13/video |
| EV-10 | P3 | Download CSV, đọc lại đúng 10×4, không có cột index | PDF15/video |
| EV-11 | P1–P4 | Logs kiểm thử **thực**, command/versions/pass-fail/commit | PDF16/tự chấm |
| EV-12 | P4 | Ít nhất một lỗi upload/edge case được thông báo đúng | PDF16/video nếu đủ thời gian |
| EV-13 | P4 | Ưu điểm/hạn chế/điểm tự chấm căn cứ tính năng thực | PDF17/Form F06 |
| EV-14 | P4 | PDF final: số trang, dung lượng, render + đọc/link đúng | Form F05 |
| EV-15 | P4 | YouTube URL xem được, chữ rõ, đúng commit và tiêu đề | Form F04 |
| EV-16 | P4 | Link repo đọc được với **quyền người chấm** | Form F03 |

**Release baseline**: Mọi EV-03..EV-12 và báo cáo/video phải nói về **cùng một Git SHA**, sample_data.csv cuối và bộ version đã thực chạy. Nếu logic/số liệu đổi sau khi quay phải cập nhật ảnh/video/PDF bị ảnh hưởng. R04 oracle không tự biến thành EV của app.

### 4.1. Quyền truy cập và riêng tư
- Repo hiện **private**: gửi URL thường không đủ cho người chấm. Owner chọn public **sau rà secret/PII** hoặc phương án cấp quyền phù hợp; không tự đổi visibility. Trên personal private repo, quyền collaborator có khả năng sửa code, nên không mặc định là chỉ đọc.
- YouTube **Unlisted không có nghĩa bảo mật tuyệt đối**; người có link có thể chia sẻ lại. Chỉ dùng dữ liệu giả lập và tránh thông tin cá nhân trong video.
- Giữ đường dẫn thật trong PDF, video description và form đồng nhất; không đặt URL giả/chưa upload trong README hoặc bản nộp.

## 5. Khung tự chấm theo form — CHƯA CÓ ĐIỂM THẬT

| Tiêu chí | Tối đa | Căn cứ trước khi chấm | Khi nào không đạt tối đa |
|---|---:|---|---|
| Hoàn thành chức năng | 3 | M01–M07, các màn hình EV-03..10 | Thiếu/tắc chức năng core |
| Kiến thức & kỹ thuật Python | 2 | Pandas/NumPy/Matplotlib **được dùng thật** và giải thích được | Thư viện chỉ import, không biết giải thích |
| Chất lượng mã nguồn | 2 | Ba file rõ, kết quả OR/IO/UI thật, xử lý lỗi | Lặp/sai logic, chưa kiểm thử hoặc còn crash |
| Giao diện/trực quan hóa | 1 | App 1 trang, 3 figure có nhãn đúng | Biểu đồ gây hiểu sai hoặc UI không xem được |
| Báo cáo & minh chứng | 2 | PDF/YouTube/GitHub/QA links hợp lệ | Thiếu tài liệu, link chặn người xem, mâu thuẫn dữ liệu |
| **Tổng** | **10** | **Chưa tự chấm** | |

**Mẫu viết sau khi kiểm thử cuối (không điền số giả):**

> Em tự đánh giá dự án đạt [tổng]/10 điểm: hoàn thành chức năng [ ]/3 vì [tính năng/EV]; kỹ thuật Python [ ]/2 vì [giải thích đúng các thư viện]; chất lượng code [ ]/2 vì [cấu trúc & QA]; giao diện/trực quan [ ]/1 vì [hình/EV]; báo cáo và minh chứng [ ]/2 vì [PDF/video/repo]. Ưu điểm của sản phẩm là [đã kiểm chứng]. Hạn chế còn lại là [thực tế], hướng khắc phục là [việc khả thi]. Điểm tự đánh giá phản ánh những tính năng đã hoàn thành và kết quả kiểm thử thực tế.

**Không tự chấm 10/10 mặc định.** Không gọi giới hạn chủ đích “không làm ML” là lỗi nếu ML nằm ngoài nội dung chủ đề 5.5.

## 6. Trace: một claim, một bộ chứng cứ nhất quán

| Claim | Oracle & Test | PDF | Video |
|---|---|---|---|
| Raw 12/2 duplicates/2 missing | PROJECT_SPEC §5; OR-01 | 05–06 | 01:05–01:45 |
| Clean 10, median4/8, raw không mutate | PROJECT_SPEC §11; OR-02/03/12/15 | 07–08 | 01:45–02:35 |
| Mean7.8, population std≈1.249 | OR-04/05 | 09–10 | 02:35–03:25 |
| Groups A8/B7.6 | OR-06/11 | 10/12 | 02:35–04:35 |
| Histogram counts, scatter pairs | OR-07/08 | 11/13 | 03:25–04:35 |
| CSV export đúng active_df | IO-10/UI-06 | 15 | 04:35–05:15 |
| QA/errors/env thật | EV-02/11/12, OR/IO/UI | 14–16 | 00:25–01:05, 05:15–06:30 |
| Hoàn thành nộp bài | EV-14/15/16 | PDF18/form | Link YouTube/watch |

## 7. Quy trình production và gate dừng — chỉ thực hiện sau khi user giao
1. P0–P3: triển khai/app ổn định; xác minh OR/IO/UI trong môi trường sạch.
2. P4 code-freeze: chọn Git SHA cuối, versions, canonical CSV, test pass; không quay khi app còn lỗi core.
3. Thu EV-01..13 thực từ code/build đã chọn; chỉ chọn ảnh cần thiết.
4. Quay demo ứng dụng thật, upload YouTube, kiểm được từ link ngoài tài khoản chủ; kiểm HD nếu cần.
5. Soạn PDF từ EV và code thật; kiểm trang, size, Unicode, link, hình/bảng và toàn bộ trang render.
6. Tự chấm năm mục chỉ sau QA; cộng đúng ≤10, nêu ưu/nhược thật.
7. Kiểm thông tin cá nhân trong form rồi **chính người dùng nộp** khi sẵn sàng.

**BLOCK:** không hoàn thành F03 (link code), F04 (video), F05 (PDF), F06 (tự chấm) hoặc oracle quan trọng thì không tuyên bố “đã xong bài nộp”.

## 8. Tài liệu dùng để thiết kế — không phải quy định thầy
- Hai ảnh biểu mẫu người dùng cung cấp, trích xuất tại `docs/REQUIREMENTS.md`.
- Hướng dẫn báo cáo kỹ thuật: https://writingcenter.gmu.edu/writing-resources/imrad/writing-an-imrad-report ; https://writingcenter.tamu.edu/guides/resources/lab-reports.html ; https://www.aub.edu.lb/msfea/creates/Pages/sections.aspx .
- YouTube chính thức: https://support.google.com/youtube/answer/157177 ; https://support.google.com/youtube/answer/57407 ; https://support.google.com/youtube/answer/71674 ; https://support.google.com/youtube/answer/1722171 .
- GitHub quyền truy cập: https://docs.github.com/en/repositories/creating-and-managing-repositories/access-to-repositories .
- PDF QA principle: xuất → **render tất cả trang** → rà typography/figures/tables/links → đếm và kiểm file-size → sửa và render lại.

## 9. R06 self-review
- [x] Bao quát F02–F06, phân biệt teacher-confirmed với design suggestion.
- [x] Khung 18 trang có nhiệm vụ cụ thể, có quy tắc giữ 15–20 physical pages.
- [x] Kịch bản YouTube ~7 phút quay ứng dụng thực (không giả timeline bắt buộc).
- [x] 16 EV gắn nơi thu và nơi trình bày; có release SHA để chống lệch phiên bản.
- [x] Năm tiêu chí tổng 10 điểm, **không bịa điểm tự chấm**.
- [x] Bảo mật GitHub private/YouTube Unlisted, link QA, PDF layout render QA.
- [x] Không có ứng dụng, PDF, video hay EV thực được tạo trong research.
- [x] Chỉ R07 tiếp theo, sau đó FINAL; P0–P4 vẫn BLOCKED.

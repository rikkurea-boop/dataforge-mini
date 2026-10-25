# Yêu cầu chính thức, bằng chứng và ma trận nghiệm thu — Research 01

**Cập nhật:** 2026-10-25 · **Nguồn ưu tiên:** hai ảnh biểu mẫu người dùng cung cấp trong chat ngày 2026-10-25.  
**Chế độ:** xác minh yêu cầu, KHÔNG triển khai ứng dụng. Đọc cùng PROJECT_SPEC.md và docs/PLAN.md.

## 1. Quy tắc phân loại bằng chứng
- **FORM-CONFIRMED**: thấy trực tiếp trong phần biểu mẫu/đoạn thông báo được chụp. Chỉ khẳng định nội dung có trong vùng ảnh; ảnh không chứng minh toàn bộ biểu mẫu không có trường khác.
- **USER-DECIDED**: quyết định được người dùng trực tiếp xác nhận trong chat.
- **DESIGN-PROPOSED**: giải pháp nhóm nghiên cứu đề xuất để đáp ứng bài tập, không phải quy định của giảng viên.
- **UNKNOWN**: chưa có căn cứ; không suy diễn, không tự coi là không bắt buộc.
- **PLATFORM-DOC**: quy tắc từ tài liệu nền tảng chính thức, KHÔNG phải tiêu chí giảng viên.

## 2. Nguồn gốc chứng cứ

| ID | Nguồn | Phạm vi được quan sát | Giới hạn |
|---|---|---|---|
| FORM-01 | Ảnh 1 do người dùng cung cấp (2026-10-25) | Thông báo bài tập cá nhân "Chương 5 – Ứng dụng Python"; danh sách chủ đề 5.1–5.5 | Không chứa toàn bộ hướng dẫn thực hiện hoặc hạn nộp |
| FORM-02 | Ảnh 2 do người dùng cung cấp (2026-10-25) | Các mục Google Form về link mã nguồn, video YouTube, PDF 15–20 trang, tự đánh giá 5 tiêu chí | Ảnh bị giới hạn khung nhìn; các câu hỏi phía dưới có thể chưa xuất hiện |
| USER-01 | User trực tiếp chọn đề tài trong chat | "Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python" | Là tên đề tài, không phải câu chữ của thầy |
| USER-02 | User trực tiếp quyết định cách làm | DataForge Mini độc lập DataForge; tối giản, dễ trình bày toàn bộ code | Không đồng nghĩa mọi chức năng đề xuất đều đã được duyệt |
| USER-03 | User yêu cầu quy trình làm việc | 7 lượt research chuyên sâu + 1 lượt kiểm định trước khi triển khai; chỉ chuẩn bị, không làm project ở giai đoạn này | Không được bắt đầu code khi chưa có quyết định cho triển khai |
| PLATFORM-01 | https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories | Private repository không mặc nhiên truy cập được từ bên ngoài | Quy tắc nền tảng |
| PLATFORM-02 | https://support.google.com/youtube/answer/157177?hl=en | Public/Unlisted có thể xem bằng link; Private giới hạn người được cho phép | Quy tắc nền tảng |

**Trích yếu chính xác từ FORM-01:** thông báo yêu cầu sinh viên điền thông tin và nộp sản phẩm dự án cá nhân thuộc Chương 5, tự kiểm tra thông tin cá nhân, đường dẫn mã nguồn và các tài liệu minh chứng; "Mỗi sinh viên nộp sản phẩm của chính mình". Chủ đề 5.5: "Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib".

**Trích yếu chính xác từ FORM-02:** "Link mã nguồn dự án (GitHub hoặc nền tảng tương đương)" (*); "Link video Youtube demo sản phẩm" (*); "PDF Báo cáo (từ 15-20 trang)" (*) với "Tải 1 tệp được hỗ trợ lên: PDF. Kích thước tối đa 100 MB"; mục "Tự đánh giá dự án cá nhân" (*) yêu cầu đoạn văn ngắn tự nhận xét, chấm theo 5 tiêu chí, nêu ưu điểm, hạn chế, giải thích điểm.

Ảnh gốc hiện nằm trong cuộc hội thoại của chủ dự án, **chưa lưu dưới dạng file ảnh trong repository**. Bản ghi này là bản trích xuất thủ công để các AI về sau tiếp quản được; nếu cần kiểm toán nguyên ảnh phải xin file gốc hoặc quyền xem chat.

## 3. Yêu cầu truy vết (RTM)

| ID | Phân loại | Yêu cầu / quyết định | Minh chứng cần có khi nộp | Xác minh |
|---|---|---|---|---|
| F01 | FORM-CONFIRMED | Một sản phẩm cá nhân thuộc Chương 5, chọn mục 5.5 | Repo/code có nguồn gốc rõ, tên/chủ đề đúng | Xem repo + đối chiếu sản phẩm |
| F02 | FORM-CONFIRMED | Điền và kiểm tra thông tin cá nhân trong form | Các trường thông tin trong biểu mẫu | Người nộp tự kiểm tra; **không đưa dữ liệu cá nhân vào repo** |
| F03 | FORM-CONFIRMED | Nộp link mã nguồn GitHub hoặc tương đương | Link đúng commit/branch chứa sản phẩm | Mở link từ tài khoản không có quyền sở hữu |
| F04 | FORM-CONFIRMED | Nộp link video YouTube demo sản phẩm | Video hoạt động, thể hiện sản phẩm thật | Mở link từ cửa sổ chưa đăng nhập |
| F05 | FORM-CONFIRMED | Nộp 1 file báo cáo PDF 15–20 trang, tối đa 100 MB | File PDF và số trang, dung lượng thật | Đếm trang, kiểm tra file và dung lượng |
| F06 | FORM-CONFIRMED | Đoạn tự nhận xét và tự đánh giá 5 tiêu chí, nêu ưu/nhược và lý do điểm | Nội dung điền trong form, gắn bằng chứng | Đủ năm thành phần và lập luận |
| U01 | USER-DECIDED | Tên đề tài: Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python | Tên nhất quán trong README, báo cáo và video | So khớp tên |
| U02 | USER-DECIDED | Dự án tách biệt Data-Forge gốc, tối giản, giải thích toàn bộ code | Source tree ít tầng, code có thể walkthrough | Code review + demo lời giải thích |
| U03 | USER-DECIDED | Chỉ nghiên cứu/chuẩn bị cho đến khi kế hoạch 7+1 lượt được khóa | Repo docs/plan; không có implementation ngoài phê duyệt | Kiểm tra git diff/commit |
| D01 | DESIGN-PROPOSED | App dùng Streamlit với CSV → Pandas → NumPy → Matplotlib → xuất CSV | Demo logic ba thư viện | Test và video; sẽ khóa ở Research 02–03 |
| D02 | DESIGN-PROPOSED | Thống kê mô tả, 2–3 biểu đồ, cleaning đơn giản, ví dụ đối chứng | Dataset mẫu, kết quả chuẩn | Test và đối chiếu tính tay; sẽ khóa ở Research 02–04 |

**Lưu ý:** việc giảng viên liệt kê tên ba thư viện trong chủ đề **không chứng minh** có một số lượng hàm/biểu đồ bắt buộc cụ thể. Yêu cầu app, lựa chọn CSV/Streamlit và 3 chart là thiết kế của dự án để đáp ứng chủ đề, không được ghi "thầy yêu cầu" khi chưa có bằng chứng.

## 4. Thang điểm **tự đánh giá** nhìn thấy trên biểu mẫu

| Tiêu chí | Tối đa | Loại minh chứng dự kiến | Cách tránh tự chấm quá mức |
|---|---:|---|---|
| Mức độ hoàn thành chức năng | 3 | Từng chức năng demo chạy, đối chiếu với spec | Chỉ nêu tính năng đã chạy |
| Kiến thức và kỹ thuật Python | 2 | Giải thích rõ Pandas, NumPy, Matplotlib và code sử dụng | Không ghi tên thư viện mà không có xử lý thật |
| Chất lượng mã nguồn | 2 | Cấu trúc gọn, hàm rõ, test, xử lý lỗi | Không tự nhận "clean code" nếu chưa review |
| Giao diện/trải nghiệm hoặc trực quan hóa dữ liệu | 1 | Ảnh giao diện và biểu đồ có nhãn, đúng dữ liệu | Không đánh đồng giao diện bóng bẩy với tính đúng |
| Báo cáo và minh chứng sản phẩm | 2 | PDF 15–20 trang, demo YouTube, ảnh/code đối chứng | Link/file phải truy cập được và khớp phiên bản |
| **Tổng** | **10** | | |

Đây là **các mục sinh viên tự chấm trong form**; không suy diễn rằng giảng viên chấm cuối cùng theo một rubric duy nhất giống hệt.

Chưa có kết quả thực thi, do đó **chưa thể điền điểm tự chấm cụ thể**.

## 5. Ma trận tiêu chí nghiệm thu nội bộ (không phải đòi hỏi nguyên văn của thầy)

| Gate | Điều kiện kiểm tra | Cơ sở |
|---|---|---|
| G-APP | MVP làm đúng luồng xử lý dữ liệu, ba thư viện xuất hiện trong code chạy thật | Thiết kế để đáp ứng F01; chi tiết khóa ở lượt 02–04 |
| G-CODE | Không có hệ thống không cần thiết; người học giải thích được toàn bộ file/hàm | U02 |
| G-VALID | Kết quả xử lý và biểu đồ có test/đối chứng; lỗi đầu vào được xử lý | Dự án cam kết chất lượng; cụ thể hóa lượt 04–05 |
| G-REPO | Link mã nguồn xem được bởi người chấm, không phụ thuộc nhánh research | F03; GitHub access |
| G-VIDEO | YouTube demo đúng commit sản phẩm và có thể xem qua link | F04; YouTube access |
| G-PDF | PDF mở được, đủ 15–20 trang, <=100MB; nội dung trùng khớp phiên bản demo | F05 |
| G-SELF | Đã viết đánh giá trung thực theo 5 tiêu chí, nêu ưu/nhược và lý do | F06 |
| G-SUBMIT | Điền đủ thông tin người nộp và xác minh mọi link/file trước khi gửi form | F02–F06 |

## 6. Điều chưa thể kết luận từ hai ảnh
- **Deadline, giờ đóng form, chính sách trễ hạn:** UNKNOWN.
- **Video tối thiểu/tối đa bao nhiêu phút, định dạng lời thoại:** UNKNOWN.
- **Có yêu cầu PPT/slides hay không:** UNKNOWN; **chưa thấy** trong phần ảnh.
- **Báo cáo có biểu mẫu, trích dẫn, định dạng, số trang tính phụ lục ra sao:** UNKNOWN ngoài 15–20 trang PDF.
- **Thầy yêu cầu giao diện Tkinter/Flask/Streamlit không:** UNKNOWN; chọn 5.5 không đồng nghĩa phải dùng 5.1 hoặc 5.2.
- **Cần đồ án nhóm hay cá nhân:** FORM-01 khẳng định bài nộp là cá nhân.
- **Có thêm trường form ngoài khung ảnh không:** UNKNOWN.
- **Có tiêu chí chấm ngoài phần tự đánh giá không:** UNKNOWN.

## 7. Hai rủi ro có thể khóa ngay từ lúc chuẩn bị
1. Repo hiện là **private**, nên link GitHub tự nó không đảm bảo thầy xem được. Trước khi nộp, chọn public (sau khi kiểm tra dữ liệu/secret) hoặc phương án cấp quyền phù hợp và kiểm tra bằng tài khoản không có quyền. Không đổi quyền riêng tư nếu user chưa đồng ý.
2. Video YouTube **Private** không phải dạng chỉ cần link là ai cũng xem được; Public hoặc Unlisted phù hợp hơn cho việc nộp link. Chọn quyền riêng tư do owner quyết định; kiểm tra thực tế từ trình duyệt không đăng nhập.

## 8. Research 01: kết luận và ranh giới
- **Đã xác minh:** F01–F06 và cơ cấu 3+2+2+1+2; cập nhật hồ sơ.
- **Chỉ đề xuất, chưa khóa:** luồng MVP cụ thể, UI, dataset, số biểu đồ và kiến trúc.
- **Không được triển khai trong lượt 01:** tạo app, cài package, viết source, tạo slide/PDF/video.
- **Lượt tiếp theo:** Research 02 — lựa chọn MVP tối thiểu + dataset phù hợp thang tự đánh giá, khóa tính năng bắt buộc/nên có/loại bỏ; dựa trên các ID F/U/D ở trên.

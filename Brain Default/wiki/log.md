  1|# Wiki Log
  2|
  3|Time-ordered log (append-only). Each entry: `## [YYYY-MM-DD] kind | title` (kind: init/ingest/update/query/lint/migrate).
  4|
  5|## [2026-10-14] ingest | Thông tin Công ty Victory Việt Nam
  6|
  7|- Source: [[Thông Tin Công Ty Victory Việt Nam]] (ghi chú do người dùng cung cấp).
  8|- Tạo: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
  9|- Insight: tập hợp thông tin pháp nhân, thanh toán và đầu mối liên hệ trong một trang tra cứu; dữ liệu chưa được xác minh độc lập.
 10|
 11|## [2026-10-14] ingest | Thông tin nhận hàng và nhà xe Victory Việt Nam
 12|
 13|- Source: [[Thông Tin Nhan Hang Va Nha Xe Victory Viet Nam]] (ghi chú do người dùng cung cấp).
 14|- Cập nhật: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
 15|- Ghi nhận thông tin nhận hàng, hai điểm nhà xe Đắc Hùng và mâu thuẫn địa chỉ cần người dùng xác minh.
 16|
 17|## [2026-10-14] update | Làm rõ địa chỉ hồ sơ và địa chỉ nhận hàng
 18|
 19|- Source: [[Giai Thich Dia Chi Ho So Va Nhan Hang]] (lời giải thích do người dùng cung cấp).
 20|- Cập nhật: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
 21|- Phân biệt địa chỉ mới dùng cho hồ sơ với cách ghi địa chỉ cũ chỉ để nhận diện điểm nhận hàng; bỏ câu hỏi xác minh địa chỉ khỏi danh sách mở.
 22|
 23|## [2026-10-14] ingest | Báo giá Victory T10 2026
 24|
 25|- Source: [[Báo Giá Victory T10 2026]] (trích xuất từ workbook người dùng gửi).
 26|- Tạo: [[Đề nghị mua hàng IT tháng 10 năm 2026]].
 27|- Insight: workbook chứa đề nghị mua 9 mặt hàng IT, không có đơn giá; tên tệp/ngữ cảnh YSS chưa khớp rõ với nội dung sheet.
 28|
 29|## [2026-10-14] update | Xóa file gửi nhầm của YSS
 30|
 31|- Theo yêu cầu người dùng, xóa source và trang Wiki phát sinh từ workbook gửi nhầm; gỡ mục khỏi chỉ mục và câu hỏi mở liên quan. Bản ghi cũ trong log được giữ nguyên để làm lịch sử.
 32|
 33|## [2026-10-15] ingest | Danh sách khách hàng Victory
 34|
 35|- Source: [[Danh sach khach hang Victory]] (workbook do người dùng cung cấp).
 36|- Tạo: [[Danh sách khách hàng Victory]].
 37|- Ghi nhận dữ liệu khách hàng để tra cứu theo tên pháp lý, mã số thuế và thông tin liên hệ.
 38|
 39|## [2026-10-16] ingest | Quy cách mẫu báo giá dùng chung Victory
 40|
 41|- Sources: [[Mau Bao Gia Chuyen Nghiep Victory Artiverse]] (mẫu PDF ban đầu) và [[Cap Nhat Quy Cach Bao Gia Victory 2026-10-16]] (các cập nhật trực tiếp của người dùng).
 42|- Tạo: [[Mẫu Báo Giá Dùng Chung Victory]].
 43|- Ghi nhận mẫu tái sử dụng, quy tắc song ngữ, ảnh sản phẩm nền trong suốt, dòng phí vận chuyển và bộ logo đối tác theo yêu cầu gần nhất.
 44|
 45|## [2026-10-16] update | Mặc định hiệu lực và người liên hệ báo giá Victory
 46|
 47|- Source: [[Mac Dinh Hieu Luc Va Nguoi Lien He Bao Gia Victory 2026-10-16]].
 48|- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]] và mẫu HTML dùng chung.
 49|- Áp dụng mặc định hiệu lực 7 ngày và người liên hệ Phòng mua hàng; cập nhật báo giá Artiverse hiện tại.
 50|
 51|## [2026-10-16] ingest | Báo giá Artiverse làm ví dụ cho mẫu Victory
 52|
 53|- Source: [[Bao Gia Artiverse VIC-2-2026]]; tệp báo giá HTML hiện hành được liên kết trong source.
 54|- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]].
 55|- Insight: lưu báo giá Artiverse như ví dụ áp dụng; thông tin giao dịch không trở thành mặc định cho khách hàng khác.
 56|
 57|## [2026-10-17] ingest | Luật Doanh nghiệp và Luật Thuế giá trị gia tăng
 58|
 59|- Sources: [[Luat Doanh nghiep 59 2020 va sua doi]] và [[Luat Thue gia tri gia tang 48 2024 va sua doi]], gồm liên kết văn bản chính thức.
 60|- Tạo: [[Luật Doanh nghiệp Việt Nam]] và [[Luật Thuế giá trị gia tăng Việt Nam]].
 61|- Ghi nhận bản đồ tra cứu có dẫn nguồn; VAT được cập nhật theo sửa đổi 09/2026/QH16. Đây không phải bản hợp nhất toàn văn hay tư vấn cho hồ sơ cụ thể.
 62|
 63|## [2026-10-17] ingest | Xác nhận mẫu báo giá Victory sau khi khôi phục
 64|
 65|- Source: [[Xac Nhan Mau Bao Gia Victory 2026-10-17]] (người dùng xác nhận tệp HTML hiện hành là mẫu chuẩn).
 66|- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]] và [[index]].
 67|- Ghi nhận: mẫu HTML đã duyệt có trường địa chỉ giao hàng khách hàng và ghi chú phí vận chuyển song ngữ; xác nhận này không biến các điều khoản thương mại khác thành mặc định.
 68|
 69|## [2026-10-18] ingest | tự học từ chat
 70|
 71|Đã tạo:
 72|- [[Chia sẻ kho tri thức qua bot Zalo nhóm]]
 73|
 74|## [2026-10-18] ingest | Danh sách hàng hóa dịch vụ
 75|
 76|- Source: [[inbox/telegram/Danh_sach_hang_hoa_dich_vu.xlsx]] (workbook người dùng gửi; giữ nguyên bản gốc).
 77|- Tạo: [[Danh Mục Hàng Hóa Dịch Vụ]].
 78|- Chưng cất 3.491 dòng gồm mã, tên hàng hóa/dịch vụ, đơn vị tính chính và thuế suất GTGT nếu có. Ghi quy tắc ưu tiên tên chuẩn và đối chiếu mã, tên gần giống, model/cấu hình; hỏi khi còn nhiều ứng viên không phân biệt được.
 79|
 80|## [2026-10-18] update | Thuế suất GTGT danh mục hàng hóa
 81|
 82|- Source: [[Xac Nhan Thue Suat Hang Hoa 2026-10-18]] (xác nhận trực tiếp của người dùng).
 83|- Cập nhật: [[Danh Mục Hàng Hóa Dịch Vụ]] và [[index]].
 84|- Áp dụng mức mặc định 8% cho toàn bộ 3.491 mặt hàng; các mức 10% trong workbook được ghi nhận là dữ liệu cũ. Workbook gốc không bị sửa.
 85|
 86|## [2026-10-18] ingest | Luật Đất đai Việt Nam
 87|
 88|- Sources: [[Luat Dat dai va van ban chinh thuc den 2026-10-18]], gồm Luật 31/2024/QH15, Luật 43/2024/QH15, văn bản hợp nhất 46/VBHN-BNNMT, Nghị quyết 254/2025/QH15, Nghị định 49/2026/NĐ-CP, 50/2026/NĐ-CP, Nghị quyết 29/2026/QH16 và nguồn về các mốc sửa đổi tương lai.
 89|- Tạo: [[Luật Đất đai Việt Nam]]; cập nhật [[index]].
 90|- Insight: dùng Luật 31 làm khung nhưng phải kiểm tra sửa đổi, quy định chi tiết, chuyển tiếp và văn bản địa phương; tách rõ Luật 21/2026/QH16 (hiệu lực 01/01/2027) và kế hoạch sửa luật khỏi quy định đang có hiệu lực.
 91|- Phạm vi: bản đồ tra cứu khái quát, chưa phải bản hợp nhất toàn văn hay kết luận cho hồ sơ cụ thể.
 92|
 93|## [2026-10-18] update | Xóa trang Luật Đất đai theo yêu cầu người dùng
 94|
 95|- Theo yêu cầu người dùng, gỡ trang tri thức khỏi Wiki, chỉ mục và câu hỏi mở; xóa đoạn tư vấn luật đất đai khỏi bộ nhớ hội thoại có thể truy xuất.
 96|- Giữ nguyên lịch sử nhật ký và file trong `sources/` theo quy ước nguồn thô bất biến.
 97|
 98|## [2026-10-18] ingest | Mẫu hợp đồng nguyên tắc mua bán hàng hóa
 99|
- Source: [[Mau Hop Dong Nguyen Tac Mua Ban Hang Hoa]]; bản DOC gốc được bảo toàn tại `sources/`.
- Source: [[Quy Tac Lap Hop Dong Victory 2026-10-18]] (quy tắc lập ngày, số hợp đồng, trường khách hàng và hạn cuối năm do người dùng đưa).
- Tạo: [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]]; cập nhật [[index]].
- Ghi rõ mẫu cũ có gia hạn tự động và duy trì hiệu lực đến khi quyết toán, mâu thuẫn với quy tắc ngày hết hạn cuối năm; giữ câu hỏi mở để xác nhận trước khi hợp nhất.


## [2026-10-18] update | Tiêu hóa lại mẫu hợp đồng từ PDF

- Nguồn chính được thay bằng [[Mau Hop Dong Nguyen Tac Mua Ban Hang Hoa PDF]]; PDF gốc giữ nguyên tại [[inbox/telegram/hop dong nguyen tac mua ban.pdf]]. Bản Word trước đó giữ nguyên như nguồn lịch sử.
- Cập nhật [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]] và [[index]], giữ nguyên các quy tắc người dùng về ngày lập, số hợp đồng, trường thiếu để trống và ngày hết hạn cuối năm.
- PDF xác nhận nội dung mẫu có điều khoản tự gia hạn và chờ quyết toán; mâu thuẫn với quy tắc hết hạn cuối năm vẫn được giữ thành câu hỏi mở.

## [2026-10-18] update | Gỡ mẫu và dự thảo hợp đồng theo yêu cầu người dùng

- Theo yêu cầu người dùng, xóa trang Wiki mẫu hợp đồng, dự thảo Nam Trường và fact bộ nhớ về quy tắc lập hợp đồng; gỡ liên kết khỏi chỉ mục Wiki và câu hỏi mở.
- Giữ nguyên file gốc người dùng gửi và tài liệu trong `sources/` theo quy ước nguồn bất biến.
## [2026-10-18] ingest | Khung pháp luật giám đốc doanh nghiệp

- Source: [[Khung phap luat giam doc doanh nghiep]], danh mục văn bản tra cứu từ Cổng văn bản Chính phủ.
- Tạo: [[Pháp luật giám đốc doanh nghiệp]]; cập nhật [[index]].
- Insight: giám đốc nên ưu tiên quản trị/thẩm quyền, thuế-kế toán, hợp đồng, lao động-bảo hiểm-an toàn; luật đầu tư, cạnh tranh và chuyên ngành được xác định theo hoạt động thực tế.
- Phạm vi: trang định hướng, không thay thế rà soát điều khoản cụ thể và toàn bộ văn bản hướng dẫn đang hiệu lực.

## [2026-10-19] update | Cập nhật hướng dẫn thuế giá trị gia tăng

- Đối chiếu Cổng Thông tin điện tử Chính phủ và Công báo: Nghị định 144/2026/NĐ-CP ban hành 05/05/2026, hiệu lực 20/06/2026, sửa Nghị định 181/2025/NĐ-CP đã được sửa đổi bởi Nghị định 359/2025/NĐ-CP.
- Thêm [[Nghi dinh 144 2026 sua doi huong dan thue GTGT]] và cập nhật [[Luật Thuế giá trị gia tăng Việt Nam]], gồm phạm vi điều chỉnh hướng dẫn và lưu ý tra toàn văn/phụ lục khi áp dụng.
- Rà soát CSDL quốc gia VBPL về Luật Doanh nghiệp 59/2020/QH14: các văn bản sửa đổi được liệt kê gồm Luật 03/2022/QH15, Luật 76/2025/QH15 và Luật 56/2024/QH15; không thấy sửa đổi mới hơn trong phạm vi rà soát ngày này.

## [2026-10-19] ingest | tự học từ chat

Đã tạo:
- [[Nguyên tắc giữ nguyên mẫu đã duyệt]]


## [2026-10-20] update | Cập nhật thời hạn chính sách thuế xăng dầu

- Đối chiếu Nghị quyết 43/2026/NQ-CP và bản PDF ký số trên Cổng Thông tin điện tử Chính phủ; xác nhận ban hành 30/09/2026, hiệu lực 01/10/2026 đến hết 31/12/2026.
- Ghi nhận việc kéo dài thời hạn áp dụng chính sách thuế bảo vệ môi trường và thuế GTGT theo Nghị quyết 19/2026/QH16 đối với xăng, dầu, nguyên liệu sản xuất xăng dầu và nhiên liệu bay trong [[Luật Thuế giá trị gia tăng Việt Nam]].
- Lưu nguồn đã tiêu hóa tại [[Nghi quyet 43 2026 keo dai thue xang dau]].
## [2026-10-20] ingest | Lỗi cơ bản Canon LBP2900

- Đọc và tổng hợp User's Guide chính hãng cùng bản sao Service Manual cho mã lỗi dịch vụ.
- Tạo [[Canon LBP 2900 - lỗi cơ bản và xử lý an toàn]], cập nhật [[wiki/index]].
- Nhấn mạnh phân biệt Scanner Error nội bộ với chức năng scan, thao tác người dùng an toàn và lỗi cần kỹ thuật viên.

## [2026-10-20] ingest | Lỗi cơ bản Canon LBP3300, LBP251dw và LBP252dw

- Đối chiếu User's Guide Canon cho LBP3300 và User's Guide chung LBP252dw/LBP251dw.
- Tạo [[Canon LBP 3300 - lỗi cơ bản và xử lý an toàn]] và [[Canon LBP 251dw và 252dw - lỗi cơ bản và xử lý an toàn]]; cập nhật [[wiki/index]].
- Phân biệt hướng dẫn người dùng với mã lỗi từ tài liệu dịch vụ; không hướng dẫn tháo cụm điện, laser hoặc bộ sấy.

## [2026-10-20] ingest | Lỗi cơ bản thường gặp ở máy in

- Đối chiếu tài liệu hỗ trợ chính hãng HP, Canon và Epson về kẹt giấy, lỗi kết nối/hàng đợi, chất lượng in, cấp giấy và thông báo vật tư.
- Tạo [[Các lỗi cơ bản thường gặp ở máy in]] và cập nhật [[wiki/index]].
- Ghi rõ đây là bản đồ triệu chứng chung, không thay thế hướng dẫn theo model; không suy ra linh kiện hỏng chỉ từ một biểu hiện.

## [2026-10-22] ingest | Lỗi cơ bản laptop, camera, photocopy và mạng

- Đối chiếu tài liệu hỗ trợ chính hãng Dell/Lenovo, Axis, Canon/Ricoh và Microsoft/Cisco.
- Tạo [[Lỗi cơ bản laptop và cách nhận diện]], [[Lỗi cơ bản camera IP và hệ thống giám sát]], [[Lỗi cơ bản máy photocopy]] và [[Lỗi cơ bản hệ thống mạng]]; cập nhật [[wiki/index]].
- Chắt lọc triệu chứng thành khu vực/nguyên nhân có thể liên quan; không khẳng định hỏng linh kiện nếu chỉ có triệu chứng chung và không ghi cách khắc phục.


## [2026-10-20] ingest | Xác nhận mẫu hợp đồng nguyên tắc dùng lại

- Source: [[Xac Nhan Mau Hop Dong Khanh Toan 2026-10-20]]; bản hợp đồng tham chiếu nằm tại `hop-dong/Du thao HDNTMB Khanh Toan 20102026.html`.
- Tạo lại/cập nhật: [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]] và [[index]] theo xác nhận mới nhất của người dùng.
- Ghi nhận các mặc định đã chốt: hạn mức tín dụng 200 triệu đồng, nợ tối đa 90 ngày từ ngày giao hàng, điều khoản xử lý giao thiếu/sai, bảo hành, lãi quá hạn từ ngày 90, mốc khởi kiện 3,5 tháng và tự thanh lý khi hoàn thành nghĩa vụ.
- Giữ PDF đã tiêu hóa trước đây làm nguồn lịch sử; bản hiện tại được chọn làm mẫu áp dụng. Ghi chú điểm chưa thống nhất giữa hai mốc thanh toán ngay trong chính bản tham chiếu.


## [2026-10-20] update | Chốt thanh toán ngay sau khi giao hàng

- Source: [[Xac Nhan Moc Thanh Toan Mau HDNTMB 2026-10-20]] (xác nhận trực tiếp của người dùng).
- Sửa Điều 4.1 trong `hop-dong/Du thao HDNTMB Khanh Toan 20102026.html` để thống nhất thanh toán ngay sau khi nhận hàng; điều chỉnh hệ quả không thanh toán thành tạm dừng giao các lô tiếp theo.
- Cập nhật [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]] và [[index]]; mốc này thay cho điểm chưa thống nhất đã ghi trong lần ingest trước.

## [2026-10-21] ingest | Mã lỗi máy in - đợt xác minh đầu tiên

Đã xử lý 29 model/biến thể có tài liệu hãng xác định phạm vi: Canon PIXMA TS3120, TS3122, TS8120, TS8140, TS8150, TS8151, TS8152, TS8160, TS8170, TS8190, TS8195, TS6110, TS6120, TS6140, TS6150, TS6151, TS6160, TS701, TS702, TS704, TS705, TS706, TS707, TS709; Epson ET-2800, ET-2803; Brother MFC-J4335DW, MFC-J4345DW, MFC-J4535DW. Mã/ý nghĩa được trích từ tài liệu chính hãng; TS8100/TS6100/TS700 hiện mới ghi danh sách support code, chưa gán ý nghĩa từng mã. Brother ghi thông báo chữ, không suy ra mã số. Chưa đạt mục tiêu 50 model; còn 21 model cần xác minh ở lượt sau. Trang đã tạo: [[Canon PIXMA TS series - mã hỗ trợ lỗi]], [[Epson ET-2800 series - mã hiển thị lỗi]], [[Brother MFC-J4335DW family - thông báo lỗi]]. Sources đều đã processed.


## [2026-10-21] update | Cập nhật quy định đăng ký doanh nghiệp

- Đối chiếu Cổng văn bản Chính phủ và Cổng thông tin quốc gia về đăng ký doanh nghiệp: Nghị định 296/2026/NĐ-CP ban hành, có hiệu lực 23/07/2026; sửa đổi Nghị định 168/2025/NĐ-CP.
- Thêm nguồn đã xử lý [[Nghi dinh 296 2026 dang ky doanh nghiep]] và trang dẫn nguồn [[Nguồn Nghị định 296-2026-NĐ-CP - Cổng văn bản Chính phủ]].
- Cập nhật [[Luật Doanh nghiệp Việt Nam]], [[Pháp luật giám đốc doanh nghiệp]] và [[index]], ghi nhận thay đổi về góp vốn/đứng tên thay, khai thác dữ liệu, đăng ký trực tuyến và kê khai chủ sở hữu hưởng lợi.

## [2026-10-21] ingest | Mẫu hợp đồng mua bán Victory bán ra

- Nguồn tham chiếu: [[Mau hop dong mua ban Victory ban ra]] (bản DOCX đã chỉnh theo xác nhận của người dùng).
- Tạo Wiki [[Mẫu Hợp Đồng Mua Bán Victory Bán Ra]] và thêm vào [[index]].
- Ghi nhận: Victory là Bên Bán; khách là Bên Mua; thanh toán toàn bộ sau ký, bàn giao đủ hàng và chứng từ; nếu được thỏa thuận chậm thì tối đa 30 ngày; giao hàng tại địa chỉ Bên Mua; mỗi bên giữ một bản; Times New Roman màu đen, thân bài 13 pt, tiêu đề 18 pt, bỏ chân trang.
- Không dùng thông tin giao dịch Siêu Việt làm dữ liệu mặc định cho giao dịch sau.


## [2026-10-21] update | Chuẩn hóa bảng và định dạng hợp đồng Victory bán ra

- Sửa bảng hàng hóa trong hợp đồng VIC-39-2026 và file mẫu: bỏ cột bảo hành khỏi bảng, xóa ô tổng cộng rỗng gây đường viền thừa, căn độ rộng bảng theo các cột còn lại.
- Cập nhật [[Mẫu Hợp Đồng Mua Bán Victory Bán Ra]]: địa điểm ở câu mở đầu lấy theo địa chỉ Bên Bán; tiêu đề Điều 2 in đậm, nội dung các khoản để chữ thường.

## [2026-10-22] ingest | Brother HL-L2350DW - thông báo lỗi hiển thị

- Source: [[Brother HL-L2350DW error and maintenance messages]], hướng dẫn trực tuyến chính hãng Brother.
- Tạo [[Brother HL-L2350DW - thông báo lỗi hiển thị]] và cập nhật [[index]].
- Ghi các nhãn hiển thị cùng phạm vi nguyên nhân hãng nêu; không diễn giải `Print Unable ##` thành mã service và không suy linh kiện hỏng.

## [2026-10-22] update | Theo dõi Nghị định 384/2026/NĐ-CP về xuất xứ hàng hóa

- Đối chiếu trang văn bản chính thức của Cổng Chính phủ: ban hành 09/10/2026, hiệu lực 01/01/2027, phạm vi theo trích yếu là xác định xuất xứ Việt Nam đối với hàng hóa sản xuất và lưu thông trong nước. [[Nguồn Nghị định 384-2026-NĐ-CP - Cổng văn bản Chính phủ]]
- Tạo trang nguồn Wiki, cập nhật [[Luật Doanh nghiệp Việt Nam]] và [[index]]. Ghi rõ đây không phải văn bản sửa đổi Luật Doanh nghiệp; chưa ghi tiêu chí/ nghĩa vụ chi tiết do chưa trích xuất được nội dung PDF.


## [2026-10-22] ingest | Mẫu biên bản bàn giao và nghiệm thu hàng hóa gọn

- Người dùng xác nhận biên bản VIC-YUE là mẫu chuẩn và yêu cầu dùng mặc định cho các lần sau.
- Cập nhật [[bien-ban/Mau bien ban ban giao va nghiem thu hang hoa dich vu]] thành mẫu gọn; tạo [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] và cập nhật [[index]].
- Ghi nhận quy cách: A4, lề trái/phải 2,54 cm, Times New Roman; tiêu đề 18 pt, chữ còn lại 13 pt; nội dung căn đều; bảng hàng hóa giữa trang; phần ký hai bên không viền.
- Không tái sử dụng dữ liệu giao dịch Yuechang; chỉ khẳng định hoàn tất/đạt yêu cầu khi đã có xác nhận thực tế.

## [2026-10-22] ingest | Giá tham khảo từ nhóm Zalo

- Người dùng yêu cầu ghi nhớ giá được báo trong nhóm để dùng tham khảo chung khi khách ở các nhóm hỏi.
- Tạo [[Giá tham khảo từ nhóm Zalo]] và cập nhật [[index]]. Lưu giá kèm mặt hàng, đơn/ngữ cảnh và thread/message ID để đối chiếu.
- Quy tắc áp dụng: nếu một mặt hàng có nhiều lần báo giá, ưu tiên mức gần nhất phù hợp; giữ rõ khác biệt theo đơn/cấu hình và không dùng mục chưa đủ ngữ cảnh để báo giá.

## [2026-10-23] ingest | HP LaserJet Pro M404dn jam error codes
- Nguồn chính hãng HP về mã kẹt giấy cho dòng M304/M305/M404/M405.
- Tạo [[HP LaserJet Pro M404dn - mã lỗi kẹt giấy]] và [[Danh mục model máy in đã tra cứu]], cập nhật [[wiki/index]]. [[HP LaserJet Pro M404dn jam error codes]]
- Ghi nhận phạm vi mã người dùng, phân biệt mã service và giới hạn chẩn đoán; không đưa hướng dẫn sửa chữa.

## [2026-10-23] update | Giá hộp mực HP 107A từ nhóm Nam Trường

- Đối chiếu lịch sử nhóm VICTORY-NAM TRƯỜNG COMPUTER 114LÊHỒNGPHONG: 1 cartridge 107A được báo 175.000đ (thread `6037079067171344716`, message `8405959372674`). Đồng bộ hoàn tất, không có khoảng trống.
- Cập nhật [[Giá tham khảo từ nhóm Zalo]]; ưu tiên mức 175.000đ là lần báo mới nhất đã thấy cho HP 107A.

## [2026-10-23] update | Đính chính model HP 400 M401d

- Chủ xác nhận mã máy in đầu tiên trong danh sách giá 1.750.000đ là HP 400 M401d, không phải HP410d.
- Cập nhật [[Giá tham khảo từ nhóm Zalo]] để dùng đúng model khi tra cứu giá; giá do chủ cung cấp, không phải báo giá từ nhóm.

## [2026-10-23] ingest | Giá máy in 2 mặt đã qua sử dụng

- Chủ xác nhận 7 mã máy in đã nêu trước đó là máy 2 mặt đã qua sử dụng; lưu kèm tình trạng để không nhầm với hàng mới.
- Ghi nhận đủ model và giá do chủ cung cấp trong [[Giá tham khảo từ nhóm Zalo]], gồm HP 400 M401d đã được đính chính.

## [2026-10-23] ingest | Giá Canon và HP do chủ cung cấp

- Ghi nhận sáu mức giá máy in do chủ cung cấp trong [[Giá tham khảo từ nhóm Zalo]], chưa gán tình trạng mới/cũ.
- Đánh dấu “Canon 1102” là mã chưa đủ căn cứ xác định model; không dùng để báo đúng tên/chức năng cho đến khi đối chiếu tem máy.

## [2026-10-23] update | Đính chính Canon 1102 thành HP 1102

- Chủ xác nhận mã đầu tiên trong danh sách là HP 1102; sửa [[Giá tham khảo từ nhóm Zalo]] thành HP LaserJet Pro P1102 với giá 1.200.000đ.

## [2026-10-23] update | Phân loại máy in 1 mặt đã qua sử dụng

- Chủ xác nhận sáu mã HP 1102, Canon 3018, 6000, 6018, 2900 và HP M15a trong danh sách giá 23/10 là máy in 1 mặt đã qua sử dụng.
- Cập nhật [[Giá tham khảo từ nhóm Zalo]] để chỉ dùng các mức này cho đúng tình trạng hàng.

## [2026-10-23] ingest | Giá và tương thích các hộp mực HP/Canon

- Ghi đủ giá chủ cung cấp cho HP 12A, 35A, 78A, 05A, 070, 76A, Canon 337, HP 16A, 14A, 92A và 93A; giữ riêng biến thể có chip/không chip.
- Lưu bảng họ máy tương thích trong [[Tương thích hộp mực HP và Canon đã tra cứu]] và cập nhật [[Giá tham khảo từ nhóm Zalo]] cùng [[index]].
- Ghi nhận HP 93A là CZ192A, tương thích M435/M701/M706; không nhầm với 49A Q5949A. Giá 05A mới nhất do chủ cung cấp là 130.000đ; mốc trước 125.000đ có ngữ cảnh loại có chip trong nhóm nên được giữ lại riêng.

## [2026-10-23] update | Cập nhật mẫu biên bản bàn giao theo xác nhận người dùng

- Cập nhật mẫu HTML [[bien-ban/Mau bien ban ban giao nghiem thu hang hoa Victory]] và hướng dẫn [[bien-ban/Mau bien ban ban giao va nghiem thu hang hoa dich vu]].
- Quy cách mới: tiêu đề 16 pt, toàn bộ chữ 12 pt kể cả bảng; ngày/địa điểm và địa chỉ hai bên in nghiêng; bảng 4 cột; chữ ký hai bên không viền, hướng dẫn ký in nghiêng ngay dưới dòng đại diện.
- Ghi nhận mặc định dùng ngày hóa đơn, địa điểm là địa chỉ Bên Mua, số lượng thực nhận bằng chứng từ và lập 2 bản. Câu xác nhận giao đủ/nhận đủ chỉ áp dụng khi có xác nhận thực tế.


## [2026-10-23] update | Chốt câu kết quả mặc định cho biên bản bàn giao

- Theo xác nhận của người dùng, cập nhật [[bien-ban/Mau bien ban ban giao nghiem thu hang hoa Victory]] và hướng dẫn [[bien-ban/Mau bien ban ban giao va nghiem thu hang hoa dich vu]]: luôn giữ nguyên câu “Kết quả: Bên bán đã giao đủ số lượng và Bên mua đã nhận đủ số lượng hàng hóa theo danh sách.” trong biên bản bàn giao.

## [2026-10-23] ingest | tự học từ chat

Đã tạo:
- [[Quy tắc báo giá trong nhóm Zalo]]

## [2026-10-24] ingest | tự học từ chat

Đã tạo:
- [[Canon LBP3500 - bản in đen toàn trang sau khi nạp mực]]

## [2026-10-24] ingest | tự học từ chat

Đã tạo:
- [[Hộp mực tương thích HP LaserJet Pro M404dn]]
## [2026-10-25] update | Chưng cất giá bán chung và quy trình Luna Zalo

- Cập nhật [[Giá tham khảo từ nhóm Zalo]]: bổ sung bốn máy in Canon 2 mặt đã qua sử dụng do chủ cung cấp; rà lại nguồn giá, biến thể và mục loại trừ giá nhà cung cấp/báo giá riêng.
- Cập nhật [[Quy tắc báo giá trong nhóm Zalo]] theo phân công mới của Luna: chỉ trả lời hai nhóm được chọn, Luna xử lý giá/đơn còn Victory xử lý kỹ thuật, chuyển đơn qua một nhánh hệ thống duy nhất có chống trùng và chỉ xác nhận trạng thái đã gửi khi có bằng chứng.
- Cập nhật [[index]] để mô tả rõ quy tắc nguồn giá và phạm vi quy trình.
- Nguồn: [[memory/conversations/2026-10-23]], [[memory/conversations/2026-10-24]], [[memory/conversations/2026-10-25]].

## [2026-10-26] ingest | Giá linh kiện Canon 2900 và 3300

- Bổ sung giá cụm sấy, main nguồn, ECU, quang và vỏ Canon 2900; quang và cụm con lăn ra giấy Canon 3300.
- Tách riêng vỏ mới và vỏ cũ zin theo máy. Đánh dấu đơn vị chưa được nêu, ngoại trừ cụm con lăn ra giấy 3300 là 150K/cụm.
- Nguồn: [[memory/facts/gia-linh-kien-canon-2900-3300-2026-10-26]].

## [2026-10-27] ingest | Mẫu biên bản làm việc Công ty Thể thao Xuân Thiện

- Lưu bản gốc trong `attachments/`, tạo bản Word dùng lại giữ nguyên định dạng và font, để trống các dòng chấm.
- Tạo trang [[Mẫu Biên Bản Làm Việc Công Ty Thể Thao Xuân Thiện]] và bản trích xuất nguồn [[Mau bien ban lam viec Cong ty The thao Xuan Thien]].

## [2026-10-27] update | Quy cách bổ sung mẫu biên bản làm việc Xuân Thiện

- Ngày giờ lấy theo thời điểm lập trừ khi người dùng cung cấp ngày giờ khác.
- Hai hình người dùng cung cấp được đặt dưới nội dung mục 1.
- Cập nhật [[Mẫu Biên Bản Làm Việc Công Ty Thể Thao Xuân Thiện]] và bộ nhớ vai trò.

## [2026-10-27] ingest | tự học từ chat

Đã tạo:
- [[Trình bày phần tổng hợp thuế trên báo giá]]

## [2026-10-27] ingest | Vật tư thay thế hệ thống LED Thể thao Xuân Thiện

- Ghi nhận ba tên vật tư do người dùng cung cấp và tạo trang [[Vật Tư Thay Thế Hệ Thống LED Thể Thao Xuân Thiện]].

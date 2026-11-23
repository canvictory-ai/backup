# Wiki Log

Time-ordered log (append-only). Each entry: `## [YYYY-MM-DD] kind | title` (kind: init/ingest/update/query/lint/migrate).

## [2026-11-19] update | Luna chỉ trực Zalo và hỗ trợ kỹ thuật

- Theo yêu cầu mới nhất của chủ, giữ cho Luna duy nhất nhiệm vụ trực Zalo và trả lời vấn đề kỹ thuật; gỡ việc báo giá, xử lý/chuyển đơn, gửi thông tin hỗ trợ chung và việc nội bộ khỏi phạm vi hiện hành.
- Ghi nhận loop chuyển đơn đã bị xóa; cập nhật hồ sơ agent, bộ phán xử và [[Phạm vi công việc của bot Luna trên Zalo]].

## [2026-11-19] update | Cách Luna tra cứu và trả lời kỹ thuật

- Theo yêu cầu mới nhất, trước mỗi câu trả lời kỹ thuật Luna tra cứu nguồn trực tuyến đáng tin cậy, ưu tiên thông tin sát model/tình huống; diễn đạt tự nhiên, không nhắc việc tra cứu hoặc gửi link, không đưa suy luận vào câu trả lời.
- Đồng bộ hướng dẫn agent, hồ sơ bộ phán xử, Wiki và memory. Nếu chưa đủ căn cứ, Luna hỏi chi tiết còn thiếu hoặc nói rõ chưa xác định được.

## [2026-11-19] update | Học phản biện và nêu dự đoán có điều kiện

- Theo bổ sung mới nhất của chủ, Luna kiểm chứng phản biện trong nhóm; chỉ lưu câu trả lời xác nhận đúng vào Wiki kèm nguồn/ngữ cảnh để dùng lại.
- Khi chưa có câu trả lời chuẩn, Luna được nêu nguyên nhân khả dĩ dựa trên dấu hiệu thực tế nếu nói rõ đó là dự đoán, không trình bày như sự thật. Đồng bộ agent, hồ sơ bộ phán xử, Wiki và memory.

## [2026-11-19] update | Không trích nguồn trong tin kỹ thuật gửi khách

- Làm rõ rằng Luna dùng nguồn trực tuyến để kiểm chứng, nhưng tin gửi khách phải tự nhiên như kiến thức đã nắm, không có trích dẫn, tên nguồn, link tham khảo hay lời nhắc đã tra cứu.
- Cập nhật hồ sơ agent, bộ phán xử, Wiki và memory.

## [2026-11-19] update | Không hứa tra cứu trong tin gửi khách

- Theo yêu cầu mới nhất, không đưa câu “em sẽ tra mã/tìm hiểu rồi báo lại” vào tin khách. Tra cứu phải hoàn tất trước khi trả lời; câu gửi khách chỉ nêu nội dung kỹ thuật cần thiết.
- Đồng bộ hồ sơ agent, bộ phán xử, Wiki và memory.

## [2026-10-14] ingest | Thông tin Công ty Victory Việt Nam

- Source: [[Thông Tin Công Ty Victory Việt Nam]] (ghi chú do người dùng cung cấp).
- Tạo: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
- Insight: tập hợp thông tin pháp nhân, thanh toán và đầu mối liên hệ trong một trang tra cứu; dữ liệu chưa được xác minh độc lập.

## [2026-10-14] ingest | Thông tin nhận hàng và nhà xe Victory Việt Nam

- Source: [[Thông Tin Nhan Hang Va Nha Xe Victory Viet Nam]] (ghi chú do người dùng cung cấp).
- Cập nhật: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
- Ghi nhận thông tin nhận hàng, hai điểm nhà xe Đắc Hùng và mâu thuẫn địa chỉ cần người dùng xác minh.

## [2026-10-14] update | Làm rõ địa chỉ hồ sơ và địa chỉ nhận hàng

- Source: [[Giai Thich Dia Chi Ho So Va Nhan Hang]] (lời giải thích do người dùng cung cấp).
- Cập nhật: [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]].
- Phân biệt địa chỉ mới dùng cho hồ sơ với cách ghi địa chỉ cũ chỉ để nhận diện điểm nhận hàng; bỏ câu hỏi xác minh địa chỉ khỏi danh sách mở.

## [2026-10-14] ingest | Báo giá Victory T10 2026

- Source: [[Báo Giá Victory T10 2026]] (trích xuất từ workbook người dùng gửi).
- Tạo: [[Đề nghị mua hàng IT tháng 10 năm 2026]].
- Insight: workbook chứa đề nghị mua 9 mặt hàng IT, không có đơn giá; tên tệp/ngữ cảnh YSS chưa khớp rõ với nội dung sheet.

## [2026-10-14] update | Xóa file gửi nhầm của YSS

- Theo yêu cầu người dùng, xóa source và trang Wiki phát sinh từ workbook gửi nhầm; gỡ mục khỏi chỉ mục và câu hỏi mở liên quan. Bản ghi cũ trong log được giữ nguyên để làm lịch sử.

## [2026-10-15] ingest | Danh sách khách hàng Victory

- Source: [[Danh sach khach hang Victory]] (workbook do người dùng cung cấp).
- Tạo: [[Danh sách khách hàng Victory]].
- Ghi nhận dữ liệu khách hàng để tra cứu theo tên pháp lý, mã số thuế và thông tin liên hệ.

## [2026-10-16] ingest | Quy cách mẫu báo giá dùng chung Victory

- Sources: [[Mau Bao Gia Chuyen Nghiep Victory Artiverse]] (mẫu PDF ban đầu) và [[Cap Nhat Quy Cach Bao Gia Victory 2026-10-16]] (các cập nhật trực tiếp của người dùng).
- Tạo: [[Mẫu Báo Giá Dùng Chung Victory]].
- Ghi nhận mẫu tái sử dụng, quy tắc song ngữ, ảnh sản phẩm nền trong suốt, dòng phí vận chuyển và bộ logo đối tác theo yêu cầu gần nhất.

## [2026-10-16] update | Mặc định hiệu lực và người liên hệ báo giá Victory

- Source: [[Mac Dinh Hieu Luc Va Nguoi Lien He Bao Gia Victory 2026-10-16]].
- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]] và mẫu HTML dùng chung.
- Áp dụng mặc định hiệu lực 7 ngày và người liên hệ Phòng mua hàng; cập nhật báo giá Artiverse hiện tại.

## [2026-10-16] ingest | Báo giá Artiverse làm ví dụ cho mẫu Victory

- Source: [[Bao Gia Artiverse VIC-2-2026]]; tệp báo giá HTML hiện hành được liên kết trong source.
- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]].
- Insight: lưu báo giá Artiverse như ví dụ áp dụng; thông tin giao dịch không trở thành mặc định cho khách hàng khác.

## [2026-10-17] ingest | Luật Doanh nghiệp và Luật Thuế giá trị gia tăng

- Sources: [[Luat Doanh nghiep 59 2020 va sua doi]] và [[Luat Thue gia tri gia tang 48 2024 va sua doi]], gồm liên kết văn bản chính thức.
- Tạo: [[Luật Doanh nghiệp Việt Nam]] và [[Luật Thuế giá trị gia tăng Việt Nam]].
- Ghi nhận bản đồ tra cứu có dẫn nguồn; VAT được cập nhật theo sửa đổi 09/2026/QH16. Đây không phải bản hợp nhất toàn văn hay tư vấn cho hồ sơ cụ thể.

## [2026-10-17] ingest | Xác nhận mẫu báo giá Victory sau khi khôi phục

- Source: [[Xac Nhan Mau Bao Gia Victory 2026-10-17]] (người dùng xác nhận tệp HTML hiện hành là mẫu chuẩn).
- Cập nhật: [[Mẫu Báo Giá Dùng Chung Victory]] và [[index]].
- Ghi nhận: mẫu HTML đã duyệt có trường địa chỉ giao hàng khách hàng và ghi chú phí vận chuyển song ngữ; xác nhận này không biến các điều khoản thương mại khác thành mặc định.

## [2026-10-18] ingest | tự học từ chat

Đã tạo:
- [[Chia sẻ kho tri thức qua bot Zalo nhóm]]

## [2026-10-18] ingest | Danh sách hàng hóa dịch vụ

- Source: [[inbox/telegram/Danh_sach_hang_hoa_dich_vu.xlsx]] (workbook người dùng gửi; giữ nguyên bản gốc).
- Tạo: [[Danh Mục Hàng Hóa Dịch Vụ]].
- Chưng cất 3.491 dòng gồm mã, tên hàng hóa/dịch vụ, đơn vị tính chính và thuế suất GTGT nếu có. Ghi quy tắc ưu tiên tên chuẩn và đối chiếu mã, tên gần giống, model/cấu hình; hỏi khi còn nhiều ứng viên không phân biệt được.

## [2026-10-18] update | Thuế suất GTGT danh mục hàng hóa

- Source: [[Xac Nhan Thue Suat Hang Hoa 2026-10-18]] (xác nhận trực tiếp của người dùng).
- Cập nhật: [[Danh Mục Hàng Hóa Dịch Vụ]] và [[index]].
- Áp dụng mức mặc định 8% cho toàn bộ 3.491 mặt hàng; các mức 10% trong workbook được ghi nhận là dữ liệu cũ. Workbook gốc không bị sửa.

## [2026-10-18] ingest | Luật Đất đai Việt Nam

- Sources: [[Luat Dat dai va van ban chinh thuc den 2026-10-18]], gồm Luật 31/2024/QH15, Luật 43/2024/QH15, văn bản hợp nhất 46/VBHN-BNNMT, Nghị quyết 254/2025/QH15, Nghị định 49/2026/NĐ-CP, 50/2026/NĐ-CP, Nghị quyết 29/2026/QH16 và nguồn về các mốc sửa đổi tương lai.
- Tạo: [[Luật Đất đai Việt Nam]]; cập nhật [[index]].
- Insight: dùng Luật 31 làm khung nhưng phải kiểm tra sửa đổi, quy định chi tiết, chuyển tiếp và văn bản địa phương; tách rõ Luật 21/2026/QH16 (hiệu lực 01/01/2027) và kế hoạch sửa luật khỏi quy định đang có hiệu lực.
- Phạm vi: bản đồ tra cứu khái quát, chưa phải bản hợp nhất toàn văn hay kết luận cho hồ sơ cụ thể.

## [2026-10-18] update | Xóa trang Luật Đất đai theo yêu cầu người dùng

- Theo yêu cầu người dùng, gỡ trang tri thức khỏi Wiki, chỉ mục và câu hỏi mở; xóa đoạn tư vấn luật đất đai khỏi bộ nhớ hội thoại có thể truy xuất.
- Giữ nguyên lịch sử nhật ký và file trong `sources/` theo quy ước nguồn thô bất biến.

## [2026-10-18] ingest | Mẫu hợp đồng nguyên tắc mua bán hàng hóa

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

## [2026-10-27] update | Chốt mẫu biên bản làm việc Xuân Thiện

- Lưu bản Word dùng lại theo bố cục và định dạng biên bản đã duyệt; để trống các dữ kiện vụ việc, giữ câu chữ cố định và vị trí hai ảnh dưới mục 1.
- Cập nhật [[Mẫu Biên Bản Làm Việc Công Ty Thể Thao Xuân Thiện]] và [[wiki/index]].

## [2026-10-27] ingest | tự học từ chat

Đã tạo:
- [[Hậu quả chậm đóng bảo hiểm xã hội]]
## [2026-10-28] ingest | Triệu chứng kỹ thuật máy in từ Zalo

- Đọc 154 tin trong cửa sổ 24 giờ; kết nối báo đồng bộ đầy đủ, không có khoảng mất kết nối.
- Tạo [[Canon G1010 - mã nháy đèn]] theo bảng support code chính hãng; thêm model vào [[Danh mục model máy in đã tra cứu]].

## [2026-10-28] ingest | tự học từ chat

Đã tạo:
- [[Diễn đạt mức độ chắc chắn khi chẩn đoán từ xa]]

## [2026-10-28] ingest | Triệu chứng kỹ thuật máy tính từ Zalo

- Rà soát lịch sử 24 giờ, đồng bộ hoàn chỉnh, không có khoảng mất kết nối.
- Ghi nhận ca Canon LBP3500 có hộp mực khác in bình thường và hộp vừa nạp in đen toàn trang; cập nhật [[Canon LBP3500 - bản in đen toàn trang sau khi nạp mực]] với nhãn lời kể chưa kiểm định độc lập.
- Ghi nhận laptop sập nguồn và máy báo lỗi pin nhưng thiếu model, điều kiện xảy ra và kết quả kiểm tra tại [[Zalo TESTBOT 2026-10-28 - triệu chứng kỹ thuật]].

## [2026-10-29] ingest | tự học từ chat

Đã tạo:
- [[Xử lý camera analog chập chờn qua dây đồng trục]]

## [2026-10-29] ingest | tự học từ chat

Đã tạo:
- [[Trả lời không kèm đường link nguồn]]

## [2026-10-30] ingest | Triệu chứng kỹ thuật từ Zalo

- Đọc 161 tin trong cửa sổ 24 giờ; đồng bộ hoàn chỉnh, không có khoảng mất kết nối.
- Tạo [[Zalo TESTBOT 2026-10-30 - triệu chứng kỹ thuật]] ghi nhận Dell 3520 kêu bíp dài lặp lại và Imou A32 báo ngoại tuyến, đèn vàng nháy; chưa đủ dữ kiện để xác minh ý nghĩa.
- Trao đổi camera đồng trục không có kết quả kiểm tra mới, nên giữ nguyên [[Xử lý camera analog chập chờn qua dây đồng trục]].

## [2026-10-30] update | Mã đèn chẩn đoán Dell Inspiron 15 3520

- Đối chiếu tài liệu dịch vụ Dell chính hãng ngày 30/10/2026; tạo [[Nguồn Dell Inspiron 15 3520 Service Manual]] và [[Dell Inspiron 15 3520 - đèn chẩn đoán]].
- Cập nhật [[Zalo TESTBOT 2026-10-30 - triệu chứng kỹ thuật]]: ghi rõ tài liệu giải nghĩa mã đèn, chưa xác minh tiếng bíp dài và chưa rõ biến thể Dell 3520.

## [2026-10-31] ingest | Triệu chứng kỹ thuật từ Zalo

- Đọc 46 tin trong cửa sổ 24 giờ; đồng bộ hoàn chỉnh, không có khoảng mất kết nối.
- Tạo [[Zalo TESTBOT 2026-10-31 - triệu chứng kỹ thuật]] ghi nhận máy tính bàn mất hình khi quạt thùng máy vẫn chạy, đầu ghi Hikvision kêu liên tục nhưng thiếu model/mã cảnh báo, và ảnh mã lỗi không truy xuất được.
- Không xác minh được nguyên nhân theo tài liệu hãng do thiếu model và thông báo cụ thể; giữ các nhận định trong chat ở mức chưa xác minh. Không ghi hướng dẫn sửa chữa.
## [2026-10-31] ingest | Máy tính bàn có nguồn nhưng không lên hình

- Chọn chủ đề theo ca kỹ thuật Zalo ngày 31/10: máy bàn vẫn quay quạt nhưng màn hình mất hình, chưa rõ model.
- Đối chiếu tài liệu hỗ trợ Dell chính hãng về no video ngày 31/10/2026; tạo [[Nguồn Dell - xử lý máy tính không hình]] và [[Lỗi máy tính để bàn có nguồn nhưng không lên hình]].
- Cập nhật [[Zalo TESTBOT 2026-10-31 - triệu chứng kỹ thuật]] với liên kết hướng dẫn khoanh vùng. Không xác định lỗi phần cứng vì thiếu model và chưa kiểm tra trực tiếp.
## [2026-11-01] cập nhật | Không bịa thông tin và giá cả
- Thêm nguyên tắc chỉ khẳng định thông tin và giá có căn cứ; nêu rõ khi chưa xác minh, thiếu dữ kiện hoặc có mâu thuẫn.

## [2026-11-01] update | Không bịa thông tin và giá cả
- Tạo [[Không bịa thông tin và giá cả]] theo xác nhận của người dùng; cập nhật [[wiki/index.md]].

## [2026-11-01] tự học | Tiếng bíp đầu ghi Hikvision
- Chọn triệu chứng đầu ghi Hikvision kêu liên tục từ [[Zalo TESTBOT 2026-10-31 - triệu chứng kỹ thuật]]. Đối chiếu hỏi đáp hỗ trợ Hikvision; ghi rõ giới hạn nguồn chỉ nói về tiếng bíp sau khởi động.
- Tạo [[Nguồn Hikvision - đầu ghi kêu bíp sau khi khởi động]] và [[Hikvision DVR/NVR - khoanh vùng tiếng bíp sau khởi động]]; cập nhật triệu chứng Zalo và [[wiki/index.md]]. Chưa kết luận nguyên nhân ca khách vì thiếu model và thông báo sự kiện.

## [2026-11-01] update | Lưu nguyên văn thông tin hỗ trợ công ty

- Cập nhật [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]] theo nội dung liên hệ do người dùng cung cấp.
- Ghi nguyên văn thông tin hỗ trợ theo giờ hành chính cho máy tính, máy in, camera, hóa đơn và tổng hợp; giữ định dạng và nêu rõ phải gửi toàn bộ nội dung này khi được hỏi, không nói thiếu số hỗ trợ riêng cho camera.
- Giữ riêng ghi chú hotline công ty 24/7 trong nguồn cũ với khung giờ hỗ trợ bộ phận trong nội dung mới.


## [2026-11-01] update | Trả đầy đủ thông tin hỗ trợ theo yêu cầu cụ thể

- Làm rõ trong [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]]: kể cả khi chỉ hỏi hỗ trợ cho một bộ phận như camera, gửi nguyên văn toàn bộ danh sách liên hệ đã cung cấp và giữ nguyên định dạng.

## [2026-11-01] update | Gộp trách nhiệm Zalo kỹ thuật vào Luna

- Cập nhật workflow Zalo để chỉ gọi Luna; gộp hướng dẫn kỹ thuật hiện hành vào hướng dẫn và bộ nhớ của Luna.
- Cập nhật [[Quy tắc báo giá trong nhóm Zalo]] và [[Các lỗi cơ bản thường gặp ở máy in]].

## [2026-11-01] update | Quy trình chốt và chuyển đơn Zalo
- Theo chỉ dẫn mới của chủ, cập nhật [[Quy tắc báo giá trong nhóm Zalo]] và `agents/luna-vu.md`: khi khách chốt, chỉ cảm ơn và chuyển đơn sang XUẤT HÀNG VICTORY; không tự đưa KiotViet vào quy trình.

## [2026-11-01] cập nhật | Tách trao đổi với khách khỏi xử lý nội bộ
- Bổ sung vào hướng dẫn Luna và [[Quy tắc báo giá trong nhóm Zalo]]: tin cho khách chỉ là lời cảm ơn; không tiết lộ việc chuyển đơn, trạng thái xác nhận, lỗi công cụ hay quy trình nội bộ. Nếu chuyển lỗi, báo chủ trong Javis.
- Làm rõ thêm tiêu chuẩn bằng chứng: chỉ báo đã chuyển khi công cụ xác nhận thành công hoặc xác minh thấy tin trong nhóm đích; nếu chưa có bằng chứng, báo chủ trong Javis là chưa xác nhận/chưa chuyển.

## [2026-11-01] ingest | tự học từ chat

Đã tạo:
- [[Quy trình xử lý đơn chốt qua Zalo]]

## [2026-11-01] update | Rút gọn nội dung chuyển đơn
- Theo yêu cầu của chủ, làm rõ trong hướng dẫn Luna, Wiki và bộ nhớ rằng tin gửi nhóm xuất hàng chỉ chứa dữ liệu cần để xuất đơn, không thêm lời dẫn hoặc diễn giải thừa.

## [2026-11-01] update | Bỏ trường thừa khỏi tin chuyển đơn
- Theo yêu cầu của chủ, bỏ khách/nhóm nguồn và tham chiếu tin gốc khỏi nội dung tin gửi nhóm xuất hàng; chỉ giữ hàng/biến thể, số lượng, giá và tổng đã xác nhận.

## [2026-11-01] update | Chỉ báo tên nhóm nguồn sau khi chuyển đơn
- Theo yêu cầu của chủ, phần báo cáo cho chủ sau khi chuyển đơn chỉ nêu tên nhóm nguồn để nhận biết nơi chốt; không nêu tên người chốt hoặc nội dung đơn.

## [2026-11-01] update | Bổ sung tên nhóm vào tin xuất hàng
- Theo yêu cầu của chủ, tin gửi nhóm xuất hàng gồm tên nhóm nguồn, hàng/biến thể, số lượng, giá và tổng tiền đã xác nhận; không kèm khách hay tham chiếu tin gốc.

## [2026-11-01] update | Không báo lỗi chuyển đơn cho khách
- Làm rõ Luna phải thực hiện ngay khi khách yêu cầu chuyển đơn; lỗi hoặc thiếu xác nhận chỉ báo chủ qua Javis, không tiết lộ với khách.

## [2026-11-01] update | Khôi phục mẫu chốt và chuyển đơn đã duyệt
- Đối chiếu hội thoại trước: khách nhận lời cảm ơn cùng tổng đơn; nhóm xuất hàng nhận nội dung theo mẫu “Tên nhóm: đơn khách vừa chốt”; chủ chỉ nhận tên nhóm sau khi chuyển.

## [2026-11-01] update | Rút gọn lời xác nhận khi khách chốt
- Theo chỉ dẫn mới nhất, Luna chỉ cảm ơn và nhắc lại hàng cùng số lượng đã chốt trước khi chuyển đơn; không nêu tổng tiền hoặc thêm lời ngoài lề trong tin cho khách.

## [2026-11-01] update | Giảm lời thừa khi Luna xử lý đơn
- Ghi nhận phản hồi của chủ rằng hôm nay Luna nói lan man; củng cố quy tắc trả lời đúng việc, ngắn gọn, không thêm nội dung ngoài lề.


## [2026-11-01] update | Diễn đạt tự nhiên với khách hàng

- Cập nhật [[Quy tắc báo giá trong nhóm Zalo]]: câu trả lời cho khách đi thẳng vào giá, đơn hoặc thông tin được hỏi; loại bỏ câu mô tả ghi nhận/lưu trữ, trạng thái hệ thống, chuyển đơn và phối hợp nội bộ.


## [2026-11-01] update | Tách bảng giá YSS khỏi giá bán trong nhóm Zalo

- Chủ xác nhận [[Bảng giá sản phẩm YSS]] chỉ dùng để lập file báo giá cho YSS khi cần; giá cập nhật về sau dùng để báo khách trong nhóm Zalo.
- Cập nhật trang giá YSS, [[Giá tham khảo từ nhóm Zalo]], [[Quy tắc báo giá trong nhóm Zalo]] và [[index]] để cấm dùng/tiết lộ giá YSS trong câu trả lời Zalo hoặc ngoài file báo giá YSS. [[memory/conversations/2026-11-01]].


## [2026-11-02] cập nhật giá | Máy in A3 cũ

Thêm giá bán buôn do người dùng cung cấp cho Canon 8710/8720/441, HP 706n và Canon 8610/8620/8630; đều đầy đủ phụ kiện. Cập nhật [[Gia Tham Khao Tu Nhom Zalo]].

## [2026-11-02] ingest | tự học từ chat

Đã tạo:
- [[Phân biệt xử lý tệp và yêu cầu đăng nội dung trong nhóm]]

## [2026-11-03] ingest | tự học từ chat

Đã tạo:
- [[Đổi khách hàng trên báo giá]]

## [2026-11-03] ingest | tự học từ chat

Đã tạo:
- [[Thời điểm lập hóa đơn giá trị gia tăng]]

## [2026-11-03] update | Tách nhóm nhận đơn khỏi nhóm xử lý hội thoại

- Cập nhật hướng dẫn Luna, workflow Zalo, loop trực và [[Quy trình xử lý đơn chốt qua Zalo]]: XUẤT HÀNG VICTORY chỉ là nhóm đích nhận đơn, Luna không phản hồi tin đến tại đó; chỉ chuyển đơn chốt từ các nhóm Zalo khác mà kết nối hiện tại cho phép đọc.
- Loop hiện vẫn tắt theo frontmatter; chỉ dẫn này cập nhật quy tắc xử lý, không xác nhận bot đang trực.

## [2026-11-03] update | Ngăn lượt nhắc kích hoạt gửi lại đơn cũ

- Rà lịch sử Zalo xác nhận đơn “3 hộp 76A có chip” ở TESTBOT đã được gửi hai lần vào 21:06:40 và 21:12:13. Giữa hai lần không có xác nhận chốt mới; có tin “Sao?” và tag Luna. Workflow nhận tag lúc 21:12:07 nhưng kết thúc `Not logged in`, nên chưa xác định được thành phần nào phát lệnh gửi thứ hai.
- Sửa hướng dẫn Luna, workflow và Wiki: chỉ tin mới xác nhận chốt hoặc trả lời trực tiếp câu hỏi còn thiếu của đúng đơn mới được tiếp tục chuyển; tag/lời nhắc/câu hỏi việc khác không mở lại đơn cũ. Nếu trạng thái không rõ hoặc nghi xử lý song song thì dừng, không gửi mù.
- Mở câu hỏi xác minh hệ thống có sổ chuyển/idempotency và khóa chống hai lượt gửi song song hay không.

## [2026-11-04] update | Bổ sung giá bán buôn Canon 2900 mới

- Cập nhật [[Giá tham khảo từ nhóm Zalo]] theo giá chủ cung cấp: máy in Canon 2900 NK KV mới, 3.150.000đ/máy.


## [2026-11-05] ingest | Bảng giá bán buôn cụm sấy

- Tạo [[Bảng giá bán buôn Victory]] với tám model HP và Canon, đồng giá 850.000đ/cụm theo chủ cung cấp.
- Cập nhật [[wiki/index]]; tách giá bán buôn khỏi bảng giá bán đại lý và [[Bảng giá sản phẩm YSS]]. [[memory/conversations/2026-11-05]]


## [2026-11-05] update | Chuyển giá cụm sấy sang giá bán đại lý

- Theo đính chính của chủ, chuyển giá 850.000đ/cụm cho tám model HP/Canon vào [[Giá tham khảo từ nhóm Zalo]] dưới loại giá bán đại lý.
- Lưu trữ trang [[Bảng giá bán buôn Victory]] do phân loại nhầm; gỡ khỏi [[wiki/index]].


## [2026-11-05] update | Bổ sung giá đại lý cụm sấy HP 401

- Thêm cụm sấy HP 401d, 401dn và 401dw giá 750K/cụm vào [[Giá tham khảo từ nhóm Zalo]].

## [2026-11-05] update | Giá bán đại lý cáp quang 1FO

- Thêm cáp quang 1FO cuộn 1.000m: 890K chưa VAT và 1.180K đã có VAT vào [[Giá tham khảo từ nhóm Zalo]]. [[memory/conversations/2026-11-05]]

## [2026-11-05] ingest | tự học từ chat

Đã tạo:
- [[Tra cứu mã tương thích trước khi báo giá]]


## [2026-11-05] update | Hợp nhất bảng giá ngoài YSS

- Hợp nhất 84 mức giá dùng chung vào [[Bang_gia_Luna.xlsx]], có cột Loại giá để tách giá bán đại lý và bán buôn.
- Giữ bảng giá YSS ở [[Bảng giá sản phẩm YSS]] riêng, không trộn vào danh mục chung.
- Hai file Excel Luna cũ giống hệt nhau; giữ bản mới làm danh mục chính và chuyển bản trùng vào `archive/bang-gia-cu/`.
- Loại khỏi danh mục áp dụng các giá nhà cung cấp, báo giá riêng theo khách/đơn và nguồn giá chưa được chủ duyệt. [[memory/conversations/2026-11-05]]


## [2026-11-05] update | Bỏ danh sách giá Luna trùng lặp

- Lưu trữ trang giá cũ [[Giá tham khảo từ nhóm Zalo]] sau khi các mức dùng chung đã được hợp nhất vào một danh mục duy nhất [[Bang_gia_Luna.xlsx]].
- Bảng giá YSS tiếp tục tách riêng tại [[Bảng giá sản phẩm YSS]].

## [2026-11-05] cleanup | Xóa các bản giá Luna cũ

- Theo yêu cầu của chủ, xóa trang giá Luna cũ và file Excel trùng đã lưu trữ để tránh nhầm tên hoặc cập nhật nhầm bảng.
- Bảng giá Luna duy nhất đang dùng: [[Bang_gia_Luna.xlsx]]. Bảng giá YSS vẫn riêng: [[Bảng giá sản phẩm YSS]].

## [2026-11-05] update | Bổ sung linh kiện Canon 2900

- Thêm bảy dòng linh kiện do chủ cung cấp vào [[Bang_gia_Luna.xlsx]]: thanh nhiệt 80K, xương sấy 100K, bao lụa bóc máy 100K, lô ép bóc máy 100K, sensor nhận giấy 80K, sensor cụm sấy 50K và khung 100K.
- Giữ đơn vị ở trạng thái chưa nêu vì chủ chưa cung cấp đơn vị. Bảng YSS không thay đổi.

## [2026-11-06] update | Bổ sung main cao áp

- Thêm riêng sáu mã main cao áp HP 402, HP 404, Canon 223, 226, 243 và 246 vào [[Bang_gia_Luna.xlsx]], mỗi mã 500K.
- Đơn vị chưa được nêu nên để là “Chưa nêu”; bảng giá YSS không thay đổi.


## [2026-11-07] update | Thiết lập nhóm Báo giá Luna làm nguồn giá bán buôn

- Theo xác nhận của chủ, nhóm Zalo Báo giá Luna (thread ID `3345965267368578027`) là nguồn chuẩn cho giá bán buôn. Các tin có mặt hàng và giá rõ ràng sẽ được nhập vào [[Bang_gia_Luna.xlsx]] với loại giá bán buôn; giá YSS vẫn tách riêng.
- Tin trong nhóm chỉ hỏi giá, chưa có mức giá cụ thể, không được ghi thành giá. Quyền dùng làm nguồn giá không mở quyền trả lời trong nhóm.
- Lượt rà hiện tại chưa có tin nào chứa mức giá cụ thể để thêm vào bảng; có một câu hỏi giá Canon 122dw nhưng chưa có giá trả lời.
- Cập nhật [[Quy tắc báo giá trong nhóm Zalo]] và bài học của Luna Vũ. [[memory/conversations/2026-11-07]]


## [2026-11-07] cập nhật giá | Main nguồn máy in HP 402D

- Ghi nhận tin giá trong nhóm Báo giá Luna: main nguồn máy in HP 402D giá 600K. Thêm vào [[Bang_gia_Luna.xlsx]] với loại giá bán buôn; đơn vị và biến thể chưa được nêu. Nguồn tin Zalo ID `8461023375023`. [[memory/conversations/2026-11-07]]


## [2026-11-07] cập nhật giá | Thiết bị và mực từ nhóm Báo giá Luna

- Thêm giá bán buôn vào [[Bang_gia_Luna.xlsx]]: mic không dây Newosund HS 58 pro 700K; Shengfu W15 930K; Ezviz H9C 3MP 2 mắt ngoài trời 1.270K; mực in Starink 071 có chip 165K, không chip 135K. Đơn vị chưa được nêu. Nguồn tin Zalo IDs `8461047741802`, `8461050170805`, `8461123795827`. [[memory/conversations/2026-11-07]]


## [2026-11-07] cập nhật giá từ ảnh | Linh kiện Canon 2900

- Đọc ảnh tin `8461055199015` trong nhóm Báo giá Luna: Bộ vỏ Canon 2900, 250K/bộ; mặt trên (ốp sấy) máy in Canon 2900, 85K/cái. Mỗi dòng số lượng 1; tình trạng bộ vỏ chưa nêu. Thêm hai mục bán buôn riêng vào [[Bang_gia_Luna.xlsx]], không nhập chung với giá bộ vỏ mới đã có vì tình trạng khác nhau hoặc chưa rõ. [[memory/conversations/2026-11-07]]

## [2026-11-08] fix | Làm bảng giá Luna truy xuất được cho chatbot

- Tạo [[Bang gia Luna - tra cuu chatbot]] từ toàn bộ 113 dòng dữ liệu trong [[Bang_gia_Luna.xlsx]], giữ các trường loại giá, mã, biến thể, đơn vị, giá, VAT, ngày cập nhật và ghi chú.
- Ghi rõ Excel là nguồn chuẩn; thêm yêu cầu đồng bộ bản Markdown mỗi khi loop cập nhật giá. Cập nhật [[index]].
- Lý do: bộ tra cứu chatbot hiện chỉ lập chỉ mục `.md`, `.txt`, `.markdown`, không lập chỉ mục `.xlsx`.

## [2026-11-08] fix | Chặn tin báo giá trong nhóm xuất hàng

- Ghi nhận Luna gửi nhầm câu trả lời giá hộp mực 133333A vào [[XUẤT HÀNG VICTORY]]. Nhóm này chỉ nhận đơn qua nhánh chuyển đơn cố định; bổ sung chặn rõ các tin báo giá và trao đổi khác trong [[agents/luna-vu]] và [[Quy tắc báo giá trong nhóm Zalo]]. Chưa tìm thấy công cụ thu hồi tin đã gửi. [[memory/conversations/2026-11-08]]



## [2026-11-09] update | Hợp nhất quy trình cộng sự và quy tắc Zalo

- Rà soát prompt các cộng sự, workflow, loop, bộ nhớ Luna và Wiki. Đặt `agents/luna-vu.md` làm nguồn chuẩn duy nhất cho hành vi Luna; Sales phụ trách file báo giá chính thức, Hồ sơ - Hợp đồng phụ trách hồ sơ, Pháp lý - Luật phụ trách câu hỏi pháp luật, Phương sai vặt chỉ tổng hợp/điều phối khi chủ yêu cầu.
- Gỡ các bản quy tắc sao chép hoặc lệch vai trò trong bộ nhớ Luna và prompt Sales/Hồ sơ; sửa định tuyến pháp lý khỏi Luna. Workflow tiếp nhận Zalo được giữ ở trạng thái `off`, chỉ để tra cứu lịch sử. Loop chỉ đối soát tin đến và đồng bộ giá, không trả lời hoặc chuyển đơn.
- Sửa quy tắc Wiki về tin chốt: khách chỉ nhận lời cảm ơn và hàng/biến thể/số lượng; tổng tiền nếu đã xác nhận chỉ có thể nằm trong tin nội bộ chuyển đơn.
- Còn điểm cần xác minh vận hành: `Javis/index.md` báo loop tự tạm dừng trong khi tệp loop ghi `enabled: true`; chưa có bằng chứng trạng thái runtime để kết luận loop thực sự chạy. `Javis/index.md` là chỉ mục tự sinh, không sửa tay.


## [2026-11-09] update | Luna xác nhận và chuyển đơn Zalo

- Theo yêu cầu của chủ, khi khách chốt Luna cảm ơn và nhắc hàng/vật tư, biến thể, số lượng trong nhóm nguồn; nếu không nắm được giá thì dùng đúng nguyên tắc duy nhất đã chốt tại hướng dẫn Luna.
- Sau đó gửi đúng một bản tóm tắt sang XUẤT HÀNG VICTORY qua `zalo_send_message` với thread `8404017101126147877`, `threadType=1`. Giá chưa xác nhận không chặn chuyển nếu hàng và số lượng đã rõ. Chỉ xác nhận hoàn tất khi công cụ xác nhận hoặc thấy đúng tin ở nhóm đích.
- Cập nhật hướng dẫn Luna, quy tắc báo giá, quy trình chốt đơn và dữ liệu học/bộ phán xử; thay mẫu mention cũ bằng mẫu mention thật ở đầu tin theo quyết định gần nhất của chủ.

## [2026-11-09] fix | Báo đủ biến thể giá khi khách hỏi chung

- Sửa [[agents/luna-vu]], [[Quy tắc báo giá trong nhóm Zalo]] và bộ nhớ Luna: nếu khách hỏi chung mặt hàng có nhiều biến thể giá đã xác nhận, báo đủ mọi biến thể trong một tin; chỉ báo riêng một loại khi khách chỉ rõ loại đó.
- Thêm ví dụ HP 76A: 140.000đ/hộp không chip và 220.000đ/hộp có chip. Cập nhật [[memory/facts/khong-phan-bien-khi-tra-loi-gia-zalo]].

## [2026-11-09] fix | Hiểu yêu cầu ship/xuất là đơn khách đã chốt

- Trong nhóm khách nguồn Luna được phép xử lý, “ship”, “lấy”, “gọi”, “chuyển” hoặc “xuất” kèm mặt hàng và số lượng được hiểu là đơn bán ra đã chốt. Luna cảm ơn trong nhóm nguồn rồi chuyển tóm tắt sang XUẤT HÀNG VICTORY; không hỏi lại khách đã chốt chưa hoặc hỏi chiều mua/bán.
- Gỡ câu hỏi xác nhận chiều giao dịch khỏi hướng dẫn Luna và cập nhật quy trình cùng bộ nhớ liên quan.
- Đối chiếu nhóm đích không thấy hai đơn này; đã gửi lời cảm ơn ở TESTBOT và mỗi đơn một bản tóm tắt vào XUẤT HÀNG VICTORY: 8 hộp HP 12A, và 2 hộp 289A + 1 hộp 35 + 2 hộp 05A.

## [2026-11-09] preference | Linh hoạt điều khoản hợp đồng theo khách hàng

- Người dùng xác nhận điều khoản pháp lý trong hợp đồng không cố định cho mọi khách hàng; giữ mẫu làm khung trình bày và linh hoạt điều khoản theo khách hàng/giao dịch. Các mặc định chung đã chốt vẫn áp dụng. Cập nhật [[Điều khoản hợp đồng linh hoạt theo khách hàng]], [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]] và [[agents/tro-ly-soan-thao-ho-so]].

## [2026-11-09] fix | Chốt mẫu duy nhất nhờ báo giá cho Luna

- Khi chưa nắm được giá, Luna chỉ gửi: `@<người hỏi> Em chưa nắm được giá <tên hàng/mã hàng>, nhờ sếp @Vũ Đức Cẩn báo giúp ạ.`
- Gắn mention thật của cả người hỏi và chủ; thay tên hàng bằng nội dung khách hỏi. Không chèn lời dẫn/giải thích, không dùng mẫu khác. Đồng bộ hướng dẫn Luna, Wiki, bộ nhớ và hồ sơ vai bot.

## [2026-11-09] format | Chữ đậm nhấn ý chính trong tin Zalo Luna

- Mọi ý chính trong tin Zalo Luna gửi phải vừa đậm vừa đỏ bằng cú pháp `**{red:<ý chính>}**`; cú pháp `**<ý chính>**` chỉ tạo chữ đậm.
- Đồng bộ hướng dẫn Luna, quy trình ghi nhớ hiện hành, Wiki quy tắc Zalo và hồ sơ vai bot hiện tại. Không tạo năng lực hoặc tệp mới.

## [2026-11-10] fix | Gắn bảng giá duy nhất vào tài liệu Luna

- Gắn [[Bang gia Luna - tra cuu chatbot]] vào tài liệu của Agent Luna để bộ truy xuất giới hạn theo tài liệu Agent có thể lấy được bảng giá.
- Chốt đây là căn cứ giá duy nhất Luna dùng khi trả lời khách; Excel là bảng gốc để cập nhật bản tra cứu, còn nhóm Báo giá Luna chỉ là đầu vào cập nhật bảng, không phải nguồn trả lời trực tiếp.
- Gỡ cách diễn đạt có thể khiến nhóm Zalo hoặc các ghi nhớ giá cũ bị hiểu là nguồn trả lời song song. Đồng bộ hồ sơ vai, hướng dẫn Luna, Wiki quy tắc và fact/index bộ nhớ.

## [2026-11-10] maintenance | Xóa các bản mẫu cũ được yêu cầu

- Đã xóa bản HTML cũ của mẫu biên bản làm việc Xuân Thiện, bản backup báo giá Victory ngày 17/10/2026 và PDF hợp đồng nguyên tắc cũ khỏi thư mục làm việc theo yêu cầu người dùng.
- Giữ các file trong `sources/` theo quy ước vault: đây là nguồn bất biến, không do AI xóa/sửa. Bản trích xuất hợp đồng nguyên tắc vẫn được đánh dấu là tài liệu lịch sử, không dùng để soạn mới.

## [2026-11-10] update | Sửa quy trình lưu câu trả lời có nguồn và loop Zalo

- QUERY trước đây chỉ yêu cầu đề xuất lưu tri thức tái sử dụng; đã đổi thành ghi thật trang Wiki nguồn chứa URL/ngày truy cập + trang tri thức + index/log khi nội dung có nguồn và giá trị dùng lại, hoặc khi chủ nói “wiki/lưu”. Không ghi nội dung vào `sources/`.
- Hướng dẫn Luna làm rõ link trong câu trả lời không đồng nghĩa tri thức đã lưu; không gửi URL nguồn vào nhóm Zalo.
- Loop Zalo được sửa để gap đồng bộ không chặn tin mới, không gán mọi tin `isSelf=true` cho loop, và không nhầm quyền `auto` với cấm ghi file trong vault.
- Vừa xác định runtime chặn loop `auto` ghi vào `Javis/`; checkpoint/audit đã được chuyển nguyên trạng sang `loop-data/` ở gốc brain để loop có thể lưu dữ liệu vận hành.
- Bổ sung bước đếm tin theo nhóm từ danh sách message và đối chiếu tổng trước khi báo cáo, sau khi verifier bắt được số lượng nhóm sai.

## [2026-11-12] fix | Ngăn Luna gán giá cho nhầm mã

Nhật ký Zalo TESTBOT ghi Luna lấy 250.000đ từ dòng Cụm trống B022 nhưng trả lời thành Cụm trống HP 102A; bảng không xác nhận hai mã là cùng mặt hàng. Đã cập nhật quy tắc chuẩn: giá luôn phải lấy đúng dòng trong [[Bang gia Luna - tra cuu chatbot]]. Theo chỉ dẫn mới nhất của chủ, Luna có thể nêu mã ứng viên như một phán đoán, kèm giá đúng dòng của mã đó và hỏi khách xác nhận; không được trình bày suy đoán như giá đã xác nhận hoặc lấy dòng tương tự gán sang mã khác. Nếu không có ứng viên hợp lý hay giá đúng dòng, dùng mẫu mention nhờ chủ báo giá. Đồng bộ hướng dẫn Agent, Wiki, memory; gỡ fact trùng đã bị thay thế.

## [2026-11-12] fix | Buộc mention báo giá của Luna dùng UID thật

Mẫu nhờ chủ báo giá trước đây chỉ nói “mention thật” nhưng chưa buộc truyền danh sách `mentions` có UID; gửi chuỗi `@Tên` bằng công cụ tin nhắn thường chỉ tạo chữ, không tag người nhận. Đã sửa hướng dẫn Agent, quy tắc Wiki, memory và hồ sơ vai bộ phán xử: dùng `zalo_send_mention` với object `{name, uid}` cho người hỏi và chủ (UID chủ `1204382391224364082`), không dùng `zalo_send_message`; thiếu UID hoặc lỗi tool thì không giả lập tag bằng chữ và không gửi bản thay thế.

## [2026-11-12] update | Thông tin tài khoản nhận thanh toán Victory

- Cập nhật [[Công Ty Cổ Phần Giải Pháp Công Nghệ và Truyền Thông Victory Việt Nam]] với tên chủ tài khoản, số tài khoản và ngân hàng theo thông tin người dùng cung cấp.
- Cập nhật [[memory/facts/thanh-toan-vao-tai-khoan-cong-ty]] để gửi đầy đủ thông tin khi khách yêu cầu thanh toán.

## [2026-11-12] fix | Dùng đúng tên hiển thị Zalo khi nhờ chủ báo giá

Đọc lịch sử TESTBOT thấy tin Luna chỉ có mention UID của người hỏi; `@Vũ Đức Cẩn` trong thân tin là chữ thường. Luồng trả lời tự động gửi qua `zalo_personal_channel.gui`: tự tag người hỏi, còn các tên `@...` thêm vào được dò theo tên người đã nhắn trong nhóm. Tên thành viên là `Victor Vu - Vũ Đức Cẩn`, nên bí danh rút gọn không khớp. Đã thay mẫu thành `@Victor Vu - Vũ Đức Cẩn` trong hướng dẫn Agent, Wiki, memory và hồ sơ vai để khớp tên Zalo thật; không gọi tool gửi mention riêng để tránh tạo hai tin.

## [2026-11-12] correction | Nguyên nhân tag chủ trong câu trả lời tự động

Điều chỉnh ghi chú vừa nêu ở entry “Buộc mention báo giá của Luna dùng UID thật”: câu trả lời tự động của bot không gửi qua tool plugin `zalo_send_mention`, nên thêm tham số `mentions` vào hướng dẫn không làm thay đổi đường gửi này. Lịch sử TESTBOT cho thấy Luna chỉ có UID mention của người được trả lời; transport chỉ tag các @Tên khác nếu khớp tên người đã nhắn trong nhóm. Tên chủ trong lịch sử là `Victor Vu - Vũ Đức Cẩn`, còn mẫu rút gọn `@Vũ Đức Cẩn` không khớp. Đã sửa mẫu trong Agent, Wiki, memory và hồ sơ bộ phán xử sang tên hiển thị đầy đủ.

## [2026-11-12] ingest | Mã QR tài khoản ngân hàng Victory

- Lưu ảnh gốc tại `attachments/QR_Tai_Khoan_Victory.jpeg` và tạo source ảnh đã xử lý tại [[QR Tai Khoan Ngan Hang Victory]].
- Cập nhật [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]] và quy tắc thanh toán: gửi kèm ảnh QR khi khách xin thông tin chuyển khoản.

## [2026-11-12] update | Chuẩn hóa chữ nhấn mạnh thành đậm và đỏ

Đồng bộ lại quy tắc định dạng Zalo trong Agent, Wiki và memory: mọi thông tin làm nổi bật phải dùng chính xác `**{red:<nội dung>}**`, để bộ gửi tạo đồng thời style đậm và đỏ. Không dùng Markdown `**...**` đứng riêng vì chỉ làm chữ đậm. Đã cập nhật fact cũ về in đậm giá thay vì tạo fact trùng.

## [2026-11-13] update | Gộp thông tin công ty và nhà xe cho Luna

Đã giữ trang công ty Victory hiện có làm nguồn Wiki duy nhất về pháp nhân, nhận hàng, hỗ trợ và nhà xe; sửa các wikilink nhận hàng thành đường dẫn nguồn thật, đồng bộ nguồn và mốc ngày. Gắn chính trang này cùng bảng giá vào tài liệu Luna, thêm chỉ dẫn trả lời đúng dữ kiện và không tự bịa địa chỉ còn thiếu của điểm Đắc Hùng Nguyễn Xiển. Xóa fact memory riêng về địa chỉ hồ sơ/nhận hàng vì đã được gộp vào trang công ty; giữ các fact quy trình thanh toán và điều khoản hợp đồng vì chúng nói về quy trình khác.

## [2026-11-13] update | Chừa chỗ ghi người đại diện trên biên bản bàn giao

- Cập nhật mẫu HTML bàn giao: tách dòng Đại diện và Chức vụ cho cả hai bên, để khoảng chấm dài đủ viết tay tên người đại diện và chức vụ.
- Đồng bộ quy cách vào [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] và hướng dẫn mẫu Markdown.

## [2026-11-15] update | Để trống ngày tháng năm trên biên bản bàn giao

- Theo yêu cầu mới, mẫu bàn giao để trống ngày, tháng, năm trên dòng ngày lập; không tự lấy ngày trên hóa đơn/đơn đặt hàng điền vào dòng này.
- Giữ riêng quy tắc đánh số biên bản, địa điểm theo địa chỉ Bên Mua, và lập hai bản mỗi bên giữ một bản. Đồng bộ vào [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]], hướng dẫn mẫu và ghi nhớ.

## [2026-11-15] update | Xác nhận mẫu chuẩn hợp đồng mua bán hàng hóa

- Theo xác nhận của người dùng, `hop-dong/Mau hop dong mua ban hang hoa va dich vu thong thuong.md` là mẫu chuẩn để lập hợp đồng mua bán hàng hóa, riêng với hợp đồng nguyên tắc.
- Cập nhật nhãn mẫu, tạo [[Mẫu Hợp Đồng Mua Bán Hàng Hóa Victory]], thêm vào [[index]] và chỉ dẫn skill soạn hồ sơ; giữ riêng mẫu hợp đồng nguyên tắc và mẫu bán ra Victory.
## [2026-11-15] update | Không ghi mã nội bộ trong tên hàng báo giá

- Theo yêu cầu người dùng, tên hàng trong báo giá không thêm mã nội bộ danh mục trong ngoặc, ví dụ `(VT02669)`; vẫn giữ model/part number nhận diện sản phẩm. Đồng bộ vào [[Mẫu Báo Giá Dùng Chung Victory]], kỹ năng lập báo giá và ghi nhớ [[memory/facts/quy-cach-bao-gia-victory]].

## [2026-11-15] update | Bố cục, đánh số và câu kết quả biên bản bàn giao

- Chừa một dòng giữa tiêu ngữ và tiêu đề; mở cột STT lên 10% bề rộng bảng.
- Số biên bản giữ đúng dạng `DDMMYYYY/BBBGNT/VIC-XXX`, không thêm số hóa đơn, PO hoặc hậu tố.
- Mở rộng câu kết quả để nêu rõ chủng loại, nhãn hiệu và chất lượng theo thỏa thuận.
- Đồng bộ mẫu HTML, hướng dẫn, Wiki và ghi nhớ.

## [2026-11-15] update | Ghi nhớ quy cách mới nhất của biên bản bàn giao

- Đồng bộ quy cách mẫu hiện hành vào memory: tiêu đề 16 pt, nội dung 12 pt, dòng trống sau quốc hiệu, cột STT 10% và câu kết quả mở rộng.
- Giữ quy tắc đã lưu về ngày trống, số biên bản không có hậu tố hóa đơn/PO và dòng đại diện/chức vụ đủ dài.
## [2026-11-16] update | Bổ sung dấu hiệu chốt đơn và tách nhiều đơn Zalo

- Bổ sung các cách nói thể hiện ý muốn lấy/gửi hàng, đồng thời quy định xét ý định trong mạch hội thoại và loại trừ câu giả định, phủ định, hủy đơn hoặc Victory mua từ nhà cung cấp.
- Quy định tách các đơn riêng trong tin nhiều dòng/nhiều tin và chuyển tuần tự theo thứ tự khách nêu; không gộp, bỏ sót hoặc gửi trùng.
- Đồng bộ [[Quy trình xử lý đơn chốt qua Zalo]], [[Quy tắc báo giá trong nhóm Zalo]], [[agents/luna-vu]] và bộ nhớ dài hạn.

## [2026-11-16] update | Duyệt mẫu giấy đề nghị thanh toán Victory

- Người dùng duyệt [[thanh-toan/Mau giay de nghi thanh toan Victory]] làm mẫu chung cho các giấy đề nghị thanh toán về sau.
- Tạo trang [[Mẫu Giấy Đề Nghị Thanh Toán Victory]], cập nhật mục lục Wiki, bộ nhớ và kỹ năng soạn hồ sơ; lưu quy cách tên công ty viết theo kiểu thông thường và in đậm.

## [2026-11-17] update | Chuẩn hóa bảng kê và khoản 2.1 trên hợp đồng

- Chỉnh bảng hàng hóa trong [[hop-dong/Hop dong mua ban hang hoa VIC-MT86 17112026]] gọn theo nội dung và đặt khoản 2.1 về chữ thường.
- Cập nhật mẫu Word Victory bán ra, tạo [[Quy Cách Trình Bày Hợp Đồng Victory]], đồng bộ mục lục, hướng dẫn soạn hồ sơ và bộ nhớ để dùng cho các hợp đồng sau.

## [2026-11-17] update | Dùng bảng kê kiểu hóa đơn GTGT trong hợp đồng

- Chỉnh bảng kê hợp đồng Công nghệ Môi trường 86 theo 8 cột hóa đơn GTGT, thêm dòng quy chiếu cột và tổng hợp tiền hàng/thuế bên dưới bảng.
- Cập nhật [[Quy Cách Trình Bày Hợp Đồng Victory]], các Wiki hợp đồng, kỹ năng soạn hồ sơ và memory để áp dụng cho hợp đồng về sau; giữ khoản 2.1 ở kiểu chữ bình thường, không in đậm.

## [2026-11-17] update | Bỏ nhãn tiếng Anh khỏi bảng kê hợp đồng

- Theo yêu cầu mới, bảng kê trong [[hop-dong/Hop dong mua ban hang hoa VIC-MT86 17112026]] bỏ các dòng tiếng Anh trong ngoặc và được dàn rộng theo vùng nội dung để hạn chế nhãn xuống dòng.
- Đồng bộ quy cách này vào [[Quy Cách Trình Bày Hợp Đồng Victory]], hướng dẫn soạn hồ sơ và memory dùng chung.


## [2026-11-17] update | Chốt mẫu hợp đồng bán ra Victory và dọn mẫu trùng

- Tạo lại [[hop-dong/Mau hop dong mua ban Victory ban ra]] từ hợp đồng Công nghệ Môi trường 86 đã duyệt; xóa dữ liệu riêng giao dịch, giữ cấu trúc và điều khoản, bảng 8 cột tiếng Việt, tên đại diện in đậm, chỉ số 2.1 in đậm.
- Cập nhật [[Mẫu Hợp Đồng Mua Bán Victory Bán Ra]], [[Quy Cách Trình Bày Hợp Đồng Victory]], chỉ mục Wiki, kỹ năng soạn thảo và bộ nhớ.
- Xóa mẫu Word Siêu Việt cũ và mẫu Markdown mua bán thông thường cùng trang Wiki trùng phạm vi. Giữ riêng mẫu hợp đồng nguyên tắc, hồ sơ vận chuyển và các hợp đồng giao dịch đã lập.

## [2026-11-18] update | Luna chỉ chuyển đơn, im lặng với nội dung khác

- Thay hướng dẫn phản hồi nhóm cũ bằng quy tắc duy nhất: nhận diện đơn lấy/gửi hàng trong mọi nhóm Luna tham gia, tách nhiều đơn và chuyển tuần tự sang XUẤT HÀNG VICTORY; mọi nội dung khác im lặng.
- Gỡ bài học cũ của bộ phán xử về trả lời việc tồn đọng; cập nhật hồ sơ vai, loop, Wiki và memory, bỏ các fact vận hành phản hồi Zalo đã bị thay thế.

## [2026-11-18] fix | Gỡ chỉ dẫn Luna trả lời giá trong nhóm

- Đổi tên và rút gọn trang quy tắc Zalo để chỉ còn luồng chuyển đơn; bỏ chỉ dẫn trả lời giá, kỹ thuật, hỗ trợ, cảm ơn và hỏi lại.
- Đánh dấu các câu hỏi Wiki cũ về mở rộng trả lời nhóm là đã bị chỉ dẫn mới nhất thay thế.


## [2026-11-18] create | Mẫu phiếu xuất kho kiêm bàn giao Victory

- Người dùng duyệt nội dung phiếu và chốt mẫu số, số phiếu tuần tự, ngày lập, địa chỉ bàn giao, kho xuất, lý do xuất, thông tin khách hàng và lượng nhận bằng lượng xuất.
- Căn các bảng theo hai lề và giữa trang; lưu mẫu Word tại [[bien-ban/Mau phieu xuat kho kiem ban giao hang hoa Victory]], cập nhật [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]], mục lục, kỹ năng và bộ nhớ.


## [2026-11-18] create | Phiếu xuất kho PXK-VIC-2026-001 cho Maple

- Lập phiếu theo hóa đơn 00001078; ghi kho VICTORY, ngày 18/11/2026, địa chỉ Maple và số lượng thực xuất bằng số lượng nhận.
- Ghi nhận số phiếu 001; số tiếp theo theo mẫu là 002. [[bien-ban/Phieu xuat kho PXK-VIC-2026-001 Maple]]

## [2026-11-18] update | VAT tổng hợp và ảnh báo giá gọn nhẹ

- Cập nhật VIC-106-2026: bỏ nhãn VAT khỏi từng dòng hàng, giữ phần tổng hợp thuế sau bảng; thu nhỏ ảnh sản phẩm nhúng còn 160×160 px.
- Quy tắc áp dụng cho báo giá sau: không ghi VAT/thuế trên từng dòng; tối ưu ảnh theo kích thước hiển thị. [[Mẫu Báo Giá Dùng Chung Victory]] [[memory/facts/thue-bao-gia-chi-o-phan-tong-hop]] [[memory/facts/bao-gia-moi-san-pham-co-anh]]

## [2026-11-19] update | Quy tắc địa điểm bàn giao trên phiếu xuất kho

- Sửa mẫu Word và quy tắc: chỉ ghi nhãn `Địa điểm bàn giao:`; lấy địa chỉ từ cơ sở dữ liệu khách hàng nếu có, nếu không thì để trống. Đã bỏ cụm `(địa chỉ khách hàng)` khỏi mẫu và phiếu Genesis hiện tại. [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-19] create | Mẫu biên bản đối chiếu công nợ Victory

- Tạo mẫu Word gọn theo tông xanh Victory; dàn bảng đối chiếu rộng bằng vùng lề văn bản, mở rộng chỗ ghi người đại diện/chức vụ; ghi quy tắc lấy thông tin Bên B từ danh sách khách hàng. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]]

## [2026-11-19] update | Tách phiếu xuất kho Genesis

- Tách phiếu `002` thành phiếu riêng cho mặt hàng thứ 4 và phiếu `003` cho các mặt hàng còn lại; cập nhật tổng thành tiền và số tiếp theo là `004`. [[bien-ban/Phieu xuat kho PXK-VIC-2026-002]] [[bien-ban/Phieu xuat kho PXK-VIC-2026-003 Genesis cac dong con lai]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-19] update | Chốt mẫu phiếu xuất kho Victory

- Cập nhật mẫu Word theo bản Genesis người dùng duyệt: bảng gồm số lượng, đơn giá, thành tiền, tình trạng; mã hàng lấy từ ký hiệu/model trong tên; tình trạng mặc định `Mới 100%`. Xóa bản xem trước phiếu xuất kho cũ đã bị thay thế; giữ các phiếu giao dịch riêng. Cập nhật Wiki, mục lục, skill và bộ nhớ. [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-19] update | Mỗi loại văn bản chỉ dùng một mẫu chuẩn

- Chốt nguyên tắc duy trì một mẫu hiện hành cho mỗi loại văn bản. Chuyển Wiki biên bản bàn giao về tệp HTML chuẩn, gỡ liên kết mẫu Markdown đã thay thế; xóa bản Word trùng của hợp đồng nguyên tắc Khánh Toàn vì bản HTML là bản chuẩn. Nguồn gốc và hồ sơ giao dịch được giữ nguyên, không dùng làm mẫu. [[Nguyên tắc giữ nguyên mẫu đã duyệt]] [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]]

## [2026-11-19] create | Phiếu xuất kho PXK-VIC-2026-004 Hà Thành

- Lập phiếu theo mẫu chuẩn cho báo giá VIC-104-2026: máy in kim Epson LQ-310+ kèm dây tín hiệu USB, số lượng 1; địa chỉ và mã số thuế theo thông tin khách hàng; giá trị bảng kê chưa VAT. Cập nhật số tiếp theo thành `005`. [[bien-ban/Phieu xuat kho PXK-VIC-2026-004 Hai Thanh Epson LQ310]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-19] create | Phiếu xuất kho PXK-VIC-2026-005 Genesis

- Lập phiếu theo hóa đơn GTGT 1C26TAA số 00000000 ngày 19/11/2026, gồm 4 dòng hàng; địa chỉ, mã số thuế người mua theo dữ liệu hóa đơn và hồ sơ khách hàng. Thành tiền bảng kê 713.638 đồng, chưa VAT. Cập nhật số tiếp theo là `006`. [[bien-ban/Phieu xuat kho PXK-VIC-2026-005 Genesis hoa don 00000000]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-19] update | Căn chỉnh bảng phiếu xuất kho

- Đặt chữ hàng tiêu đề màu trắng trên nền xanh đậm; phân lại độ rộng cột để nhãn không xuống dòng và căn tên hàng, số liệu, mã/ĐVT theo chuẩn. Cập nhật mẫu chuẩn và phiếu PXK-VIC-2026-005. [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]

## [2026-11-20] cleanup | Gỡ quy tắc Zalo cũ trùng lặp

- Gỡ quy trình vận hành Zalo lỗi thời khỏi trang kiến thức máy in, xóa trang riêng trùng lặp về không dẫn link, và rút gọn trang phạm vi Luna cùng memory thành liên kết về hồ sơ chuẩn `agents/luna-vu`.
- Quy tắc phản hồi hiện hành vẫn giới hạn Luna ở hỗ trợ kỹ thuật; mọi nội dung khác im lặng. Giữ nguyên các ghi chép hội thoại và nhật ký lịch sử, không xem chúng là chỉ dẫn đang hiệu lực.

## [2026-11-20] fix | Xóa ca mẫu cũ ngoài phạm vi kỹ thuật

- Gỡ 6 ca mẫu Luna vẫn được hướng dẫn trả lời hỏi giá, tồn kho, chốt đơn, tình trạng xuất hàng và thanh toán. Giữ 2 ca mẫu im lặng với tin bot khác và chuyện trò; giữ các ví dụ kỹ thuật riêng. Bộ phán xử hiện còn 2 ca mẫu bootstrap và một bài học kỹ thuật-only.

## [2026-11-20] update | Theo dõi nhiều yêu cầu kỹ thuật song song

- Luna giữ riêng ngữ cảnh từng người/vấn đề đến khi được giải đáp hoặc người hỏi dừng; trả lời gắn trực tiếp với tin hỏi khi có thể. Ảnh lỗi trong nhóm được xem là yêu cầu kỹ thuật dù không có chữ; nếu chỉ có ảnh, hỏi lịch sự và nêu nguyên nhân khả dĩ dựa trên dấu hiệu. Phạm vi được lưu trong [[agents/luna-vu]].
- Bỏ bài học kỹ thuật-only trùng lặp khỏi bộ phán xử; hồ sơ vai và agent chuẩn là nơi duy nhất chứa quy tắc phạm vi.

## [2026-11-20] update | Không đưa suy nghĩ nội bộ vào câu trả lời Luna

- Hướng dẫn Luna trả lời trực tiếp bằng dấu hiệu, nguyên nhân khả dĩ và bước xử lý; không kể quá trình phân tích hay dùng lời dẫn mô tả suy nghĩ nội bộ. [[agents/luna-vu]]

## [2026-11-20] update | Chủ động xử lý ảnh lỗi có mã máy

- Khi ảnh trong nhóm cho thấy mã máy hoặc mã lỗi, Luna đọc thông tin nhìn rõ, xác nhận nhẹ nhàng khách đang hỏi về lỗi rồi trả lời ngay trong luồng ảnh; hỏi thêm khi ảnh thiếu căn cứ. [[agents/luna-vu]]

## [2026-11-20] clarify | Ảnh lỗi là câu hỏi ngầm

- Không chờ khách hỏi lại hoặc hỏi xác nhận. Luna chủ động đọc mã/lỗi nhìn rõ trong ảnh và trả lời ngay; chỉ hỏi thêm khi thiếu thông tin để nhận định. [[agents/luna-vu]]


## [2026-11-20] create | Phiếu xuất kho PXK-VIC-2026-007 Artiverse Apparel

- Lập theo ảnh phiếu người dùng cung cấp; Bên Nhận, mã số thuế và địa chỉ đối chiếu theo danh sách khách hàng Victory.
- Gồm máy quét mã vạch Honeywell 1472GHD số lượng 1 và loa mini TTA-TM6 số lượng 2; tổng thành tiền 6.060.000 đồng trước VAT; kèm PO 66218976.
- Cập nhật số phiếu tiếp theo thành `008`. [[bien-ban/Phieu xuat kho PXK-VIC-2026-007 Artiverse Apparel PO 66218976]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-20] create | Hai phiếu xuất kho cho Hải Vinh

- Lập hai phiếu riêng theo hai ảnh danh sách hàng; Bên Nhận, mã số thuế và địa chỉ đối chiếu theo danh sách khách hàng Victory.
- Phiếu `008` có 5 mặt hàng, phiếu `009` có 5 mặt hàng; đơn giá và thành tiền để trống vì ảnh không có giá.
- Cập nhật số phiếu tiếp theo thành `010`. [[bien-ban/Phieu xuat kho PXK-VIC-2026-008 Hai Vinh - danh sach 1]] [[bien-ban/Phieu xuat kho PXK-VIC-2026-009 Hai Vinh - danh sach 2]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-20] update | Chốt mẫu phiếu xuất kho A4 dọc Victory

- Dựng lại tệp mẫu chuẩn từ bố cục phiếu 007 đã duyệt, xóa dữ liệu khách hàng, PO, số phiếu, ngày và mặt hàng giao dịch khỏi mẫu; giữ thông tin cố định của Victory.
- Chốt phong cách A4 dọc tông xanh như báo giá, tên công ty một dòng kèm MST, tiêu đề 15 pt một dòng, giờ căn cột với số phiếu, bảng 8 cột và chữ ký ghi chú sát chức danh.
- Rà thư mục mẫu: không còn bản mẫu xuất kho trùng khác; các phiếu đã lập vẫn là hồ sơ giao dịch riêng. Đồng bộ Wiki, memory và skill soạn hồ sơ. [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]] [[Nguyên tắc giữ nguyên mẫu đã duyệt]]


## [2026-11-20] update | Chuẩn hóa mẫu đối chiếu công nợ A4 dọc

- Chuyển mẫu Word sang A4 dọc; dàn lại bảng thông tin hai bên, bảng công nợ sáu cột và phần ký theo vùng lề, dùng tông xanh Victory đồng bộ với mẫu phiếu xuất kho. Giữ nguyên nội dung và các trường đối chiếu đã có.
- Cập nhật quy cách trong Wiki, mục lục và memory. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-20] update | Bổ sung đầu trang và thông tin Bên A cho mẫu đối chiếu công nợ

- Đồng bộ đầu trang với cụm nhận diện trên mẫu phiếu xuất kho. Địa điểm “tại” dùng địa chỉ khách hàng do người dùng cung cấp hoặc tra cứu trong cơ sở dữ liệu. Điền Bên A: Vũ Đức Cẩn, Giám đốc, điện thoại 0228.86.22222.
- Cập nhật mẫu Word, Wiki và memory. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]] [[Công ty Cổ phần Giải pháp công nghệ và Truyền thông Victory Việt Nam]]


## [2026-11-20] update | Đồng bộ đầu trang và Bên A mẫu đối chiếu công nợ

- Sao chép cụm nhận diện Victory, MST và địa chỉ từ mẫu phiếu xuất kho lên đầu trang mẫu công nợ. Dòng “tại” được để chỗ trống để điền địa chỉ khách hàng do người dùng cung cấp hoặc tra cứu trong cơ sở dữ liệu.
- Điền Bên A là Vũ Đức Cẩn, Giám đốc, điện thoại 0228.86.22222; cập nhật quy tắc Wiki và memory. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-20] update | Bỏ quốc hiệu và thu gọn phần ký mẫu đối chiếu công nợ

- Bỏ hai dòng quốc hiệu/tiêu ngữ đầu trang; thu gọn khoảng cách để “(Ký, ghi rõ họ tên)” nằm sát ngay dưới dòng đại diện. Đồng bộ quy tắc Wiki và memory. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]]


## [2026-11-20] approve | Chốt mẫu đối chiếu công nợ dùng lâu dài

- Người dùng xác nhận mẫu hiện tại là chuẩn và yêu cầu dùng cho các lần sau. Rà thư mục `thanh-toan/`: chỉ có một tệp mẫu đối chiếu công nợ, không có bản mẫu cũ trùng cần xóa. Hồ sơ giao dịch và nguồn lưu trữ không phải bản mẫu.
- Đánh dấu đây là mẫu chuẩn duy nhất trong Wiki và memory. [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]] [[memory/facts/mau-bien-ban-doi-chieu-cong-no-victory]]


## [2026-11-20] cleanup | Xóa bản tham chiếu cũ trong attachments theo yêu cầu

- Xóa bản DOCX gốc biên bản Xuân Thiện và PDF mẫu báo giá khỏi `attachments/`; gỡ các ghi chú hiện hành trỏ tới hai tệp này.
- Các nguồn trong `sources/` được giữ nguyên theo quy tắc vault: lớp nguồn thô do người dùng quản lý và AI không được sửa/xóa. Mẫu chuẩn hiện hành trong thư mục nghiệp vụ không bị xóa.


## [2026-11-20] create | Mẫu phiếu nhập kho kiêm kiểm nhận Victory

- Tạo mẫu Word A4 dọc theo nhận diện xanh Victory, có thông tin nhà cung cấp, chứng từ tham chiếu, số lượng theo chứng từ và thực nhận, tình trạng/ghi chú, kết quả kiểm nhận, hướng xử lý và bốn vị trí ký.
- Không mặc định kết quả kiểm nhận; để trống số phiếu cho đến khi người dùng chốt quy tắc đánh số. Cập nhật Wiki, mục lục và memory. [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-20] fix | Căn lại đầu trang mẫu phiếu nhập kho

- Sửa bảng nhận diện Victory bị co hẹp: đặt độ rộng cố định theo vùng lề, căn thương hiệu thành hai dòng gọn và giảm cỡ chữ phần thông tin công ty để tránh vỡ dòng. [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]]


## [2026-11-20] update | Căn chỉnh lại trang mẫu phiếu nhập kho

- Chuẩn hóa A4 dọc, tiêu đề căn giữa; số phiếu trái và ngày/giờ nhập phải trên cùng hàng; tiêu đề mục căn trái, bảng dàn theo lề. Bổ sung dòng lý do nhập và địa điểm nhập.
- Đồng bộ mô tả trong Wiki và memory. [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]]


## [2026-11-20] update | Căn hai phía đầu trang mẫu phiếu nhập kho

- Căn “VICTORY TECHNOLOGY” sát trái và tên pháp nhân, MST, địa chỉ sát phải trên cùng hàng đầu trang. Cập nhật quy cách Wiki và memory. [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]]


## [2026-11-20] approve | Chốt mẫu phiếu nhập kho dùng lâu dài

- Người dùng xác nhận mẫu phiếu nhập kho kiêm kiểm nhận hiện tại là chuẩn, áp dụng cho các lần sau và yêu cầu xóa bản cũ bị thay thế. Rà soát thư mục mẫu: chỉ có một tệp mẫu hiện hành, không có bản cũ trùng để xóa.
- Đánh dấu mẫu hiện tại là bản chuẩn duy nhất trong Wiki và memory. [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]]

## [2026-11-20] update | Mẫu HTML xanh Victory cho biên bản Xuân Thiện

- Chuyển mẫu dùng lại sang HTML phong cách xanh Victory và đặt HTML làm định dạng đầu ra mặc định cho biên bản Xuân Thiện.
- Giữ nguyên câu chữ cố định, bố cục hai bên, quy cách chữ đã duyệt và vị trí ảnh dưới mục 1.
- Cập nhật [[Mẫu Biên Bản Làm Việc Công Ty Thể Thao Xuân Thiện]], [[index]], memory và skill soạn hồ sơ.
- Nguồn nội dung cố định: [[Mau bien ban lam viec Cong ty The thao Xuan Thien]].

## [2026-11-20] update | Tinh chỉnh bố cục mẫu Xuân Thiện

- Bỏ gạch trang trí đầu trang, chuẩn hóa hai ô tên công ty cùng kích thước và thêm sẵn hai khung ảnh dưới mục 1.
- Đưa dòng “(Ký, ghi rõ họ tên)” sát tên hai công ty.
- Cập nhật mẫu HTML, Wiki, memory và skill soạn hồ sơ.

## [2026-11-20] update | Căn chỉnh tên công ty và thứ tự phần ký Xuân Thiện

- Chia tên mỗi công ty thành hai dòng; giảm cỡ chữ tên Victory để vừa khung và đặt “XUÂN THIỆN” ở dòng thứ hai.
- Đảo phần ký để Công ty Thể thao Xuân Thiện đứng trước Victory.
- Cập nhật mẫu HTML, Wiki, memory và skill soạn hồ sơ.

## [2026-11-20] delete | Gỡ nguồn biểu mẫu cũ trùng loại

- Theo yêu cầu người dùng, xóa các nguồn biểu mẫu cũ liên quan đến biên bản Xuân Thiện, báo giá Victory và hợp đồng nguyên tắc BCA/PDF khỏi `sources/`.
- Cập nhật các Wiki mẫu hiện hành để không còn trỏ đến các nguồn đã xóa; giữ nguyên các mẫu đang dùng và thông tin điều khoản hiện hành.

## [2026-11-20] update | Đồng bộ bố cục biên bản Xuân Thiện với phiếu xuất kho

- Thêm đầu trang nhận diện Victory hai phía, giữ quốc hiệu/tiêu ngữ, dùng các khối xanh nhạt và điểm nhấn xanh Victory theo mẫu phiếu xuất kho.
- Giữ nguyên câu chữ cố định, các khung ảnh và quy cách đã duyệt.
- Cập nhật HTML, Wiki, memory và skill soạn hồ sơ.

## [2026-11-20] update | Đặt quốc hiệu lên đầu mẫu Xuân Thiện

- Gỡ khối nhận diện Victory và thông tin pháp nhân khỏi đầu trang; đặt quốc hiệu/tiêu ngữ ở vị trí đầu tiên.
- Giữ các khối thông tin, điểm nhấn xanh và nội dung đã duyệt; cập nhật Wiki, memory và skill.

## [2026-11-21] update | Định dạng xuất biên bản bàn giao

- Người dùng đặt định dạng mặc định mới: biên bản bàn giao xuất Word `.doc`, không xuất HTML.
- Giữ tệp HTML hiện hành làm mẫu tham chiếu; cập nhật Wiki, chỉ mục, memory và skill.
- Biên bản Xingyu được xuất lại thành Word-compatible RTF trong tệp `.doc`; bỏ bản HTML đầu ra cũ để tránh nhầm.


## [2026-11-21] create | Phiếu xuất kho Hải Vinh số 010

- Lập phiếu PXK-VIC-2026-010 theo ảnh người dùng gửi: 5 hộp mực HP 45, mã CC625AA; đơn giá và thành tiền để trống vì ảnh không nêu giá.
- Dùng địa chỉ và mã số thuế Hải Vinh VN từ danh sách khách hàng. Số phiếu tiếp theo là 011. [[bien-ban/Phieu xuat kho PXK-VIC-2026-010 Hai Vinh CC625AA]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-21] create | Phiếu xuất kho Artiverse Apparel Yên Lư số 011

- Lập phiếu theo ảnh hóa đơn HD041449, gồm máy tính để bàn Dell QVT1260 và màn hình Samsung LS24D300GAEXXV, mỗi loại 1 chiếc. Giá không có trong ảnh nên để trống.
- Lấy mã số thuế và địa chỉ bên nhận từ danh sách khách hàng; số phiếu tiếp theo là 012. [[bien-ban/Phieu xuat kho PXK-VIC-2026-011 Artiverse Apparel Yen Lu HD041449]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-21] create | Phiếu xuất kho Artiverse Apparel Yên Lư số 012

- Lập phiếu theo ảnh: bộ kiểm soát cửa Outdoor và công tắc Datic Basic, mỗi dòng số lượng 1; đơn giá và thành tiền để trống vì ảnh không có giá.
- Dùng thông tin bên nhận trong danh sách khách hàng; số phiếu tiếp theo là 013. [[bien-ban/Phieu xuat kho PXK-VIC-2026-012 Artiverse Apparel Yen Lu]] [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]]


## [2026-11-21] update | Chỉ dùng mẫu DOC cho biên bản bàn giao

- Theo yêu cầu mới nhất, xóa mẫu HTML bàn giao đã dùng để tham chiếu; tạo mẫu Word `.doc` làm mẫu chuẩn duy nhất và đổi toàn bộ hướng dẫn hiện hành sang `.doc`.
- Cập nhật Wiki, mục lục, memory và kỹ năng soạn hồ sơ; lịch sử các biên bản đã lập được giữ nguyên. [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] [[Nguyên tắc giữ nguyên mẫu đã duyệt]]


## [2026-11-21] update | Chuyển mẫu hợp đồng nguyên tắc sang Word

- Chuyển bản tham chiếu Khánh Toàn sang mẫu Word `.docx`, giữ nguyên nội dung, điều khoản và dữ liệu trong bản đã duyệt; kiểm tra lại các điều khoản chính sau khi chuyển.
- Xóa tệp HTML làm mẫu cũ; cập nhật Wiki, mục lục, memory và kỹ năng để chỉ dùng/xuất hợp đồng nguyên tắc dạng Word `.docx`. [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]] [[hop-dong/Mau hop dong nguyen tac mua ban Victory]]


## [2026-11-21] update | Chuyển mẫu bàn giao từ DOC sang DOCX

- Theo yêu cầu mới nhất, chuyển mẫu bàn giao sang Word `.docx`; giữ quy cách đã duyệt, xóa bản `.doc` RTF cũ để tránh trùng.
- Cập nhật Wiki, mục lục, memory và kỹ năng: biên bản bàn giao về sau chỉ dùng/xuất `.docx`. [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] [[bien-ban/Mau bien ban ban giao nghiem thu hang hoa Victory.docx]]

## [2026-11-21] update | Chuẩn hóa quy trình lập hồ sơ Victory

- Chuẩn hóa trường dữ liệu thiếu thành `...` trên bản giấy tờ; giữ nguyên khoảng ký, khung ảnh và cấu trúc mẫu; không sửa dữ liệu nguồn.
- Cập nhật Wiki các mẫu hợp đồng, báo giá, biên bản, phiếu kho, đối chiếu công nợ và đề nghị thanh toán; cập nhật skill soạn hồ sơ và memory, thay quy tắc cũ yêu cầu để trống.
- Tạo [[Quy Trình Chuẩn Hóa Hồ Sơ Victory]] và [[Sổ Theo Dõi Số Văn Bản Victory]]. Số kế tiếp đã kiểm kê: báo giá 112, phiếu xuất kho 013.

## [2026-11-21] update | Cho phép bộ mẫu và biến thể theo khách hàng

- Điều chỉnh cách quản lý: mẫu hiện hành là mặc định cho tình huống phổ biến; có thể lưu mẫu biến thể theo khách hàng/tình huống và ghép nhiều loại chứng từ thành bộ hồ sơ cho cùng một việc.
- Người dùng xác nhận bộ mẫu hiện có đã đủ, chưa tạo thêm loại chứng từ lúc này. Không xóa biến thể có nhu cầu; chỉ dọn bản sao y hệt hoặc mẫu bị thay thế.
- Đồng bộ Wiki, memory và skill soạn hồ sơ. [[Nguyên tắc giữ nguyên mẫu đã duyệt]] [[Quy Trình Chuẩn Hóa Hồ Sơ Victory]]

- Tạo [[Bộ Mẫu Chứng Từ Theo Khách Hàng Và Quy Trình]] để ghi nhận hiện bộ mẫu đã đủ, chưa cần tạo thêm.

## [2026-11-22] ingest | Nghị định 399/2026/NĐ-CP về lương tối thiểu

- Nguồn chính thức: [[Nguồn Nghị định 399-2026-NĐ-CP - Cổng văn bản Chính phủ]].
- Tạo: [[Lương tối thiểu từ ngày 01-01-2027]].
- Ghi nhận mức tháng/giờ theo 4 vùng, ngày hiệu lực 01/01/2027, Nghị định 293/2025/NĐ-CP hết hiệu lực cùng ngày và yêu cầu rà soát thỏa thuận tiền lương.


## [2026-11-23] ingest | Thông tư 149/2026/TT-BTC và ưu đãi tên miền biz.vn

- Nguồn chính thức: [[Nguồn Thông tư 149-2026-TT-BTC - Cổng Chính phủ]]; ban hành 08/10/2026, hiệu lực 23/11/2026.
- Tạo [[Miễn phí tên miền biz.vn cho doanh nghiệp đủ điều kiện từ 2027]]: miễn lệ phí đăng ký và phí duy trì 3 năm cho một tên miền mới nếu doanh nghiệp thỏa điều kiện; chính sách áp dụng từ 01/01/2027.
- Đã cập nhật wiki/index.md. Không phát hiện mâu thuẫn với nội dung Wiki hiện có.

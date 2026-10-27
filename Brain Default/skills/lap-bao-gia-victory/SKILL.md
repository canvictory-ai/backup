---
name: Lập báo giá Victory
description: Lập, kiểm tra và gửi báo giá Victory theo hồ sơ, bảng giá YSS và mẫu đã lưu.
group: Bán hàng
updated: '2026-10-27'
learned_updated: '2026-10-27'
---
## Khi nào dùng
Dùng khi người dùng yêu cầu lập mới, chỉnh sửa, kiểm tra hoặc gửi lại báo giá Victory. Không dùng cho câu hỏi giá thông thường.

## Chuẩn bị
- Đọc mẫu `bao-gia/mau-bao-gia-victory.html` trước khi tạo báo giá.
- Tra khách hàng trong `wiki/Danh sach khach hang Victory.csv`; đối chiếu tên, mã số thuế, địa chỉ hồ sơ và địa chỉ giao hàng.
- Xem các báo giá hiện có và xác minh số in bên trong file.
- Tra từng mặt hàng trong bảng giá YSS theo mã, tên và biến thể tương đương; xác minh quy cách. Chỉ dùng giá người dùng cung cấp khi YSS không có giá khớp hoặc không thể xác định mặt hàng.
- Mặc định số lượng là 1 nếu người dùng không nêu số khác. Áp dụng VAT và yêu cầu ảnh theo chỉ dẫn của người dùng và các mặc định đã lưu.
- Kiểm tra công cụ và cộng sự có sẵn trước khi giao bước nào cho họ. Không giả định workflow đã xóa vẫn chạy.

## Cách chạy
- Lập bản nháp từ mẫu chuẩn và chỉ thay các trường được yêu cầu.
- Khi sửa báo giá có sẵn, đọc đúng tệp đích và ghi nhận nội dung liên quan trước khi sửa.
- Giữ nguyên đầy đủ mô tả, cấu hình và chi tiết hàng hóa từ bảng kê, PDF hoặc tài liệu nguồn. Không rút gọn thành tên hoặc tiêu đề sản phẩm. Nếu nội dung nguồn chưa rõ hoặc thiếu, hỏi người dùng hoặc ghi rõ phần chưa xác minh, không tự điền cấu hình.
- Nếu người dùng gửi tài liệu mới để sửa nội dung hàng hóa, dùng tài liệu mới làm căn cứ đối chiếu chính cho phần được yêu cầu sửa.
- Sau khi sửa, đọc lại chính tệp đích. Đối chiếu từng yêu cầu với nội dung thực tế đã lưu và kiểm tra rằng nội dung yêu cầu đã thay đổi so với bản trước nếu đó là mục cần sửa.
- Nếu nội dung không thay đổi, chưa phản ánh yêu cầu hoặc không xác định đúng tệp, tiếp tục xử lý trước khi báo hoàn tất. Không chỉ lặp lại lời xác nhận từ lần trước.
- Chỉ gửi liên kết tới tệp thực tế đã được tạo hoặc cập nhật.

## Quy trình
1. Chốt khách hàng, địa chỉ giao hàng, mặt hàng, số lượng, đơn giá, VAT và yêu cầu ảnh.
2. Soạn bản nháp từ mẫu đã lưu, chỉ thay các trường cần thiết.
3. Kiểm tra bản nháp với mẫu gốc trực tiếp; không bắt buộc cộng sự kiểm định độc lập và không gọi workflow không còn tồn tại.
4. Đối chiếu cấu trúc, định dạng, logo, địa chỉ giao hàng, nội dung yêu cầu, giá, phép tính và HTML hợp lệ.
5. Đối chiếu nguyên văn phần mô tả và cấu hình hàng hóa với tài liệu nguồn; kiểm tra không bị lược bỏ hoặc chép nhầm.
6. Với yêu cầu sửa, kiểm tra trực tiếp các đoạn đã yêu cầu trong tệp sau khi lưu; xác nhận nội dung hiển thị và không bị giữ nguyên bản cũ.
7. Chỉ đặt phần tổng hợp thuế ngay sau bảng hàng theo bố cục mẫu. Trình bày riêng tiền hàng chịu thuế theo từng mức thuế, tiền VAT tương ứng và tiền hàng không chịu thuế; giữ nhãn và định dạng đúng mẫu đã lưu. Nếu cần để khách nhận biết mặt hàng thuộc nhóm thuế nào, thể hiện nhóm thuế trên các dòng hàng hoặc chia nhóm hàng theo yêu cầu, đồng thời giữ tổng hợp thuế ngay sau bảng hàng.
8. Sau khi tạo hoặc cập nhật file thành công, kiểm tra phép tính, VAT, tổng tiền, bảo toàn mẫu và xác nhận file tồn tại đúng đường dẫn, gửi ngay link cho người dùng. Không yêu cầu kết quả kiểm định độc lập `pass: true`. Nếu thiếu dữ liệu bắt buộc, lỗi mẫu, sai số liệu hoặc không xác nhận được file/đường dẫn, không gửi; nêu rõ lý do.
9. Chỉ xác nhận đã tạo hoặc gửi khi có tệp thực tế hoặc phản hồi thành công từ kênh gửi.
10. Trả lời ngắn bằng tiếng Việt, nêu số báo giá, khách hàng, tiền hàng, VAT và tổng thanh toán.

## Tính tiền và kiểm tra
- Tính thành tiền từng dòng bằng số lượng nhân đơn giá.
- Cộng tiền hàng, VAT và tổng thanh toán; tự tính lại để đối chiếu.
- Xác minh số báo giá từ nội dung file, không dựa riêng vào tên file.
- Đối chiếu khách hàng, mã số thuế, địa chỉ giao hàng, mặt hàng, số lượng, đơn giá, ảnh, thời hạn và các tổng.
- Với số tiền bằng chữ song ngữ, kiểm tra cả phần tiếng Việt lẫn tiếng Anh và đối chiếu với tổng thanh toán bằng số.
- Kiểm tra điều khoản theo đúng yêu cầu của người dùng; không giữ lại dòng thuế nếu người dùng yêu cầu bỏ vì thuế đã có trên bảng kê.

## Bẫy
- Không kết luận YSS không có giá chỉ từ một tìm kiếm tên gần đúng.
- Không ghép địa chỉ công ty khác hoặc bỏ địa chỉ giao hàng.
- Không làm mất logo hoặc dải logo chân trang.
- Không thêm ảnh khi người dùng yêu cầu không có ảnh.
- Không tự thêm phí, chiết khấu, tồn kho, vận chuyển hay cam kết chưa được xác nhận.
- Không rút gọn mô tả hoặc cấu hình hàng hóa trong tài liệu nguồn thành tiêu đề; lỗi chép cấu hình đã xảy ra khi lập VIC-57-2026 theo hội thoại ngày 2026-10-26.
- Không tuyên bố đã giao việc, tạo file hoặc gửi file nếu chưa có bằng chứng.
- Nếu lần chạy bị lỗi đăng nhập, báo trạng thái chưa hoàn tất; không tiếp tục hứa sẽ gửi sau khi chưa có lần chạy thành công.
- Không coi việc đọc thấy nội dung đã có sẵn là bằng chứng rằng yêu cầu sửa mới đã được áp dụng; xác minh nội dung cần sửa trong tệp đích sau thao tác.
- Không tự đổi nhãn hoặc cách nhóm thuế theo suy đoán; đối chiếu mẫu lưu và yêu cầu hiện tại, rồi kiểm tra cả nhóm hàng lẫn phần tổng hợp sau khi sửa.

## Kiểm chứng
- Mở lại tệp đích sau khi lưu và kiểm tra các trường được yêu cầu.
- Đối chiếu mô tả và cấu hình hàng hóa với tài liệu nguồn, bảo đảm đủ chi tiết và đúng nội dung.
- Đối chiếu số tiền bằng chữ với tổng tiền bằng số, gồm cả bản dịch nếu được yêu cầu.
- Xác nhận các điều khoản cần sửa đã hiện diện và các mục cần bỏ không còn trong báo giá.
- Xác nhận file cuối cùng tồn tại tại đúng đường dẫn, rồi gửi ngay link sau khi các kiểm tra trên đạt; không chờ kiểm định độc lập.
- Xác nhận phần tổng hợp thuế nằm ngay sau bảng hàng, các nhóm hàng và mức VAT thể hiện đúng yêu cầu, các dòng tiền cộng lại khớp tổng thanh toán.

## Lịch sử (tự học)
- [2026-10-20] Các workflow báo giá đã bị xóa theo yêu cầu người dùng. Xử lý trực tiếp, không gọi workflow đã xóa.
- [2026-10-20] Hội thoại cho thấy người dùng nhiều lần phản ánh báo giá VIC-23-2026 vẫn không đổi sau khi trợ lý xác nhận đã sửa. Bổ sung bước đọc lại tệp đích, đối chiếu yêu cầu với nội dung thực lưu và không xác nhận hoàn tất chỉ dựa trên lời khẳng định trước đó.
- [2026-10-26] Báo giá VIC-57-2026 bị chép sai cấu hình và rút gọn nội dung hàng hóa; yêu cầu giữ đầy đủ mô tả theo tài liệu nguồn, dùng PDF mới làm căn cứ sửa khi người dùng gửi lại.
- [2026-10-26] Hội thoại ngày 2026-10-26 cho thấy báo giá VIC-57-2026 bị chép sai cấu hình và mô tả hàng hóa bị rút gọn còn tiêu đề. Bổ sung bước giữ nguyên, đối chiếu đầy đủ nội dung theo tài liệu nguồn và không tự suy đoán cấu hình.
- [2026-10-27] Khi sửa VIC-59-2026, định dạng VAT ban đầu sai so với mẫu cũ; bổ sung bước đối chiếu nhãn VAT với mẫu và kiểm tra phần tổng hợp thuế sau khi sửa.
- [2026-10-27] Hội thoại ngày 2026-10-27 cho thấy mục VAT của VIC-59-2026 sai định dạng mẫu cũ, sau đó yêu cầu làm rõ nhóm chịu thuế và không chịu thuế, đồng thời giữ tổng hợp ngay sau dòng hàng. Bổ sung đối chiếu nhãn thuế, cách nhóm mặt hàng và vị trí tổng hợp vào quy trình và kiểm chứng.

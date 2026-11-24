---
type: wiki
status: active
tags: [wiki, máy-tính, chẩn-đoán]
created: 2026-10-31
updated: 2026-11-24
source: [[Nguồn Dell - xử lý máy tính không hình]], [[Nguồn Microsoft - khởi động và phục hồi Windows]]
---

# Lỗi máy tính để bàn có nguồn nhưng không lên hình

Quạt quay hoặc đèn sáng chưa đủ để kết luận máy đã khởi động thành công. Cần tách trường hợp màn hình/kết nối không hiển thị khỏi lỗi POST; quy trình dưới đây chắt lọc hướng dẫn Dell và không thay thế tài liệu riêng của hãng/model khác. [[Nguồn Dell - xử lý máy tính không hình]]

## Trình tự khoanh vùng an toàn

1. Xác nhận màn hình có nguồn và đèn báo; chọn đúng ngõ vào đang dùng (HDMI/DisplayPort/VGA tùy thiết bị). Kiểm tra cáp hình ở hai đầu, thử cáp hoặc màn hình đã biết hoạt động nếu có. [[Nguồn Dell - xử lý máy tính không hình]]
2. Khi tháo cáp hình khỏi máy tính, xem màn hình có tự hiện thông báo hoặc hộp tự kiểm tra hay không. Nếu không có, thử màn hình khác đã xác nhận tốt để khoanh vùng màn hình. [[Nguồn Dell - xử lý máy tính không hình]]
3. Ghi lại hình có xuất hiện lúc logo/POST hay không, có tiếng bíp hoặc đèn chẩn đoán nháy theo chu kỳ không. Nếu có mã đèn/tiếng bíp, tra đúng manual theo model, không suy mã từ model khác. [[Nguồn Dell - xử lý máy tính không hình]]
4. Nếu có hình trong POST rồi mới mất khi Windows tải, ghi nhận mốc này vì hướng kiểm tra có thể chuyển sang driver/khởi động hệ điều hành. Driver đồ họa là một khả năng, không phải kết luận; nếu cần thử Safe Mode, dùng Windows Recovery Environment/Startup Settings theo hướng dẫn Microsoft vì cách vào phụ thuộc phiên bản và thiết bị. [[Nguồn Dell - xử lý máy tính không hình]] [[Nguồn Microsoft - khởi động và phục hồi Windows]]

## Phân nhánh theo triệu chứng

- **Mất nguồn:** không đèn, quạt hay âm báo. Hỏi ổ điện, dây nguồn, công tắc nguồn phía sau bộ nguồn, thiết bị cắm thêm gần đây và có mùi khét/tiếng nổ không. Bước đầu chỉ thử ổ điện đã biết tốt và cắm lại dây ngoài khi máy đã tắt; nếu vẫn im, có mùi khét, tia lửa hoặc dây nóng thì ngắt điện và chuyển kỹ thuật, không mở bộ nguồn. [[Nguồn Dell - xử lý máy tính không hình]]
- **Có điện nhưng không qua POST:** đèn/quạt khởi động rồi dừng, lặp khởi động hoặc có mã chẩn đoán. Hỏi có logo hãng, có thay RAM/linh kiện gần đây, mã đèn/bíp chính xác và model/service tag. Ghi lại chu kỳ nháy/bíp, tra đúng manual; nếu triệu chứng bắt đầu sau thao tác trong case hoặc mã báo CPU/RAM/bo mạch thì kỹ thuật cần kiểm tra trực tiếp. Không suy mã chung. [[Nguồn Dell - xử lý máy tính không hình]]
- **Qua POST nhưng không lên hình:** áp dụng kiểm tra màn hình, cáp và ngõ vào ở trên. Nếu vẫn không có hình với màn/cáp đã thử tốt, chuyển kỹ thuật kiểm tra cổng xuất hình/GPU. Mã Dell ở nguồn chỉ dùng theo model được tài liệu bao phủ. [[Nguồn Dell - xử lý máy tính không hình]]
- **Không vào hệ điều hành:** nếu có logo/BIOS hoặc thông báo “no boot device”, hỏi thông báo nguyên văn, ổ có tiếng lạch cạch, dữ liệu có sao lưu không. Tránh cài lại, reset, format hoặc chạy công cụ ghi lên ổ trước khi xác nhận bản sao lưu; có thể dùng Startup Repair khi hiểu tác động và có khóa BitLocker nếu được yêu cầu. Nếu ổ biến mất, phát tiếng bất thường hoặc dữ liệu quan trọng chưa sao lưu, dừng thử và chuyển kỹ thuật cứu dữ liệu. [[Nguồn Microsoft - khởi động và phục hồi Windows]]
- **Nóng, quạt ồn hoặc tự tắt:** hỏi thời điểm xảy ra, khe thoát gió có bị che, môi trường bụi và có quá nhiệt gần đây không. Để máy tắt nguội, thông thoáng khe gió ngoài và thử lại một lần; nếu tự tắt tiếp, nóng bất thường, có mùi hoặc quạt cạ/rít thì cần vệ sinh và đo kiểm trực tiếp. Không tháo tản nhiệt khi chưa có chuyên môn. [[Nguồn Dell - xử lý máy tính không hình]]
- **Chậm, treo hoặc báo lỗi ổ lưu trữ:** hỏi tiếng ổ, lỗi SMART/BIOS, máy có nhận đúng ổ và dữ liệu đã sao lưu chưa. Nếu còn vào Windows, ưu tiên sao lưu dữ liệu trước; kiểm tra chỗ trống/tình trạng ổ chỉ sau khi có bản sao. Tiếng lạch cạch, ổ lúc nhận lúc mất hoặc lỗi đọc ghi là dấu hiệu dừng thao tác và chuyển kỹ thuật, không chạy sửa lỗi/format. [[Nguồn Microsoft - khởi động và phục hồi Windows]]

## Câu hỏi cần hỏi trước khi kết luận

Ghi model/service tag, triệu chứng bắt đầu lúc nào, có logo/POST không, có đèn hoặc bíp gì (quay video chu kỳ nếu tiện), thiết bị/cáp vừa thay đổi, màn hình báo gì, có nóng/mùi/tiếng lạ không, và dữ liệu đã sao lưu chưa. Chỉ dùng mã đèn, mã bíp, phím chẩn đoán hoặc tháo lắp theo tài liệu đúng model; nếu người dùng không rõ model thì chưa diễn giải mã. [[Nguồn Dell - xử lý máy tính không hình]] [[Nguồn Microsoft - khởi động và phục hồi Windows]]

## Khi trao đổi với khách

Xin khách cung cấp model máy và màn hình, loại cáp/cổng đang dùng, đèn nguồn màn hình, dòng chữ trên màn hình (ví dụ “No Signal”), thời điểm mất hình và mã nháy/bíp nếu có. Với ca ghi nhận ngày 31/10/2026, máy bàn vẫn quay quạt nhưng thiếu model và dấu hiệu màn hình, nên chưa thể xác định nguyên nhân. [[Zalo TESTBOT 2026-10-31 - triệu chứng kỹ thuật]]

## Giới hạn xác minh

Đối chiếu tài liệu Dell và Microsoft trực tuyến ngày 24/11/2026. Đây là hướng khoanh vùng từ xa, không xác nhận linh kiện hỏng. Không mở bộ nguồn, không thao tác phần cứng đang có điện, không reset/cài lại/format ổ trước khi bảo vệ dữ liệu. Mã chẩn đoán và sửa chữa bên trong phụ thuộc đúng model và cần kỹ thuật kiểm tra trực tiếp. [[Nguồn Dell - xử lý máy tính không hình]] [[Nguồn Microsoft - khởi động và phục hồi Windows]] [[Zalo TESTBOT 2026-10-31 - triệu chứng kỹ thuật]]

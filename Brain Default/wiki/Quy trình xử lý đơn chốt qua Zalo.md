---
type: wiki
status: active
tags: [wiki]
origin: javis-learned
created: 2026-11-01
updated: 2026-11-03
source: [[conversations/2026-11-01]]
---
Khi khách xác nhận chốt, chỉ cảm ơn và nhắc lại ngắn gọn hàng/biến thể cùng số lượng đã chốt, không thêm tổng tiền hay lời ngoài lề. Sau đó chuyển theo mẫu “Tên nhóm: đơn khách vừa chốt”. [[conversations/2026-11-01]]

Quy trình áp dụng cả với đơn gửi bằng ảnh; nếu ảnh không rõ hoặc thiếu căn cứ về giá thì hỏi lại, không tự suy đoán. [[conversations/2026-11-01]]

Tin gửi nhóm xuất hàng gồm tên nhóm nguồn, danh sách hàng/biến thể, số lượng, giá và tổng tiền đã xác nhận. Không thêm tên khách, tham chiếu tin gốc, lời dẫn hay diễn giải. Sau khi chuyển, báo chủ chỉ tên nhóm nguồn. [[conversations/2026-11-01]]

Mỗi sự kiện chốt chỉ tạo tối đa một tin chuyển. Chỉ tin mới xác nhận chốt/yêu cầu xuất hàng hoặc trả lời trực tiếp câu hỏi còn thiếu của đúng đơn mới có thể tiếp tục chuyển. Tag Luna, lời nhắc chung, câu “Sao?”, câu hỏi khác hoặc lần chạy lại không mở lại đơn đã xử lý. Đối chiếu ID tin xác nhận mới nhất, nhóm nguồn, mặt hàng/biến thể/số lượng và lịch sử nhóm đích; nếu đơn tương ứng đã có thì dừng. Nếu kết quả gửi không rõ, kiểm tra nhóm đích trước khi retry, không gửi lần hai mù. Chỉ gửi bổ sung khi tin mới nêu thay đổi rõ về hàng, biến thể hoặc số lượng; sửa/hủy phải gắn với đơn gốc. Nếu không xác định được trạng thái hoặc nghi có lượt xử lý song song, dừng và báo chủ trong Javis. Không nói với khách về lỗi hay quy trình nội bộ. [[conversations/2026-11-01]]

XUẤT HÀNG VICTORY (chat_id 8404017101126147877) là nhóm đích nội bộ: Luna im lặng hoàn toàn với mọi tin đến, không trả lời, xử lý, phản ứng hay gửi tin. Chỉ nhánh chuyển đơn cố định của Javis được gửi đơn đã chốt từ nhóm nguồn khác. Luna chỉ chuyển đơn đã chốt từ các nhóm Zalo khác mà kết nối hiện tại cho phép đọc; khả năng đọc không đồng nghĩa với bảo đảm đã đọc mọi tin nhắn lịch sử. [[conversations/2026-11-03]]

## Mâu thuẫn

Một trang quy tắc Zalo khác ghi hệ thống có sổ chuyển theo ID tin nguồn, nhưng lần rà lịch sử hiện tại không trả về ID sự kiện gắn với hai lần gửi hoặc bằng chứng sổ chuyển. Trong TESTBOT, cùng đơn “3 hộp 76A có chip” xuất hiện tại nhóm đích lúc 21:06:40 và 21:12:13 ngày 03/11/2026; giữa hai lần có tin mới “Sao?” và tag Luna, không có xác nhận chốt mới. Nhật ký workflow lúc 21:12:07 nhận tag Luna nhưng kết thúc `Not logged in`; vì vậy chưa xác định được bộ phận nào đã phát lệnh gửi lần hai. Quy tắc trên chặn việc dùng tin nhắc/tag để khôi phục đơn cũ, nhưng cơ chế chống gửi song song ở tầng gửi vẫn cần xác minh. [[conversations/2026-11-03]]

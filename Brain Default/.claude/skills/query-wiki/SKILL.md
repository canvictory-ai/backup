---
name: Query Wiki
description: "Khai thác tri thức trong Second Brain: tổng hợp, so sánh, giả thuyết. Trả lời có trích dẫn."
description_en: "Mine the knowledge held in the Second Brain: synthesis, comparison, hypotheses. Every answer carries citations."
group: AI
---

# QUERY - trả lời từ wiki (có citation, compounding)

## Khi nào dùng

Kích hoạt khi người dùng hỏi/khai thác tri thức trong Second Brain, vd "tổng hợp các
framework về X", "so sánh A vs B vs C", "wiki có gì về Y".

Năm kiểu khai thác: tổng hợp, so sánh, giả thuyết, liệt kê, trực quan hoá. Luôn trả lời
có trích dẫn và lưu lại kết quả giá trị.

1. Đọc `wiki/index.md` TRƯỚC để biết có trang nào.
2. Đọc các trang wiki liên quan (theo nhóm/tên); mở trang đích của wikilink thật nếu cần đủ context.
3. Thiếu -> đọc `sources/` tương ứng. Vẫn thiếu -> append 1 dòng vào `wiki/_open-questions.md`.
4. Trả lời có wikilink tới nguồn thật cho mọi khẳng định cụ thể. Nói rõ chỗ nào wiki chưa cover thay vì bịa.
5. Nếu câu trả lời có kiến thức mới, có nguồn dẫn và có giá trị dùng lại (ví dụ mã tương thích, quy trình, thông số đã xác minh), hãy lưu thật vào brain đang chọn trong cùng lượt: với nguồn web, tạo/cập nhật trang Wiki nguồn ghi URL và ngày truy cập (không tạo nội dung trong `sources/`, đây là lớp nguồn do người dùng quản lý); tạo/cập nhật trang tri thức có citation tới trang nguồn, cập nhật `wiki/index.md` và append `wiki/log.md`. Đọc lại các file và xác nhận wikilink trỏ tới trang có thật trước khi nói đã lưu. URL trong câu trả lời chỉ là trích dẫn, không phải bản ghi tri thức.
6. Nếu người dùng yêu cầu “wiki/lưu”, luôn thực hiện đủ bước lưu ở brain đang chọn; không chuyển sang brain khác, memory, drafts hoặc lịch sử chat làm nơi lưu thay thế. Câu trả lời một lần, không có tri thức tái sử dụng thì không tự tạo Wiki.

7 dạng câu hỏi chất lượng cao: Tổng hợp (bảng so sánh) · So sánh 3+ (ma trận) · Giả thuyết (phân tích ảnh hưởng) · Gán nhãn/liệt kê · Trực quan hoá (canvas/sơ đồ) · Dịch/chuyển ngữ · Tự kiểm gap (append open-questions).

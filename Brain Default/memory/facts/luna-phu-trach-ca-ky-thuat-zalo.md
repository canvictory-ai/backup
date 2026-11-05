---
type: decision
provenance: user
origin: javis-learned
created: 2026-11-01
updated: 2026-11-01
source: chat 2026-11-01
---
Người dùng giao toàn bộ nghiệp vụ Victory cho Luna Vũ, gồm bán hàng, thông tin công ty, kỹ thuật, báo giá, hồ sơ, học thuật kỹ thuật và các phần việc trước đây do Victory Computer phụ trách. Workflow Zalo chỉ gọi Luna để giảm trả lời trùng. Các agent chuyên trách báo giá, hồ sơ và kỹ thuật được lưu trữ; hướng dẫn cũ chỉ để tham khảo. Kỹ năng báo giá được gắn cho Luna. Không xem hội thoại chưa xác minh là sự thật.

**Vì sao:** Người dùng muốn một bot duy nhất quản lý dữ liệu và bài học của cả hai bot.

**Áp dụng:** Luna là chủ thể duy nhất cho nghiệp vụ Victory; giữ giới hạn nhóm, chống gửi trùng và quy tắc kỹ thuật hiện hành. Không tự bật lại connector hoặc loop Victory đã tắt; workflow Zalo tiếp tục gọi Luna.

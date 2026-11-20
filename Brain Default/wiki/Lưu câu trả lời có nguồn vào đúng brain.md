---
type: wiki
status: active
tags: [wiki, javis, quy-trinh]
created: 2026-11-10
updated: 2026-11-10
source: [[skills/query-wiki/SKILL.md]], [[agents/luna-vu]]
---

# Lưu câu trả lời có nguồn vào đúng brain

Một URL xuất hiện trong câu trả lời chỉ là dẫn chứng cho lượt chat; nó chưa tạo bản ghi trong Wiki. Quy trình QUERY cũ cho phép đề xuất lưu kiến thức tái sử dụng thay vì bắt buộc ghi, nên tri thức có thể chỉ còn trong hội thoại hoặc quy trình học agent. [[skills/query-wiki/SKILL.md]]

## Nguyên tắc đã sửa

- Với thông tin mới có nguồn và giá trị dùng lại, tạo/cập nhật trang Wiki nguồn ghi URL và ngày truy cập nếu là nguồn web, sau đó cập nhật trang tri thức có citation; cập nhật `wiki/index.md` và `wiki/log.md`, rồi đọc lại để kiểm tra link đích tồn tại. Không viết nội dung vào `sources/`, đây là lớp người dùng quản lý. [[skills/query-wiki/SKILL.md]]
- Khi người dùng nói “wiki/lưu”, hoàn tất ghi Wiki ngay trong lượt hiện tại; không xem tin nhắn trả lời, memory, drafts hoặc một brain khác là nơi lưu thay thế. [[AGENTS.md]]



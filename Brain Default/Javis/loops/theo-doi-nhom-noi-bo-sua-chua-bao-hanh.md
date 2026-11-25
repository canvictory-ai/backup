---
type: loop
name: "Theo dõi nhóm Nội bộ Sửa chữa - Bảo hành"
slug: theo-doi-nhom-noi-bo-sua-chua-bao-hanh
enabled: false
mode: auto
goal: custom
interval_min: 5
owner_chat: "web:8914475cbb74426ebc11210134e782e7"
agent: "dich-vu-theo-doi-cong-viec"
updated: 2026-11-25
---

Theo dõi nhóm Zalo Nội bộ | Sửa chữa - Bảo hành - Việc phát sinh (threadId 2433597573334150721). Mỗi lượt đọc sổ /brains/Brain Default/loop-data/noi-bo-sua-chua-viec.json và lấy tin mới kể từ last_processed_message_id/last_processed_at; đối chiếu nguồn và thời điểm. Tạo hoặc cập nhật đúng việc theo ID/mạch trao đổi, không gộp hai việc chỉ vì giống nội dung. Việc chưa rõ giữ trạng thái chờ/chưa xác minh, không tự kết luận xong, tự chẩn đoán, báo giá, hứa hạn hay giao việc. Hạn chỉ ghi khi tin nêu rõ; mặc định mọi người phụ trách, trừ khi có người được nêu cụ thể. Khi thành viên xác nhận xong rõ việc nào, xóa hẳn mục đó khỏi tasks, không giữ lịch sử hoàn tất. Khi ai hỏi việc còn phải làm, Luna Vũ xử lý theo mẫu đã lưu trong hồ sơ; vòng theo dõi chỉ cập nhật sổ, không gửi tin vào nhóm. Ghi last_processed_message_id và last_processed_at sau khi xử lý lịch sử đồng bộ đầy đủ; nếu sync không đầy đủ hoặc có gap thì giữ mốc chưa xác minh, báo chủ và không kết luận không có tin. Không đọc hay ghi tin sang nhóm khác. Tóm tắt ngắn cho chủ qua khung chat khi có việc mới, hoàn tất, quá hạn, chưa rõ hoặc lỗi đồng bộ.

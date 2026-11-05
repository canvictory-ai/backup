---
superseded_by: victory-computer-da-duoc-bat-lai
type: decision
provenance: user
origin: javis-learned
created: 2026-11-01
updated: 2026-11-02
source: chat 2026-11-01
---
Chủ đã giao toàn bộ nghiệp vụ Victory Computer cho Luna Vũ và yêu cầu Victory Computer không làm bất kỳ việc gì. Thực tế kiểm tra ngày 02/11/2026: chatbot chuyên trách Victory Computer đã được tắt qua giao diện quản lý; trạng thái trả về `enabled=false`, `running=false`, `state=off`. Kết nối MCP “Victory Computer” cũng đang `enabled=false`; loop trực Zalo Victory Computer có `enabled: false`; bộ phán xử của bot có hồ sơ tạm dừng; workflow Zalo chỉ gọi Luna. Các cấu hình và lịch sử cũ được giữ lại, không vận hành.

**Vì sao:** Người dùng muốn Luna nhận toàn bộ phần việc trước đây của Victory, đồng thời tránh kích hoạt hai bot song song.

**Áp dụng:** Không để chatbot Victory nhận hoặc trả lời tin, không để kết nối/loop/bộ phán xử Victory hoạt động. Luna là đầu mối xử lý nghiệp vụ Victory. Chỉ kích hoạt lại Victory khi chủ giao việc mới rõ ràng.


## Lịch sử
- [2026-11-02] Bị thay thế bởi [[victory-computer-da-duoc-bat-lai]] (user đổi thông tin).

---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer NX200 - tra cứu cấu hình

**Loại thiết bị:** Router SIM 5G. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-nx200/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer NX200 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-nx200/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: REV1.0.0

[User Guide Archer NX200 REV1.0.0](https://static.tp-link.com/upload/manual/2025/202503/20250324/Archer%20NX200_UG_REV1.0.0.pdf). Chương 2 §2.2 tr. 8-9: tắt modem nếu có; SIM nano lắp chiều tiếp điểm vàng quay phải đến khi khớp, hoặc dùng EWAN cắm modem vào WAN; không cần nối cả hai đường. Chương 4 Quick Setup §4.1 tr. 14; manual setup §4.3 tr. 16-18 chọn MBB hoặc EWAN; Mobile WAN ở `Advanced > Network > Mobile WAN`, EWAN ở `Basic > Internet`, có tùy chọn VLAN nhưng ISP phải cấp giá trị. Nhấn `Save`; kiểm tra bằng `Advanced > System Tools > Diagnostics`, §4.4 tr. 19, bấm `Start`. Wi-Fi ở `Basic > Wireless` hoặc `Advanced > Wireless > Wireless Settings`, nhập SSID/mật khẩu và `Save`, chương 6 tr. 46-47.

Với SIM, guide đưa profile/APN/username/password/PDP/authentication theo thông tin nhà mạng; không dùng giá trị ví dụ. FAQ về Mobile WAN yêu cầu kiểm tra profile, PIN, data limit, Mobile Data và roaming với ISP (FAQ Q6).

**Mức xác minh:** đã đọc guide REV1.0.0 cho các mục trên; bìa không xác định vùng. Chưa biết nhãn máy nên không thể xác nhận đúng bản cho thiết bị thực tế.

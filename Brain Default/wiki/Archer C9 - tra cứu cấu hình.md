---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C9 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c9/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C9 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c9/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở, Archer C9 US REV4.0.0

[User Guide chính hãng US REV4.0.0](https://static.tp-link.com/Archer%20C9%28US%29_V3_User%20Guide.pdf). Đã đọc chương 2 §2.2 Connect Your Router (tr. 6-8) và chương 4 §4.2 Internet (tr. 14-16): modem vào cổng Internet, khởi động modem trước router, đèn báo và cách nối máy cấu hình; vào `Basic > Internet`, chọn loại theo ISP, `Save`, kiểm tra `Network Map`. WAN có Dynamic IP, Static IP, PPPoE, L2TP/PPTP; PPPoE/tunnel và thông số phụ cần ISP cung cấp. Nếu không có Internet, guide dẫn đến FAQ.

**Mức xác minh:** chỉ US REV4.0.0; guide EU/UN hoặc revision khác không được suy theo. Chưa đọc sâu Wi-Fi và FAQ; không có tem máy để đối chiếu vùng/revision thực tế.

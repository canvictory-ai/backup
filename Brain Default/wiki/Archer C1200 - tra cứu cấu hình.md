---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C1200 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c1200/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C1200 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c1200/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở, Archer C1200 REV2.0.0 (EU/US) và US V3

Đã mở [User Guide REV2.0.0 EU/US](https://static.tp-link.com/1910012083_Archer%20C1200%28EU%29%26%28US%29_V2_User%20Guide.pdf), bìa nêu Archer C1200 REV2.0.0; đã đọc thiết lập Quick Setup, `Basic > Internet`, các loại kết nối và lưu/kiểm tra ở chương 4, tr. 12-18. Tài liệu chính hãng khác [PDF US V3](https://static.tp-link.com/1910012083_Archer%20C1200%28US%29_V3_User%20Guide.pdf) có trang bìa ghi REV2.0.0; phần §2.2 Connect Your Router, tr. 6, hướng dẫn modem sang cổng Internet/WAN, cấp nguồn và kiểm tra đèn.

- Modem nối đến cổng Internet/WAN; nếu Ethernet từ tường thì nối trực tiếp cổng này. Khởi động modem rồi router; trạng thái đèn Power/Internet/2.4G/5G được nêu tại chương 2 §2.2.
- Thiết lập lần đầu qua `Quick Setup`; cấu hình thủ công tại `Basic > Internet`. Chọn loại kết nối theo ISP; tài liệu nêu Dynamic IP, Static IP, PPPoE và các dạng tunnel. Nhấn `Save`; kiểm tra tại `Network Map` sau khi đợi 1-2 phút (chương 4, tr. 12-18).
- Tham số phụ, tài khoản PPPoE và thông tin IP phải do ISP xác nhận. FAQ có mục khi không truy cập Internet (mục lục tr. 96, guide US V3).

**Mức xác minh:** guide biến thể REV2.0.0 đã đọc một phần; US V3 cũng được mở và đọc phần đấu nối. Chưa biết tem máy/vùng nên chưa xác minh đúng máy; chưa đọc hết Wi-Fi và FAQ theo từng biến thể.

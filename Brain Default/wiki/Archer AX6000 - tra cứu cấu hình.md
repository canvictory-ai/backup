---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX6000 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-ax6000/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer AX6000 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-ax6000/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở, Archer AX6000 US REV1.3.0

[User Guide chính hãng, PDF trực tiếp US REV1.3.0](https://static.tp-link.com/upload/manual/2023/202311/20231108/1910013553_Archer%20AX6000%28US%29%201.0_UG_REV1.3.0.pdf). Mục lục ghi chương 2 phần kết nối tr. 6-8, chương 4 Internet tr. 12-18, §12.7 Wi-Fi tr. 74-76 và chương 13 §13.3 Diagnostics tr. 83. Đã mở các phần kết nối, Wireless và diagnostics; không suy các chi tiết này sang V2.0.0 hoặc REV1.2.0.

- Kết nối modem với cổng WAN theo chương 2; Ethernet từ tường có thể vào cổng WAN khi ISP cấp Ethernet.
- Cấu hình Internet ở `Basic > Internet`; loại kết nối và thông tin đăng nhập/IP theo ISP. Guide US REV1.3.0 nêu các trang WAN trong chương 4; không đặt giá trị thay ISP.
- Wi-Fi ở `Basic > Wireless` hoặc `Advanced > Wireless > Wireless Settings`, đặt SSID và mật khẩu rồi lưu (§12.7).
- Chẩn đoán bằng Ping/Traceroute tại mục Diagnostics, chương 13 §13.3, tr. 83.

**Mức xác minh:** đã mở guide US REV1.3.0, nhưng chưa khớp vùng/revision máy thực tế; các guide US REV1.2.0 và V2.0.0 cũng tồn tại nhưng chưa đọc, nên không gộp nội dung.

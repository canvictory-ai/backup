---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C20 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c20/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C20 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c20/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc, phạm vi kết quả (24/11/2026)

[User Guide Archer C20 EU, REV6.2.0](https://static.tp-link.com/upload/manual/2026/202604/20260417/1910013835_Archer%20C20%28EU%29_UG_REV%206.2.0.pdf). Mục lục xác nhận Connect Your Router (ch. 2, tr. 7-9), login (ch. 3, tr. 10), cấu hình router (ch. 4), Wireless Settings §4.6 (tr. 36-38), connectivity/troubleshooting trong các mục quản trị/FAQ. Chương 2 (tr. 7-9): WAN từ modem tắt nối bằng Ethernet, bật modem chờ khoảng 2 phút, cấp nguồn router, xác nhận LED Power/2.4G/5G/Internet; máy tính nối LAN hoặc Wi-Fi theo nhãn. Ch. 4 §4.3.2 (tr. 18-19): `Advanced > Network > Internet`, chọn kiểu kết nối theo ISP và `SAVE`. §4.6: `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, SSID/mật khẩu và lưu.

Guide EU REV6.2.0; chưa xác nhận nhãn/vùng của máy. Router Ethernet, không DSL/SIM/APN. Thông số WAN/PPPoE/VLAN cần ISP xác nhận.

**Còn thiếu:** mở sâu mục setup WAN và diagnostics/FAQ của guide để ghi các loại WAN mà phiên bản này hỗ trợ, đường kiểm tra kết nối, bước xử lý lỗi; xác nhận máy khớp EU V6.2.0. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

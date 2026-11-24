---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX90 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-ax90/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer AX90 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-ax90/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: REV1.0.0

[User Guide chính hãng Archer AX90 REV1.0.0](https://static.tp-link.com/2020/202009/20200917/1910012880_Archer%20AX90US%29_UG_REV1.0.0.pdf). PDF có chương 2 đấu nối tr. 7-9; chương 4 Quick Setup/manual Internet tr. 13-16; Wi-Fi chương 6 §§6.1 tr. 28-29; FAQ có mục lục ch. 16. Đã đọc §2.2: modem vào cổng 2.5 Gbps WAN/LAN, hoặc Ethernet tường vào cổng này; bật modem trước, đợi khoảng 2 phút, cấp nguồn router và xác nhận đèn. Đăng nhập `tplinkwifi.net`, tạo mật khẩu, Quick Setup. WAN thủ công tại `Internet`, chọn port WAN và loại kết nối; Dynamic IP, Static IP, PPPoE, L2TP, PPTP; nhập theo ISP, `Save`. Wi-Fi tại `Wireless` hoặc `Advanced > Wireless > Wireless Settings`; SSID/mật khẩu rồi `SAVE`. FAQ được guide gọi là bước tiếp nếu mất Internet.

**Mức xác minh:** guide REV1.0.0 mở và thao tác chính đã đọc; tên tệp chứa `US`, nhưng bìa không tuyên bố rõ vùng, vì vậy vùng guide chưa được xác nhận. Chưa khớp tem máy và thiếu đọc sâu FAQ/test chi tiết. ISP xác nhận tham số WAN.

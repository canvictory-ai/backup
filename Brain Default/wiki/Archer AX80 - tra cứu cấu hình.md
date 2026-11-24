---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX80 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-ax80/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer AX80 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-ax80/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở, biến thể Archer AX80 REV2.0.0

[User Guide chính hãng, PDF trực tiếp REV2.0.0](https://static.tp-link.com/upload/manual/2024/202403/20240325/Archer%20AX80%20User%20Guide_REV2.0.0.pdf). Đã mở mục lục và đọc chương 2 §2.2 (cắm thiết bị, tr. 8), chương 4 §4.3 (WAN, từ tr. 15), chương 7 §7.1 (Wi-Fi, tr. 32-34), chương 16 §16.8 (Diagnostics, tr. 119). Một tài liệu khác tìm được cho EU REV1.0.0 nhưng chưa dùng thay cho REV2.0.0: [PDF EU REV1.0.0](https://static.tp-link.com/upload/manual/2023/202301/20230109/Archer%20AX80%28EU%29%20User%20Guide_REV1.0.0.pdf).

- Cắm modem vào cổng WAN theo chương 2 §2.2, cấp nguồn, kết nối máy cấu hình qua Ethernet hoặc Wi-Fi.
- WAN ở `Internet`; các loại được guide REV2.0.0 nêu gồm Dynamic IP, Static IP, PPPoE, L2TP, PPTP. Thông tin tài khoản/tham số theo ISP; `Save` theo hướng dẫn cấu hình Internet.
- Wi-Fi tại `Wireless` hoặc `Advanced > Wireless > Wireless Settings`; đặt SSID/mật khẩu, `SAVE` (§7.1).
- Kiểm tra Ping/Traceroute tại `Advanced > System > Diagnostics` (§16.8). Đây là phép kiểm tra trong giao diện, chưa thực hiện trên thiết bị.

**Mức xác minh:** guide REV2.0.0 đã đọc các phần nêu trên; không xác định đây là revision/vùng của thiết bị cụ thể, không áp dụng guide EU REV1.0.0 nếu tem máy không khớp.

---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX73 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-ax73/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer AX73 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-ax73/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.



## Guide đã đọc theo biến thể (24/11/2026)

### User Guide REV1.1.0

[PDF chính hãng](https://static.tp-link.com/upload/manual/2022/202202/20220210/1910013032_Archer%20AX73_UG_REV1.1.0.pdf). Chapter 2 §2.2 (tr. 8-9): cổng WAN nối modem đã tắt bằng Ethernet, bật modem chờ khoảng 2 phút, cấp nguồn router, xác nhận LED rồi nối client LAN/Wi-Fi. Chapter 4 §§4.1-4.3 (tr. 14-17): Quick Setup web/Tether; thủ công tại `Internet`, chọn Dynamic IP/Static IP/PPPoE/L2TP/PPTP theo ISP, `SAVE`; Network Map/Status kiểm tra trạng thái. Chapter 6 Wireless Settings (tr. 27-32): `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, SSID/mật khẩu, lưu `SAVE`. Chapter 15 §15.8 Test Network Connectivity (tr. 108): Diagnostics.

### User Guide REV2.0.1

[PDF chính hãng](https://static.tp-link.com/upload/manual/2025/202501/20250109/1910013878_Archer%20AX73_UG_REV2.0.1.pdf). Chapter 2 §2.2 (tr. 8-9), Chapter 4 §4.3 (tr. 14-17), Chapter 7 §7.1 Wireless Settings (tr. 31-33), Chapter 16 §16.8 connectivity diagnostics (tr. 116). Với REV2.0.1, hướng dẫn Wi-Fi xác nhận `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, đặt SSID/password rồi `SAVE`; Diagnostics tại `Advanced > System > Diagnostics`. Không gán số chương/menu giữa V1.1.0 và REV2.0.1 nếu chưa đối chiếu riêng.

**Mức xác minh:** đã mở và đọc hai guide, nhưng chưa xác minh máy thực tế do thiếu Hardware Version/vùng trên nhãn. WAN Ethernet; không DSL/SIM/APN. PPPoE credentials, IP, VLAN/bridge cần ISP xác nhận. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C64 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c64/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C64 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c64/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc, phạm vi kết quả (24/11/2026)

[User Guide Archer C64 EU REV1.0.0](https://static.tp-link.com/upload/manual/2025/202509/20250911/1910012999_Archer%20C64%28EU%29_UG.pdf), mục lục xác nhận Chapter 2 §2.2 (tr. 8), Chapter 4 §§4.1-4.3 (tr. 14-16), Chapter 11 §11.6 Wireless Settings (tr. 55-56), Chapter 12 §12.7 Test the Network Connectivity (tr. 68), FAQ (tr. 74). Chapter 4 §4.3 nêu `http://tplinkwifi.net` > `Internet`, chọn Dynamic IP/Static IP/PPPoE/L2TP theo ISP; Chapter 11 nêu `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, chỉnh SSID/password và `SAVE`; Diagnostics là `Advanced > System > Diagnostics`.

Guide ghi biến thể EU REV1.0.0; chưa biết nhãn/vùng thiết bị thực tế. Cắm Ethernet WAN vào modem, không có DSL/SIM/APN. PPPoE, thông số IP, VLAN/bridge và credential cần ISP cấp. Không khẳng định tương thích vùng/revision khác.

**Còn thiếu:** đối chiếu nhãn Hardware Version/vùng và guide đúng thiết bị; đọc chi tiết thứ tự đấu nối và troubleshooting FAQ thay vì áp dụng hướng dẫn chung. Chưa thay đổi thiết bị hoặc thử đăng nhập. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

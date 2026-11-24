---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C80 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c80/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C80 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c80/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc, phạm vi kết quả (24/11/2026)

[User Guide Archer C80, REV1.0.1](https://static.tp-link.com/2021/202104/20210422/1910012744_Archer%20C80_UG_V4.pdf). Chương 2 §2.2 (tr. 8-9): WAN nối modem hoặc Ethernet wall, bật modem chờ khoảng 2 phút, cấp nguồn router và kiểm tra LED; chương 4 §4.3 (tr. 15-17): web `http://tplinkwifi.net`, WAN theo ISP và Save; chương 11 §11.6 Wireless Settings (tr. 55-56): `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, đặt SSID/password, `SAVE`; chương 12 §12.7 (tr. 68): `Advanced > System > Diagnostics`.

PDF ghi REV1.0.1; vùng bán không xác định trong nội dung đã đọc. Trang tìm được có tên tệp V4 nhưng bìa PDF ghi REV1.0.1, vì vậy lấy revision trên bìa làm căn cứ và không suy ra V4. Không có DSL/SIM/APN. PPPoE, IP tĩnh, VLAN/bridge và thông tin truy cập do ISP xác nhận.

**Còn thiếu:** đối chiếu nhãn Hardware Version/vùng; mở FAQ để ghi bước xử lý tiếp nếu test lỗi. Chưa thao tác thiết bị hoặc thử credentials. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

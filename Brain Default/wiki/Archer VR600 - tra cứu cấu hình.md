---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer VR600 - tra cứu cấu hình

**Loại thiết bị:** Modem-router DSL. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-vr600/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer VR600 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-vr600/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: Archer VR600 EU REV1.1.0

[User Guide chính hãng EU REV1.1.0](https://static.tp-link.com/res/down/doc/Archer_VR600%28EU%29_V1_UG.pdf). Đã đọc sơ đồ §2.2 tr. 10-11: phone jack qua splitter vào DSL, hoặc dùng cổng LAN4/WAN khi chạy wireless router mode; chờ DSL LED ổn định rồi kết nối máy qua LAN/Wi-Fi. Quick Setup §4.1 và cấu hình thủ công §4.2 tr. 15; vào `Basic > Internet`, ISP list điền VPI/VCI/VLAN nếu có hồ sơ nhà cung cấp; `Other` thì nhập các thông tin ISP cấp. Nhấn `Save`; xem/sửa tại `Advanced > Network > Internet`. Kiểm tra `Advanced > System Tools > Diagnostics`, §4.4 tr. 18, bấm `Start`. Wi-Fi: §12.2.1 `Specify Basic Wireless Settings`, tr. 68; guide hướng tới Network Name/password và lưu.

**Mức xác minh:** EU REV1.1.0 đã đọc các mục này; tìm thấy các guide riêng REV1.0.1, REV2.0.0 và REV3.0.0 nhưng chưa mở sâu, không trộn nội dung. Chưa khớp tem thiết bị. VPI/VCI/VLAN, DSL modulation, PPPoE account phải ISP xác nhận.

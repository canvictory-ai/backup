---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer VR300 - tra cứu cấu hình

**Loại thiết bị:** Modem-router DSL. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-vr300/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer VR300 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-vr300/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: EU REV1.0.0

[User Guide chính hãng Archer VR300 EU REV1.0.0](https://static.tp-link.com/1910012157_Archer%20VR300%28EU%29_V1_UG.pdf). Đã đọc §2.2 sơ đồ đấu nối tr. 7: phone jack qua splitter vào DSL, hoặc nối thẳng cổng điện thoại nếu không cần dịch vụ thoại; cấp nguồn, đợi đèn và dùng LAN/Wi-Fi theo SSID trên nhãn. Quick Setup §4.1, cấu hình WAN §4.2, test §4.3 tr. 12-13; menu `Basic > Internet`, chọn ISP hoặc `Other`, DSL modulation và thông tin kết nối theo ISP; nhấn `Save`; kiểm tra bằng `Advanced > System Tools > Diagnostics` và `Start`. Ví dụ VLAN 101/PPPoE trong ảnh là minh họa, không phải cấu hình khuyến nghị.

**Mức xác minh:** đọc guide EU REV1.0.0. TP-Link còn có EU REV1.2.0 guide riêng, chưa dùng thay cho REV1.0.0. Chưa khớp revision/vùng máy; thiếu đọc sâu Wi-Fi và FAQ. ISP cần xác nhận VPI/VCI, VLAN, loại DSL, PPP credentials.

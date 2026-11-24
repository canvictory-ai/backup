---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer MR200 - tra cứu cấu hình

**Loại thiết bị:** Router SIM 4G. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-mr200/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer MR200 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-mr200/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: EU REV2.0.0

[User Guide chính hãng Archer MR200 EU REV2.0.0](https://static.tp-link.com/1910012062_ArcherMR200%28EU%29_V2_UG.pdf). Đã đọc §2.3, tr. 7-9: gắn anten hướng lên, SIM vào khe đến khi khớp; Micro/Nano SIM cần adapter cỡ chuẩn; nối nguồn, máy tính vào LAN hoặc dùng SSID/mật khẩu trên tem. Quick Setup §4.1 và connection profile §4.2 tr. 13-14; cấu hình thủ công tại `Advanced > Network > Internet`; profile di động/APN do nhà mạng cung cấp. Kiểm tra kết nối tại `Advanced > System Tools > Diagnostics`, §4.3 tr. 15. Wi-Fi `Basic > Wireless`, §11.5.1 tr. 49; lưu bằng `Save`.

**Mức xác minh:** đọc guide EU REV2.0.0 cho các thao tác trên; chưa biết phiên bản/vùng của thiết bị cụ thể. Không nhập APN mẫu trong hình vì đó là dữ liệu minh họa theo mạng khác; xin APN, PDP type, xác thực và roaming từ ISP/nhà mạng. Nếu không có tín hiệu, guide khuyên kiểm tra dịch vụ SIM và đặt router nơi có sóng tốt (§1.2, tr. 4).

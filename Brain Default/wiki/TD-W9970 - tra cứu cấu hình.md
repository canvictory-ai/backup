---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# TD-W9970 - tra cứu cấu hình

**Loại thiết bị:** Modem-router DSL. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/td-w9970/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ TD-W9970 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/td-w9970/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở: REV4.0.0 và QIG V1

[User Guide REV4.0.0](https://static.tp-link.com/2020/202001/20200114/1910012731_TD-W9970_UG_REV4.0.0.pdf) có mục lục cụ thể: đấu nối §2.2 tr. 9; Quick Setup/manual WAN/test §4.1-4.3 tr. 14-15; Wi-Fi §13.4 tr. 70-75; 3G/4G backup §13.1 tr. 62-64. [Quick Installation Guide TD-W9970/TD-W9970B V1 REV1.0.2](https://static.tp-link.com/resources/document/TD-W9970_V1_QIG.pdf) đã đọc toàn văn: splitter/phone jack và cổng VDSL, kiểm tra Power/DSL/Wireless LED, đăng nhập giao diện, Quick Setup, chọn region/time zone, nhập ISP parameters, tùy chọn 3G/4G backup, Wi-Fi, `Save` rồi `Finish`; FAQ kiểm tra cáp, VPI/VCI/connection type/tài khoản với ISP. QIG này ghi rõ TD-W9970 dùng làm hình minh họa và không dùng làm bằng chứng cho REV4.0.0.

**Mức xác minh:** User Guide cụ thể REV4.0.0 đã mở và mục lục đối chiếu; QIG trực tiếp V1 REV1.0.2 đã đọc. Chưa đọc sâu nội dung UG REV4 theo từng thao tác, và chưa có nhãn máy/vùng nên không thể kết hợp quy trình hai biến thể. VPI/VCI, encapsulation, PPP credentials phải ISP xác nhận; không dùng giá trị minh họa của QIG.

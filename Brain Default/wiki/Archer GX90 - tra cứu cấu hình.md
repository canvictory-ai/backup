---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer GX90 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-gx90/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer GX90 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-gx90/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide và QIG đã mở: US REV1.0.0

[User Guide Archer GX90 US REV1.0.0](https://static.tp-link.com/2021/202101/20210107/1910012816_Archer%20GX90%28US%29_UG_REV1.0.0_V2.pdf) và [Quick Installation Guide US REV1.0.0](https://static.tp-link.com/2020/202011/20201119/7106508927_Archer%20GX90%28US%29_QIG_V1.pdf). User Guide mục lục có §2.2 đấu nối tr. 8, chương 4 Quick Setup/WAN tr. 13-17, Wi-Fi §12.6 tr. 75, quản lý/test kết nối chương 13. QIG đã đọc trang hỗ trợ: WAN/LAN 1Gbps có thể chọn trong setup hoặc sau đó vào `Internet > Internet Port` trên giao diện web, hoặc `Tools > Internet Connection > Internet Port` trong Tether. QIG FAQ về mất Internet yêu cầu khởi động modem/router, xác nhận Internet của modem, kiểm tra Network Map/địa chỉ IP WAN, rồi chạy Quick Setup hoặc kiểm tra cáp; nếu modem cable thì hướng dẫn MAC clone.

**Mức xác minh:** hướng dẫn US REV1.0.0; chưa khớp thiết bị thực tế. User Guide full chưa đọc sâu WAN/Wi-Fi; QIG là nguồn rõ cho chọn port và troubleshooting nhưng không thay cho các phần còn thiếu. Thông tin WAN theo ISP.

---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer BE230 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-be230/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer BE230 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-be230/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Quick Installation Guide đã mở trực tiếp: REV1.0.0

**Mức xác minh:** đã đọc QIG Archer BE230 1.0, REV1.0.0. Bìa xác nhận phiên bản tài liệu; QIG không nêu rõ thị trường áp dụng trên phần bìa đã đọc và chưa đối chiếu tem thiết bị. Đây là xác minh quy trình theo QIG, chưa phải xác minh máy cụ thể.

- [Quick Installation Guide PDF trực tiếp](https://static.tp-link.com/upload/manual/2024/202403/20240313/7106510964_Archer%20BE230%201.0_QIG_V1.pdf): hướng dẫn cài đặt nhanh tr. 1; FAQ xử lý tr. 1-2.
- Sơ đồ/cắm dây: tắt modem, nối cổng Ethernet modem tới cổng Internet màu xanh 2.5Gbps của router; bật modem, chờ khoảng 2 phút rồi cấp nguồn router. QIG mô tả hoàn tất khi đèn báo theo sơ đồ sáng ổn định.
- Thiết lập lần đầu: dùng ứng dụng Tether, `+ > Wireless Router > Standard Routers`, hoặc trình duyệt tới `tplinkwifi.net`/`192.168.0.1`; tạo mật khẩu quản trị và làm theo thiết lập. QIG không nêu PPPoE/VLAN/APN cụ thể.
- FAQ nếu không vào Internet: khởi động lại modem, chờ 5 phút; thử máy tính nối trực tiếp modem; xem WAN IP trong Network Map. Nếu WAN IP hợp lệ, QIG hướng dẫn thử DNS `8.8.8.8`/`8.8.4.4` tại `Advanced > Network > Internet`; nếu không hợp lệ, kiểm tra phần cứng/ISP và hỏi ISP, có nêu MAC clone cho trường hợp modem/ISP ràng buộc MAC. DNS là bước troubleshooting trong QIG, không phải cấu hình bắt buộc hay giá trị ISP.
- QIG không mô tả chi tiết tách riêng bước cấu hình SSID/mật khẩu Wi-Fi, lưu từng trường, hay kiểm tra bằng bài test độc lập ngoài đèn và Network Map. Các mục đó còn cần User Guide cùng revision. Thông số WAN/PPPoE/VLAN do ISP xác nhận.

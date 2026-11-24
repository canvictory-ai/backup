---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer MR100 - tra cứu cấu hình

**Loại thiết bị:** Router SIM 4G. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-mr100/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer MR100 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-mr100/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## User Guide đã mở trực tiếp: TL-MR100 EU REV1.0.0

**Mức xác minh:** đã mở và đọc phần chính của User Guide TL-MR100 EU REV1.0.0. Tài liệu dùng tên TL-MR100, không phải Archer MR100; trang này được gắn theo model trong danh sách, cần đối chiếu nhãn/model chính xác trước khi áp dụng. EU REV1.0.0 chưa được xác nhận khớp thiết bị cụ thể.

- [User Guide PDF trực tiếp](https://static.tp-link.com/upload/manual/2022/202205/20220504/1910012970_TL-MR100%28EU%29_UG_REV1.0.0.pdf): §2.2 tr. 7-8, §3 đăng nhập tr. 10-11, ch. 4 setup/profile/test tr. 12-15, §10.5 Wi-Fi tr. 47+, FAQ tr. 66+.
- SIM: cắm Nano SIM theo hình, mặt tiếp xúc vàng xuống, anten dựng thẳng, cấp nguồn; nối máy tính bằng LAN hoặc dùng SSID/mật khẩu trên nhãn. Guide xác định SIM Nano, không suy ra từ model khác.
- Setup: mở giao diện quản trị theo §3, chạy Quick Setup §4.1. Có profile kết nối §4.2; nếu không nhận cấu hình ISP tự động, thông tin APN/xác thực/PIN phải do nhà mạng cấp. §4.3 là bài kiểm tra Internet; đèn Internet tắt thì xem FAQ và xác nhận dịch vụ với ISP.
- Wi-Fi: cấu hình tại `Wireless Settings` §10.5; nội dung menu có mục Basic Wireless Settings. Lưu sau khi thay đổi theo giao diện. PPPoE/VLAN chỉ liên quan khi dùng cổng Ethernet ở Wireless Router Mode §4.4; cấu hình ISP phải hỏi nhà mạng.
- Còn thiếu trích chi tiết từng tùy chọn APN và toàn bộ các bước FAQ cụ thể. Hardware Version trên tem chưa biết; không áp dụng cho biến thể EU khác revision.

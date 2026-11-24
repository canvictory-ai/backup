---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX12 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-ax12/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer AX12 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-ax12/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## User Guide đã mở trực tiếp: Archer AX12 EU V1 REV1.0.0

**Mức xác minh:** User Guide hãng cho nhóm Archer AX12/AX17/AX18, EU V1, REV1.0.0 đã mở và đọc phần cài đặt router. Phần này khớp tên model và revision V1 trong guide, nhưng cần đối chiếu tem máy và vùng mua trước khi áp dụng.

- [User Guide PDF trực tiếp](https://static.tp-link.com/upload/manual/2023/202309/20230905/1910013387_Archer%20AX12%26AX17%26AX18%201.0_UG_V1.1.pdf): bìa REV1.0.0; §2.2 tr. 8-10; §3 đăng nhập tr. 11-12; §4.1-4.3 setup/WAN tr. 14-16; §7.1 Wi-Fi tr. 31-32; §16.8 diagnostics tr. 93-94; FAQ sau tr. 101.
- Cắm nối: modem tắt, nối modem vào WAN bằng Ethernet; modem từ Ethernet outlet có thể nối thẳng Internet/WAN port. Khởi động modem và chờ khoảng 2 phút, cấp nguồn router, kiểm tra đèn, nối máy tính LAN hoặc Wi-Fi theo SSID/mật khẩu trên nhãn.
- Thiết lập: mở `tplinkwifi.net` hoặc `192.168.0.1`, tạo mật khẩu quản trị, chạy Quick Setup. Cấu hình thủ công tại Internet/`Advanced > Network > Internet`; guide §4.3 yêu cầu chọn kiểu kết nối và thông số ISP cung cấp. PPPoE, Dynamic/Static IP, PPTP/L2TP hoặc Bridge chỉ chọn theo xác nhận ISP, không tự điền dữ liệu.
- Wi-Fi: wizard cho đặt Wi-Fi và `SAVE`; Wi-Fi thủ công ở `Wireless Settings`, §7.1. Kiểm tra kết nối bằng `Advanced > System > Diagnostics`, chọn Ping/Traceroute, nhập host, `START`. Nếu lỗi, FAQ nêu kiểm tra kết nối vật lý, kiểu Internet theo ISP, WAN IP, khởi động modem/router; MAC Clone chỉ khi ISP ràng buộc MAC.
- Không có DSL modem tích hợp hay APN SIM trong hướng dẫn này. Tài liệu không xác nhận được revision/vùng của thiết bị cụ thể.

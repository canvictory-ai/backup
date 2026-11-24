---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C86 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c86/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C86 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c86/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## Tài liệu hãng đã mở, biến thể Archer C86 REV2.0.0 (EU/US)

Nguồn là [User Guide trực tiếp, REV2.0.0](https://static.tp-link.com/upload/manual/2024/202405/20240506/1910013671_Archer%20C86%28EUUS%292.0_UG_V1.pdf). Đã đọc chương 2 §2.2 (kết nối phần cứng, khoảng tr. 8-9), chương 4 §4.3 (cấu hình Internet thủ công, khoảng tr. 15 trở đi), chương 7 §7.1 (Wi-Fi, tr. 29 trở đi) và chương 16 §16.9 (Diagnostics, tr. 88). Hướng dẫn chỉ áp dụng cho REV2.0.0 theo bìa; vùng thực tế của thiết bị chưa biết.

- Cắm modem/đường Ethernet vào cổng WAN theo sơ đồ chương 2.2; cấp nguồn, chờ khởi động và kết nối máy cấu hình bằng Ethernet hoặc Wi-Fi.
- WAN: `Internet` hoặc `Advanced > Network > Internet`; guide liệt kê Dynamic IP, Static IP, PPPoE, L2TP/PPTP. Tên tài khoản, mật khẩu, IP tĩnh và thông số phụ phải do ISP cung cấp. Lưu bằng `Save` theo màn hình cấu hình.
- Wi-Fi: `Wireless` hoặc `Advanced > Wireless > Wireless Settings`; đặt SSID/mật khẩu rồi `Save` (§7.1).
- Kiểm tra/chẩn đoán bằng `Advanced > System > Diagnostics`, Ping/Traceroute (§16.9). Chưa ghi nhận kết quả kết nối thực tế.

**Mức xác minh:** đã đọc một guide revision cụ thể, nhưng chưa xác minh máy thực tế hoặc toàn bộ các nhánh lỗi. Cần Hardware Version và vùng trên tem để chọn đúng biến thể; không suy rộng REV2.0.0 sang bản khác.

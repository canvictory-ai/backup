---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer C2300 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-c2300/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer C2300 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-c2300/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc, phạm vi kết quả (24/11/2026)

Đã đọc guide hãng cho hai biến thể riêng: [Archer C2300/A2300 US REV1.1.0](https://static.tp-link.com/1910012198_Archer%20C2300%28US%29_V1_UG.pdf) và [Archer C2300/A2300 EU/US REV1.0.0](https://static.tp-link.com/1910012068_Archer%20C2300%28EU%29%28US%29_V1_User%20Guide.pdf). Không gộp nội dung hai guide để suy ra revision nào của máy. Với US REV1.1.0, ch. 2 §2.2 (tr. 7-9) xác nhận cổng Internet nhận Ethernet từ modem hoặc tường, khởi động modem rồi router, đèn xác nhận, kết nối client LAN/Wi-Fi; ch. 4 §§4.1-4.2 (tr. 13-15) Quick Setup tại `http://tplinkwifi.net` hoặc thủ công `Basic > Internet`, Dynamic IP/Static IP/PPPoE/L2TP/PPTP theo ISP, Save, kiểm tra Network Map; ch. 6 Wireless Settings; phần diagnostics/FAQ trong quản trị.

Model router Ethernet, không DSL/SIM/APN. WAN/PPPoE/IP/VLAN/bridge phải theo thông tin ISP. Guide US/EU không chứng minh tương thích với đơn vị bán tại VN; nhãn Hardware Version và vùng chưa biết.

**Còn thiếu:** xác nhận nhãn/vùng, đối chiếu guide tương ứng, đọc sâu menu Wi-Fi/save và mục kiểm tra/FAQ của đúng biến thể trước khi áp dụng. Chưa thao tác thiết bị hay thử credentials. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

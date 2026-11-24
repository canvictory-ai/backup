---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer A64 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-a64/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer A64 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-a64/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc, phạm vi kết quả (24/11/2026)

[User Guide Archer C64/Archer A64 EU REV1.0.0](https://static.tp-link.com/upload/manual/2023/202303/20230301/1910012999_Archer%20C64%28EU%29_UG.pdf) ghi rõ cả hai model ở bìa. Mục lục: Chapter 2 §2.2 đấu nối (tr. 8); Chapter 4 wizard/WAN (tr. 14-16); Chapter 11 §11.6 Wireless Settings (tr. 55-56); Chapter 12 §12.7 connectivity test (tr. 68); FAQ (tr. 74). Chapter 4 chỉ rõ `http://tplinkwifi.net` > `Internet`, chọn loại WAN theo ISP; Wi-Fi nằm tại `Wireless` hoặc `Advanced > Wireless > Wireless Settings`, thay SSID/password rồi `SAVE`; Diagnostics tại `Advanced > System > Diagnostics`.

Guide là EU REV1.0.0; chưa xác nhận nhãn/vùng của máy. WAN là Ethernet; không có DSL/SIM/APN. PPPoE, IP tĩnh, VLAN/bridge và thông tin đăng nhập phải được ISP xác nhận. Không suy rộng sang vùng/revision khác.

**Còn thiếu:** đối chiếu Hardware Version và vùng thực tế; đọc chi tiết sơ đồ dây và FAQ để hoàn tất hướng xử lý lỗi. Không thao tác thiết bị hoặc thử credentials. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

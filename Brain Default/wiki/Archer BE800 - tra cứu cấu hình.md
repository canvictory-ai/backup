---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer BE800 - tra cứu cấu hình

**Loại thiết bị:** Router Wi-Fi Ethernet. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-be800/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer BE800 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-be800/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở: REV1.0.0

[User Guide Archer BE800 REV1.0.0](https://static.tp-link.com/upload/manual/2023/202305/20230512/1910013397_Archer%20BE800_UG_REV1.0.0.pdf). Đã đọc §2.2 tr. 8-9: nối mạng qua cổng 10Gbps Combo bằng Ethernet hoặc fiber; chọn/thay WAN port qua app hoặc giao diện; cấp nguồn, chờ màn hình LED hoàn tất, nối máy LAN/Wi-Fi. Quick Setup §4.1 tr. 14; WAN thủ công §4.3 tr. 15-18. Wi-Fi §7.1 tr. 32-34 tại `Wireless` hoặc `Advanced > Wireless > Wireless Settings`; tên mạng/mật khẩu, `SAVE`, Smart Connect; 6 GHz được cấu hình riêng. Trang trạng thái kết nối cần tham khảo Network Map; không có kiểm tra thực tế.

**Mức xác minh:** chỉ REV1.0.0; chưa biết revision/vùng của thiết bị. Cổng WAN khả dụng và kiểu WAN phải khớp sơ đồ máy và thông tin ISP; guide không cấp giá trị PPPoE/VLAN cho thuê bao.

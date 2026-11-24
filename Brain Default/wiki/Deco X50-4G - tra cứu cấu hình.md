---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Deco X50-4G - tra cứu cấu hình

**Loại thiết bị:** Router SIM 4G/5G dạng mesh. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/deco-x50-4g/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Deco X50-4G - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/deco-x50-4g/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Guide đã đọc theo từng phiên bản (24/11/2026)

### Hardware Version 2.0, guide EU, REV1.0.0, Deco app 3.1

[User Guide PDF](https://static.tp-link.com/upload/manual/2023/202301/20230120/1910013291_Deco%20X50-4G%28EU%292.0_UG_V1_Deco%203.1app.pdf) - trang 2-3 xác nhận model/revision guide, Nano SIM, 3 Ethernet ports, hai cổng anten ngoài; guide cảnh báo khả năng có thể khác theo vùng/ISP. Trang 4-7: trong Deco app chọn model > `Use as a 3G/4G Router` > lắp Nano SIM > bật nguồn và đợi LED xung xanh > xác nhận/chỉnh thông tin SIM theo ISP > tạo Wi-Fi name/password; trang 8 báo hoàn tất. Guide nói lắp đủ hai anten ngoài để LTE hoạt động đúng.

Trang 12-15 Troubleshooting: nếu không có mobile Internet, kiểm tra SIM LTE/NR lắp đúng, chế độ 3G/4G, vùng phủ và gói cước với ISP; kiểm tra giới hạn dữ liệu tại `More > Data Settings`, Mobile Data tại `More > Internet`; nếu roaming thì xác nhận với ISP và kiểm tra `Advanced > Internet` > Data Roaming. Nếu IP Internet bằng 0.0.0.0, liên hệ ISP xác nhận SIM/mạng, PIN tại `More > Advanced > PIN Management > PIN Code`, hoặc tạo profile tại `More > Advanced > Internet > Mobile ISP`. LED xanh liền báo đã hoàn tất và kết nối 4G/WAN (tr. 3). Guide không gọi tên trường APN; cấu hình profile cần thông số ISP.

### Hardware Version 1.x, guide EU REV1.0.0

[User Guide PDF](https://static.tp-link.com/upload/manual/2022/202208/20220809/1910013218_Deco%20X50-4G%28EU%29_UG_V1.pdf) xác nhận REV1.0.0; mục lục xác định setup SIM tr. 4-8, Wi-Fi router mode tr. 8-12, Data Settings tr. 25, Wi-Fi Settings tr. 31, Internet Settings tr. 36, PIN Management tr. 39, Troubleshooting tr. 53. Đã đọc mở đầu/appearance (tr. 2-3), thấy Nano SIM, cổng Ethernet WAN/LAN linh hoạt, cần lắp hai anten ngoài. Công cụ đọc tài liệu hết thời gian chờ khi trích nội dung sâu; chưa ghi thao tác menu của V1. Không mượn thao tác V2 cho V1.

**Mức xác minh:** đã đọc các thao tác V2 EU hardware 2.0 như nêu; chưa xác minh máy thực tế vì chưa có nhãn hardware version/vùng. V1 có nguồn trực tiếp và định vị được mục/trang nhưng các bước chi tiết chưa đọc xong. Hai guide không thay thế lẫn nhau. Với cả hai bản, APN/PIN/roaming/gói dữ liệu cần ISP xác nhận; không thử PIN hay thông tin truy cập, không thay đổi thiết bị. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

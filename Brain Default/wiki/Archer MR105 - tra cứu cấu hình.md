---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer MR105 - tra cứu cấu hình

**Loại thiết bị:** Router SIM 4G. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-mr105/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer MR105 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-mr105/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## User Guide đã mở trực tiếp: TL-MR105 EU REV1.0.0

**Mức xác minh:** đã mở User Guide chính hãng TL-MR105 EU REV1.0.0 và đọc hướng dẫn kết nối SIM, mục lục WAN/SIM, Wi-Fi và kiểm tra. Tên guide là TL-MR105, chưa xác nhận thiết bị người dùng đúng vùng/revision này.

- [User Guide PDF trực tiếp](https://static.tp-link.com/upload/manual/2023/202307/20230724/1910013413_TL-MR105%28EU%29_UG_REV1.0.0.pdf): §2.2 tr. 7-8, §3 đăng nhập tr. 10-11, ch. 4 §4.1-4.3 tr. 13-15, §11.5 Wi-Fi tr. 53-58, FAQ tr. 75+.
- SIM/khởi động: cắm Nano SIM, cấp nguồn, chờ đèn Internet sáng; nối máy tính qua LAN hoặc SSID/mật khẩu trên nhãn. Đèn Internet tắt: tham khảo FAQ > Q4 và xác nhận dịch vụ với ISP.
- Thiết lập: chạy Quick Setup §4.1. Nếu cần profile thủ công, dùng §4.2; APN, PIN và xác thực cần xác nhận từ nhà mạng. §4.3 kiểm tra kết nối Internet. PPPoE/VLAN không được suy ra từ SIM; chế độ Wireless Router Mode §4.4 là riêng cho kết nối WAN Ethernet.
- Wi-Fi: mục Wireless Settings §11.5 và Basic Wireless Settings §11.5.1; đặt SSID/mật khẩu theo giao diện, lưu thay đổi. Tài liệu cũng ghi nếu kết nối vẫn lỗi thì xem FAQ và kiểm tra SIM/ISP. Chưa trích đủ từng bước các câu hỏi FAQ cụ thể.
- Guide EU REV1.0.0 không chứng minh tương thích với model/revision hoặc khu vực khác; cần đối chiếu Hardware Version trên tem.

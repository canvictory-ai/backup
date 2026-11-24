---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer MR600 - tra cứu cấu hình

**Loại thiết bị:** Router SIM 4G. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-mr600/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer MR600 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-mr600/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.


## User Guide đã mở trực tiếp: Archer MR600 V4, REV1.1.1

**Mức xác minh:** đã mở guide tiếng Pháp chính hãng, ghi model MR600 V4 và REV1.1.1. Có thể dùng làm bằng chứng cho chính biến thể tài liệu này, không khẳng định tương thích với vùng hoặc Hardware Version khác; trang hỗ trợ và nhãn máy chưa được đối chiếu.

- [User Guide PDF trực tiếp](https://static.tp-link.com/2020/202006/20200605/04062020_Guide_d%27installation_ArcherMR600_v4_FR.pdf): §2.3 kết nối router tr. 11; §3 đăng nhập tr. 14; ch. 4 Quick Setup §4.1 tr. 17, profile §4.2 tr. 17-18, kiểm tra Internet §4.4 tr. 21. Bìa ghi Rev1.1.1.
- Sơ đồ SIM: lắp SIM theo chiều/kích thước trong hình §2.3, lắp anten LTE và đặt router theo hướng dẫn; dùng đúng SIM kích thước tương thích, không ép SIM/adapter. Cần đọc hình trên PDF để biết chiều khay chính xác trước khi thao tác.
- Thiết lập lần đầu: kết nối thiết bị qua Wi-Fi/Ethernet, mở `http://tplinkmodem.net`, tạo mật khẩu quản trị theo §3; Quick Setup nằm ở §4.1. Tạo/chọn profile kết nối ở §4.2; tên APN, xác thực và PIN cần lấy từ nhà mạng, không tự đoán.
- Kiểm tra: §4.4 hướng dẫn kiểm tra kết nối Internet; nếu profile không kết nối, đối chiếu APN/loại xác thực/PIN với nhà mạng. Chưa trích được thao tác Wi-Fi, nút lưu cụ thể và đường menu troubleshooting từ phần thân vì truy vấn sâu PDF timeout.
- Còn thiếu đọc sâu trang SIM và mục profile/test; chưa đưa ra tên tùy chọn APN hay đường menu Wi-Fi không được xác nhận. Guide tiếng Pháp và khu vực áp dụng chưa xác nhận cho máy tại Việt Nam.

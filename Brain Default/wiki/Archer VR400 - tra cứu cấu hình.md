---
type: wiki
status: draft
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer VR400 - tra cứu cấu hình

**Loại thiết bị:** Modem-router DSL. **Mức xác minh: chưa xác minh theo revision.** Chưa có bằng chứng đủ điều kiện trong trang này để hướng dẫn thao tác cụ thể: chưa đối chiếu User Guide/Quick Installation Guide chính hãng cho đúng khu vực và Hardware Version của model. Không coi quy trình chung hoặc trang Download là bằng chứng cho menu hay thao tác của thiết bị này.

## Phạm vi đã xác nhận

- Trang hỗ trợ TP-Link Việt Nam theo model: https://www.tp-link.com/vn/support/download/archer-vr400/. Đây chỉ là đầu mối để chọn Hardware Version và tìm tài liệu; không chứng minh các bước cài đặt bên dưới.
- Chưa xác nhận revision áp dụng, khu vực/revision của tài liệu, sơ đồ cổng thực tế, tên menu, lựa chọn WAN/DSL/APN, cách lưu, kiểm tra kết nối hay xử lý lỗi cho model này.

## Cần tài liệu để hoàn tất

Mở hướng dẫn User Guide hoặc Quick Installation Guide trực tiếp từ trang hỗ trợ sau khi chọn đúng Hardware Version trên nhãn thiết bị. Ghi URL PDF/guide sâu, tên mục hoặc số trang cho từng nội dung: cắm WAN/DSL hoặc lắp SIM; thiết lập lần đầu; đường dẫn menu; kiểu WAN/DSL/APN; Wi-Fi; lưu; xác nhận Internet; chẩn đoán và bước kế tiếp khi lỗi. Không suy rộng từ model khác hoặc revision khác.

## Điều kiện nhà mạng

PPPoE, VLAN ID, bridge, thông số đường DSL, APN và thông tin đăng nhập là dữ liệu cần ISP xác nhận cho thuê bao/địa bàn cụ thể. Trang này không cung cấp giá trị để nhập và không xác nhận khả năng tương thích nhà mạng. Chưa thao tác trên thiết bị thực tế hay thử thông tin đăng nhập.

**Nguồn hãng:** [Trang hỗ trợ Archer VR400 - TP-Link Việt Nam](https://www.tp-link.com/vn/support/download/archer-vr400/), truy cập 24/11/2026. Cần chọn revision trên nhãn rồi mở tài liệu hướng dẫn; trang hỗ trợ không thay thế tài liệu hướng dẫn.

## Đọc User Guide theo từng Hardware Version (24/11/2026)

### Archer VR400 EU V1, REV1.0.0

[User Guide PDF](https://static.tp-link.com/res/down/doc/Archer_VR400%28EU%29_V1_UG.pdf). Đã tải và đọc nội dung PDF. Chương 2 §§2.1-2.2 (tr. 7-8): dây điện thoại từ phone jack qua splitter vào DSL; bỏ splitter nếu không dùng điện thoại; cấp nguồn, đợi DSL ổn định khoảng 1-2 phút, rồi nối máy tính LAN hoặc Wi-Fi theo nhãn. Chương 4 §4.1 (tr. 12): vào `http://tplinkmodem.net`, chọn Region/Time Zone rồi Quick Setup. §4.2 (tr. 12): `Basic > Internet`, chọn ISP hoặc Other, chỉ nhập thông tin ISP cấp, Save. §4.3 (tr. 13): `Advanced > System Tools > Diagnostics`, Start để test. Chương 14 §14.3.1 (tr. 80-81): Wi-Fi cơ bản tại `Basic > Wireless`; lưu SSID/password rồi kết nối lại. Appendix T4 (tr. 108-109): kiểm tra cáp/nguồn, đăng nhập trang quản trị, nhờ ISP xác nhận VPI/VCI, Connection Type và credentials; chạy lại wizard hoặc hỗ trợ hãng nếu chưa hết lỗi.

### Archer VR400 EU V2, REV2.0.0

[User Guide PDF](https://static.tp-link.com/1910012199_Archer%20VR400%28EU%29_V2_UG.pdf). Đã tải và đọc nội dung PDF riêng, không kế thừa bước từ V1. Chương 2 §2.2 (tr. 7-8): phone jack/splitter -> DSL, cấp nguồn, đợi DSL LED ổn định, kết nối client LAN/Wi-Fi. Chương 4 §4.1 (tr. 12): `http://tplinkmodem.net` > Quick Setup. §4.2 (tr. 12): `Basic > Internet`, chọn ISP hoặc Other, thông tin tương ứng do ISP cấp; Save. §4.3 (tr. 13): `Advanced > System Tools > Diagnostics` > Start. Chương 14 §14.3.1 (tr. 80-81): Wi-Fi tại `Basic > Wireless`, chỉnh SSID/mật khẩu, lưu. Appendix T4 (tr. 108-109): kiểm tra cáp điện thoại/Ethernet/nguồn; đối chiếu VPI/VCI, Connection Type và account với ISP; chạy lại Quick Setup hoặc liên hệ hỗ trợ nếu còn lỗi.

**Mức xác minh:** thao tác đã đọc riêng cho guide EU V1 và EU V2, nhưng chưa xác minh máy thực tế vì không có Hardware Version/vùng trên nhãn; hai quy trình vẫn được phân riêng. DSL modulation, VPI/VCI, VLAN, PPPoE credentials, bridge/IPTV do ISP xác nhận. Chưa thao tác thiết bị hoặc thử thông tin đăng nhập. [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]

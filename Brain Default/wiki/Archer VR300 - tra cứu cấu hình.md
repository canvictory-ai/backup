---
type: wiki
status: active
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer VR300 - tra cứu cấu hình

**Phân loại:** Modem-router DSL (đường điện thoại đồng, không phải ONT quang). Đây là mục tra cứu theo model, không phải xác nhận model bán chạy. Trang hãng có thể có nhiều Hardware Version, region và firmware; đọc nhãn mặt đáy và chọn đúng khu vực tại trang hỗ trợ trước khi áp dụng. Nguồn hiện diện/model và giới hạn tài liệu: Model được TP-Link nêu trong FAQ cấu hình DSL: https://www.tp-link.com/vn/support/faq/3839/ . Hãng phân biệt DSL modem-router mode với wireless-router mode và yêu cầu xác nhận VLAN, DSL type, PPPoE với ISP. Phạm vi phần cứng/firmware phải đối chiếu nhãn tại trang hỗ trợ tải xuống; không suy thông số nhà mạng. Nguồn: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]].

## Kết nối và cấu hình

1. DSL: ổ cắm đường dây điện thoại → cổng DSL; máy tính → LAN. Nếu Internet vào bằng Ethernet từ modem/ONT khác thì dùng chế độ Wireless Router/EWAN thay vì DSL.
2. Mở `tplinkmodem.net` (hoặc IP theo nhãn/hướng dẫn), tạo mật khẩu quản trị mới. Chờ đèn DSL ổn định.
3. Trong Quick Setup, chọn ISP/kiểu đường truyền đúng hợp đồng. PPPoE dùng tên đăng nhập/mật khẩu do ISP cấp; Dynamic IP chỉ khi ISP yêu cầu. VLAN ID, encapsulation/DSL type và bridge chỉ nhập theo thông số đúng ISP/model.
4. Đặt SSID và mật khẩu Wi-Fi bảo mật, lưu; kiểm tra đèn Internet và truy cập website.
5. Mất DSL sync: kiểm tra dây/ổ cắm và báo ISP; DSL sáng nhưng Internet lỗi: rà PPPoE/VLAN với ISP. Nếu dùng sau ONT, chọn chế độ router Ethernet, tránh cấu hình DSL WAN.

**Thông tin nhà mạng:** Không có thông số riêng của VNPT/Viettel/FPT trong tài liệu model đã dẫn. Tên đăng nhập PPPoE, APN, VLAN, bridge, cấu hình quang/PON hoặc quyền quản trị do ISP quản lý phải xin đúng nhà mạng. Không lưu mật khẩu thật ở trang này và không cấu hình trên thiết bị đang sử dụng.

**Nguồn hãng và ngày truy cập:** [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]], truy cập 24/11/2026. Tài liệu liên quan cần chọn theo đúng Hardware Version/firmware và vùng; các bước giao diện có thể khác.

---
type: wiki
status: active
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Archer AX6000 - tra cứu cấu hình

**Phân loại:** Router Wi-Fi Ethernet (không phải modem/ONT quang). Đây là mục tra cứu theo model, không phải xác nhận model bán chạy. Trang hãng có thể có nhiều Hardware Version, region và firmware; đọc nhãn mặt đáy và chọn đúng khu vực tại trang hỗ trợ trước khi áp dụng. Nguồn hiện diện/model và giới hạn tài liệu: Model thuộc danh mục router Wi-Fi TP-Link; tên model được liệt kê ở trang tải xuống hãng. Xác minh khu vực, đúng tên đầy đủ và Hardware Version tại trang hỗ trợ trước khi theo giao diện: https://www.tp-link.com/vn/support/download/ . Hướng dẫn WAN/Wi-Fi chung và giới hạn ISP: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]].

## Kết nối và cấu hình

1. Sơ đồ: modem/ONT của ISP (LAN) → cổng WAN router; máy tính/điện thoại → LAN hoặc Wi-Fi.
2. Kết nối LAN/Wi-Fi mặc định theo nhãn thiết bị; mở `tplinkwifi.net` hoặc địa chỉ LAN in trên nhãn, tạo/nhập mật khẩu quản trị riêng. Không dùng mật khẩu mặc định làm mật khẩu thật.
3. Internet > WAN: sau modem/router đang cấp mạng chọn Dynamic IP; nếu nối thẳng và ISP cấp PPPoE, nhập thông tin do ISP cung cấp. Không tự bật VLAN hoặc bridge.
4. Wireless: đặt SSID, WPA2-AES/WPA3 nếu firmware hỗ trợ, mật khẩu Wi-Fi mạnh; lưu lại. Kiểm tra trạng thái Internet và mở website.
5. Nếu lỗi: kiểm tra cáp từ modem vào WAN, khởi động lại modem rồi router, kiểm tra WAN IP và loại WAN với ISP; quên Wi-Fi thì kết nối dây để sửa. Nếu không vào trang quản trị, kiểm tra gateway của máy và đúng địa chỉ theo nhãn/hướng dẫn.

**Thông tin nhà mạng:** Không có thông số riêng của VNPT/Viettel/FPT trong tài liệu model đã dẫn. Tên đăng nhập PPPoE, APN, VLAN, bridge, cấu hình quang/PON hoặc quyền quản trị do ISP quản lý phải xin đúng nhà mạng. Không lưu mật khẩu thật ở trang này và không cấu hình trên thiết bị đang sử dụng.

**Nguồn hãng và ngày truy cập:** [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]], truy cập 24/11/2026. Tài liệu liên quan cần chọn theo đúng Hardware Version/firmware và vùng; các bước giao diện có thể khác.

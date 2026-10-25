---
type: wiki
status: active
tags: [wiki, mạng, xử-lý-sự-cố]
created: 2026-10-22
updated: 2026-10-22
source: "[[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]"
aliases: [Lỗi mạng, Mất mạng, Không vào được mạng, Sự cố Wi-Fi]
---

# Lỗi cơ bản hệ thống mạng

Trang này phân loại sự cố mạng phổ biến theo tài liệu Microsoft và Cisco. Cùng một triệu chứng như “không vào được Internet” có thể do thiết bị đầu cuối, Wi-Fi, LAN, DHCP/IP, gateway, DNS, firewall/VPN hoặc nhà cung cấp; phạm vi ảnh hưởng giúp khoanh vùng nhưng chưa đủ để kết luận. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Mất liên kết vật lý hoặc Wi-Fi

- **Không có link Ethernet / biểu tượng mạng báo mất kết nối:** có thể thuộc dây, cổng switch, NIC hoặc cấu hình liên kết vật lý. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]
- **Không kết nối hoặc xác thực Wi-Fi được:** phạm vi có thể là sóng/điểm truy cập, thông tin xác thực, chính sách bảo mật hoặc driver/adapter. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]
- **Đã kết nối Wi-Fi nhưng không truy cập tài nguyên:** liên quan có thể nằm ở TCP/IP, DHCP, DNS, proxy, firewall hoặc gateway. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Lỗi cấp phát hoặc cấu hình IP

Địa chỉ IP/subnet/gateway không hợp lệ, DHCP không cấp địa chỉ, địa chỉ IP trùng hoặc route sai có thể khiến một thiết bị hoặc một phân đoạn mạng mất liên lạc. Microsoft và Cisco xem cấu hình IP/DHCP là nhóm nguyên nhân cần phân biệt với DNS. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Lỗi DNS

Nếu truy cập theo địa chỉ IP được nhưng theo tên miền/tên máy thất bại, lỗi có thể nằm ở phân giải DNS, cấu hình DNS client/server hoặc đường truy cập tới DNS. DNS lỗi có thể làm dịch vụ nội bộ và kết nối Internet có vẻ “mất” dù liên kết IP còn hoạt động. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Chậm, trễ, rớt gói hoặc mất kết nối chập chờn

Nhóm khả năng gồm nghẽn băng thông, mất gói, nhiễu Wi-Fi, roaming, thiết bị trung gian, firewall/VPN, tải server hoặc sự cố upstream/ISP. Nếu nhiều thiết bị cùng bị, nguyên nhân mạng chung hoặc dịch vụ upstream đáng được xem xét; nếu chỉ một thiết bị bị, phạm vi có thể ở thiết bị/adapter/cấu hình riêng. Đây là quy tắc khoanh vùng, không phải kết luận chắc chắn. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Giới hạn

Đổi cấu hình DHCP, DNS, gateway, VLAN, firewall hoặc VPN có thể ảnh hưởng các thiết bị khác trong mạng doanh nghiệp; trang này chỉ phân loại lỗi, không chứa lệnh thay đổi cấu hình. Cần sơ đồ mạng, thiết bị liên quan và phạm vi người dùng bị ảnh hưởng để chẩn đoán cụ thể. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

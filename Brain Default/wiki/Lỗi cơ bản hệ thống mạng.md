---
type: wiki
status: active
tags: [wiki, mạng, xử-lý-sự-cố]
created: 2026-10-22
updated: 2026-11-26
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

## Thứ tự kiểm tra khi hỗ trợ từ xa

1. Hỏi một hay nhiều thiết bị bị lỗi, đang dùng Wi-Fi hay dây, và mất Internet hay chỉ mất một dịch vụ. Thử thiết bị thứ hai trên cùng mạng để thu hẹp phạm vi. [[Microsoft và TP-Link - Kiểm tra Wi-Fi và PoE]]
2. Kiểm tra nguồn, đèn link, dây và cổng. Với camera PoE, đối chiếu chuẩn camera và switch, công suất tối đa mỗi cổng và tổng công suất switch. Khi camera đã có nguồn, kiểm tra đường mạng rồi mới kiểm tra đầu ghi hoặc ứng dụng. [[Microsoft và TP-Link - Kiểm tra Wi-Fi và PoE]]
3. Trên Windows, dùng `ipconfig` để xem IP và default gateway. IP tự gán 169.254.x.x là dấu hiệu cần kiểm tra kết nối và DHCP. Thử ping gateway để kiểm tra đường đến router, rồi thử phân giải tên với `nslookup` nếu truy cập theo IP vẫn được. Một lần ping thất bại chưa đủ kết luận vì thiết bị có thể chặn ICMP. [[Microsoft và TP-Link - Kiểm tra Wi-Fi và PoE]]
4. Với máy in mạng, đọc IP trên màn hình hoặc trang cấu hình rồi so với IP cổng in. Nếu máy in truy cập được trong LAN mà chỉ một máy tính không in được, kiểm tra hàng đợi, cổng in và driver trên máy đó trước khi đổi cấu hình router. Đây là cách áp dụng nguyên tắc khoanh vùng theo từng thiết bị. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

## Giới hạn

Đổi cấu hình DHCP, DNS, gateway, VLAN, firewall hoặc VPN có thể ảnh hưởng các thiết bị khác trong mạng doanh nghiệp; trang này chỉ phân loại lỗi, không chứa lệnh thay đổi cấu hình. Cần sơ đồ mạng, thiết bị liên quan và phạm vi người dùng bị ảnh hưởng để chẩn đoán cụ thể. [[Tài liệu hãng về lỗi cơ bản hệ thống mạng]]

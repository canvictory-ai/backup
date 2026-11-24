---
type: wiki
status: active
tags: [wiki, camera, camera-ip, xử-lý-sự-cố]
created: 2026-10-22
updated: 2026-11-24
source: "[[Tài liệu hãng về lỗi cơ bản camera IP]], [[Nguồn hãng - khắc phục sự cố camera IP và analog]]"
aliases: [Lỗi camera IP, Camera offline, Camera không lên hình, Lỗi camera giám sát]
---

# Lỗi cơ bản camera IP và hệ thống giám sát

Trang này tổng hợp nhóm lỗi thường gặp ở camera IP/CCTV và hệ thống VMS theo tài liệu Axis; các nguyên nhân thay đổi theo camera, switch/PoE, đầu ghi, ứng dụng xem và cấu hình. [[Tài liệu hãng về lỗi cơ bản camera IP]]

## Camera offline hoặc hệ thống không liên lạc được

Thường khoanh vùng kết nối vật lý/mạng, cấp nguồn, địa chỉ/cấu hình mạng, xác thực hoặc đường liên lạc giữa camera, đầu ghi/server và máy xem. Thông báo “No contact” hay “Can't contact camera” nghĩa là hệ thống không truy cập được thiết bị, chưa tự xác nhận camera đã hỏng. [[Tài liệu hãng về lỗi cơ bản camera IP]]

Hỏi một camera hay toàn hệ thống bị offline, kết nối PoE hay adapter, đèn link ở switch/đầu ghi, có thay dây/cấu hình/IP gần đây không. Bước an toàn là kiểm tra đèn nguồn/link và cắm lại đầu nối ngoài; với PoE, xem trạng thái port/switch và thử dây/port đã biết tốt nếu có quyền. Một camera lỗi thì đổi chéo dây/port theo quy trình hệ thống; cả nhóm cùng lỗi thì ưu tiên kiểm tra nguồn switch, uplink và mạng chung. Nếu port PoE báo quá tải, nguồn chập chờn, đầu nối ngoài trời vào nước hoặc phải đo điện/đấu lại thì chuyển kỹ thuật. Mức PoE, sơ đồ chân và công suất cần đối chiếu model camera/switch. [[Nguồn hãng - khắc phục sự cố camera IP và analog]]

## Có thiết bị nhưng không xem được hình trực tiếp

“No video in live view” có thể liên quan camera/luồng video, ứng dụng VMS, tường lửa, khả năng tương thích, giải mã phía máy khách hoặc băng thông. Nếu ghi hình vẫn có nhưng không xem live được, phạm vi lỗi có thể nằm ở luồng xem hoặc ứng dụng chứ không nhất thiết cảm biến ảnh. [[Tài liệu hãng về lỗi cơ bản camera IP]]

Hỏi có xem được giao diện/camera trực tiếp qua thiết bị khác, playback có hình, lỗi xảy ra một hay nhiều kênh và có thay tài khoản/cấu hình không. Nếu camera online và playback có hình, thử một client/trình xem khác được hỗ trợ, kiểm tra quyền truy cập và mạng máy khách; nếu camera không đưa luồng lên đầu ghi, khoanh sang camera/cấu hình luồng/mạng. Không reset camera hoặc đổi IP nếu chưa lưu cấu hình và biết tác động; nếu lỗi theo chính camera qua nhiều port/client thì cần kỹ thuật. [[Nguồn hãng - khắc phục sự cố camera IP và analog]]

## Hình giật, trễ, mất khung hình hoặc chất lượng thấp

Nhóm khả năng gồm nghẽn/băng thông mạng, mất gói, nhiều luồng hoặc client cùng truy cập, tải xử lý camera/server, độ phân giải/tốc độ khung hình và hiệu năng máy xem. Axis lưu ý hiệu năng thực tế phụ thuộc đồng thời thiết bị, mạng, cấu hình hình ảnh, cảnh và client. [[Tài liệu hãng về lỗi cơ bản camera IP]]

## Hình mờ, sai màu, tối hoặc mất nét

Có thể thuộc nhóm lấy nét, điều kiện ánh sáng/cảnh, cài đặt chất lượng hình ảnh hoặc phần cứng quang học/cảm biến; cần đúng model và mẫu hình để phân biệt. Axis tách riêng hướng dẫn chất lượng ảnh và focus khỏi lỗi kết nối mạng. [[Tài liệu hãng về lỗi cơ bản camera IP]]

Hỏi lỗi xuất hiện ban ngày/ban đêm, toàn cảnh hay một vùng, sau vệ sinh/lắp đặt hay thay đổi cài đặt. Quan sát ảnh trực tiếp và lau mặt ngoài ống kính bằng khăn mềm sạch nếu tiếp cận an toàn; kiểm tra vật cản, mạng có mất khung hay không. Ảnh nhòe theo chuyển động/tối có thể liên quan ánh sáng và cài đặt phơi sáng; ảnh sọc/màu sai có thể cần xem nguồn nhiễu hoặc tương thích. Không mở vỏ hoặc chỉnh sâu thông số ban đêm khi chưa ghi nhận cấu hình trước; nước ngưng bên trong, nứt hoặc lỗi ảnh ổn định qua nhiều điều kiện cần kỹ thuật kiểm tra. [[Nguồn hãng - khắc phục sự cố camera IP và analog]]

## Không xem lại hoặc thiếu bản ghi

Có thể thuộc nhóm lưu trữ/recorder, chính sách lịch ghi, luồng camera tới máy chủ, dung lượng hoặc trạng thái dịch vụ VMS. Không xem lại được không đồng nghĩa camera không phát hình trực tiếp. [[Tài liệu hãng về lỗi cơ bản camera IP]]

Hỏi thiếu bản ghi ở một camera hay toàn hệ thống, khoảng thời gian nào, live view hiện tại có hình, trạng thái ổ cứng/SD, lịch ghi và thông báo lỗi của đầu ghi. Bước đầu chỉ xem trạng thái dung lượng/lưu trữ, lịch ghi và playback ở mốc gần nhất; đối chiếu thời gian hệ thống. Không format ổ/SD hoặc khởi tạo lại vì thao tác có thể xóa bản ghi. Nếu ổ có cảnh báo lỗi, không nhận, phát tiếng lạ hoặc đoạn ghi quan trọng đang có nguy cơ mất, dừng thao tác và chuyển kỹ thuật sao lưu/kiểm tra. [[Nguồn hãng - khắc phục sự cố camera IP và analog]]

## Giới hạn

Phân loại trên chủ yếu áp dụng cho camera mạng và VMS. Camera analog, camera hành trình, web camera và hệ thống khác có cấu trúc, mã báo lỗi khác; không áp mã của một hãng sang hãng khác. [[Tài liệu hãng về lỗi cơ bản camera IP]]

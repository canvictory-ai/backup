---
type: wiki
status: active
tags: [wiki, vận-hành, đánh-số, Victory]
created: 2026-11-21
updated: 2026-11-21
source: [[memory/facts/chuan-hoa-lap-ho-so-victory]]
---

# Sổ Theo Dõi Số Văn Bản Victory

Sổ theo dõi số đã phát hành để tra số kế tiếp, tránh trùng. Chỉ ghi nhận khi đã tạo được hồ sơ; không lấy số từ bản nháp chưa phát hành.

| Loại văn bản | Quy tắc | Số gần nhất đã xác minh | Số tiếp theo | Ghi chú |
|---|---|---:|---:|---|
| Báo giá Victory năm 2026 | `VIC-NNN-2026` | 111 | 112 | Đối chiếu tên tệp trong `bao-gia/` ngày 21/11/2026. |
| Phiếu xuất kho Victory năm 2026 | `PXK-VIC-2026-NNN` | 012 | 013 | Đối chiếu hồ sơ trong `bien-ban/` ngày 21/11/2026. |
| Biên bản bàn giao hàng hóa | `DDMMYYYY/BBBGNT/VIC-XXX` | Không có chuỗi tăng liên tục | Theo ngày và mã đối tác | Không thêm số hóa đơn/PO/hậu tố. |
| Hợp đồng mua bán | `DDMMYYYY/HĐKT/VIC-XXX` | Theo từng hồ sơ | Theo quy tắc ngày/mã đối tác | Không tự tạo dãy tăng liên tục. |
| Loại khác chưa có quy tắc | Chưa chốt | `...` | `...` | Không tự đặt quy tắc đánh số. |

Khi lập chứng từ mới, kiểm tra tệp giao dịch gần nhất và cập nhật dòng tương ứng sau khi tạo thành công. Nếu phát hiện khác biệt giữa sổ và hồ sơ thực tế, ưu tiên kiểm kê tệp đã phát hành, sửa sổ và ghi rõ căn cứ kiểm kê. [[Quy Trình Chuẩn Hóa Hồ Sơ Victory]]

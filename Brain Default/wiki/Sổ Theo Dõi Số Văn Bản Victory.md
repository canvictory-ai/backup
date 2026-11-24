---
type: wiki
status: active
tags: [wiki, vận-hành, đánh-số, Victory]
created: 2026-11-21
updated: 2026-11-24
source: [[memory/facts/chuan-hoa-lap-ho-so-victory]]
---

# Sổ Theo Dõi Số Văn Bản Victory

Sổ theo dõi số đã phát hành để tra số kế tiếp, tránh trùng. Chỉ ghi nhận khi đã tạo được hồ sơ; không lấy số từ bản nháp chưa phát hành.

| Loại văn bản | Quy tắc | Số gần nhất đã xác minh | Số tiếp theo | Ghi chú |
|---|---|---:|---:|---|
| Báo giá Victory năm 2026 | `VIC-NNN-2026` | 114 | 115 | Đối chiếu tệp VIC-114-2026 trong `bao-gia/` ngày 23/11/2026. |
| Phiếu xuất kho Victory năm 2026 | `PXK-VIC-2026-NNN` | 012 | 013 | Đối chiếu hồ sơ trong `bien-ban/` ngày 21/11/2026. |
| Biên bản bàn giao hàng hóa | `DDMMYYYY/BBBGNT/VIC-XXX` | `23112026/BBBGNT/VIC-TVM` | Theo ngày và mã đối tác | Đã lập cho Thịnh Vượng Minh Châu ngày 23/11/2026; không thêm số hóa đơn/PO/hậu tố. |
| Hợp đồng mua bán | `HĐKT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `HĐKT/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt đối tác. |
| Hợp đồng nguyên tắc | `HĐNT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `HĐNT/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt đối tác. |
| Phiếu nhập kho | `PNK-VIC-YYYY-NNN` | Chưa phát hành theo quy tắc mới | `PNK-VIC-2026-001` | Dãy riêng theo năm, tăng từ 001. |
| Biên bản đối chiếu công nợ | `BBĐCCN/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `BBĐCCN/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt khách hàng. |
| Giấy đề nghị thanh toán | `DNTT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `DNTT/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt khách hàng. |
| Biên bản làm việc Xuân Thiện | `BBLV/YYYY-NN/VIC-XT` | Chưa phát hành theo quy tắc mới | `BBLV/2026-01/VIC-XT` | Dãy riêng theo năm; mã đối tác cố định `XT`. |

Với hợp đồng mua bán, hợp đồng nguyên tắc, biên bản đối chiếu công nợ, giấy đề nghị thanh toán và biên bản làm việc Xuân Thiện, tăng `NN` lần lượt `01`, `02`, `03`... trong từng năm và từng loại văn bản; sang năm mới, đổi `YYYY` và bắt đầu dãy số của năm đó từ `01`. Với phiếu nhập kho, tăng `NNN` lần lượt `001`, `002`, `003`... theo từng năm. `ABC` là tên viết tắt khách hàng; mã Xuân Thiện dùng `XT`. Các số đã cấp trước khi chốt quy tắc mới giữ nguyên; dãy mới trong năm 2026 bắt đầu từ `01` hoặc `001` theo loại văn bản. [[memory/facts/quy-tac-danh-so-hop-dong-victory]] [[memory/facts/quy-tac-danh-so-chung-tu-victory]]

Khi lập chứng từ mới, kiểm tra tệp giao dịch gần nhất và cập nhật dòng tương ứng sau khi tạo thành công. Nếu phát hiện khác biệt giữa sổ và hồ sơ thực tế, ưu tiên kiểm kê tệp đã phát hành, sửa sổ và ghi rõ căn cứ kiểm kê. [[Quy Trình Chuẩn Hóa Hồ Sơ Victory]]

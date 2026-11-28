---
type: wiki
status: active
tags: [wiki, vận-hành, đánh-số, Victory]
created: 2026-11-21
updated: 2026-11-25
source: [[memory/facts/chuan-hoa-lap-ho-so-victory]]
---

# Sổ Theo Dõi Số Văn Bản Victory

Sổ theo dõi số đã phát hành để tra số kế tiếp, tránh trùng. Chỉ ghi nhận khi đã tạo được hồ sơ; không lấy số từ bản nháp chưa phát hành.

| Loại văn bản | Quy tắc | Số gần nhất đã xác minh | Số tiếp theo | Ghi chú |
|---|---|---:|---:|---|
| Báo giá Victory năm 2026 | `VIC-NNN-2026` | 121 | 122 | Đối chiếu báo giá Đường Mía VIC-121-2026 trong `bao-gia/` ngày 27/11/2026; các số 119–120 là hai báo giá Nam Đông ngày 25/11/2026. |
| Phiếu xuất kho Victory năm 2026 | `PXK-VIC-2026-NNN` | 013 | 014 | Cấp cho Artiverse Knit theo báo giá VIC-117-2026 ngày 24/11/2026. |
| Biên bản bàn giao hàng hóa | `BBBGNT/YYYY-NN/VIC-ABC` | `BBBGNT/2026-05/VIC-AAP` | `BBBGNT/2026-06/VIC-ABC` | Số 05 cho Công ty TNHH Artiverse Apparel, 1 cuộn ruy băng mực Hiti CS200e/220e; thông tin khách hàng theo danh sách, ngày lập để `...`. |
| Hợp đồng mua bán | `HĐKT/YYYY-NN/VIC-ABC` | `HĐKT/2026-01/VIC-ARK` | `HĐKT/2026-02/VIC-ABC` | Cấp cho Công ty TNHH Artiverse Knit theo báo giá VIC-117-2026. |
| Hợp đồng nguyên tắc | `HĐNT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `HĐNT/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt đối tác. |
| Phiếu nhập kho | `PNK-VIC-YYYY-NNN` | Chưa phát hành theo quy tắc mới | `PNK-VIC-2026-001` | Dãy riêng theo năm, tăng từ 001. |
| Biên bản nghiệm thu dịch vụ | `BBNTDV/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `BBNTDV/2026-01/VIC-ABC` | Dãy riêng theo năm và loại; `ABC` là mã đối tác. |
| Biên bản tiếp nhận bảo hành/sửa chữa/đổi trả | `BBTN/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `BBTN/2026-01/VIC-ABC` | Dãy riêng theo năm và loại; `ABC` là mã đối tác. |
| Đơn đặt hàng/xác nhận đơn hàng | `XNDH/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `XNDH/2026-01/VIC-ABC` | Dãy riêng theo năm và loại; `ABC` là mã đối tác. |
| Phiếu xác nhận thanh toán | `XNTT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `XNTT/2026-01/VIC-ABC` | Dãy riêng theo năm và loại; `ABC` là mã đối tác. |
| Biên bản đối chiếu công nợ | `BBĐCCN/YYYY-NN/VIC-ABC` | `BBĐCCN/2026-01/VIC-GEN` | `BBĐCCN/2026-02/VIC-ABC` | Lập theo hóa đơn GTGT 1C26TAA số 00000000 của Genesis Sports Technology; ngày đối chiếu để `...`. |
| Giấy đề nghị thanh toán | `DNTT/YYYY-NN/VIC-ABC` | Chưa phát hành theo quy tắc mới | `DNTT/2026-01/VIC-ABC` | Dãy riêng theo năm; `ABC` là mã viết tắt khách hàng. |
| Biên bản làm việc Xuân Thiện | `BBLV/YYYY-NN/VIC-XT` | Chưa phát hành theo quy tắc mới | `BBLV/2026-01/VIC-XT` | Dãy riêng theo năm; mã đối tác cố định `XT`. |

Với hợp đồng mua bán, hợp đồng nguyên tắc, biên bản bàn giao, biên bản đối chiếu công nợ, giấy đề nghị thanh toán, biên bản làm việc Xuân Thiện, biên bản nghiệm thu dịch vụ, biên bản tiếp nhận bảo hành/sửa chữa/đổi trả, đơn đặt hàng/xác nhận đơn hàng và phiếu xác nhận thanh toán, tăng `NN` lần lượt `01`, `02`, `03`... riêng theo từng năm và từng loại văn bản; sang năm mới bắt đầu từ `01`. Dãy biên bản bàn giao dùng chung giữa các khách hàng, không đặt lại theo ngày hoặc khách hàng. `ABC` là tên viết tắt đối tác; mã Xuân Thiện dùng `XT`. Với phiếu nhập kho, tăng `NNN` lần lượt `001`, `002`, `003`... theo từng năm. Các số đã cấp trước khi chốt quy tắc mới giữ nguyên; dãy mới năm 2026 bắt đầu từ `01` hoặc `001` theo loại văn bản. [[memory/facts/quy-tac-danh-so-hop-dong-victory]] [[memory/facts/quy-tac-danh-so-chung-tu-victory]]

Khi lập chứng từ mới, kiểm tra tệp giao dịch gần nhất và cập nhật dòng tương ứng sau khi tạo thành công. Nếu phát hiện khác biệt giữa sổ và hồ sơ thực tế, ưu tiên kiểm kê tệp đã phát hành, sửa sổ và ghi rõ căn cứ kiểm kê. [[Quy Trình Chuẩn Hóa Hồ Sơ Victory]]

---
type: wiki
status: active
tags: [wiki, vận-hành, hồ-sơ, Victory]
created: 2026-11-21
updated: 2026-11-23
source: [[memory/facts/du-lieu-thieu-dung-dau-cham]]
---

# Quy Trình Chuẩn Hóa Hồ Sơ Victory

Quy trình áp dụng khi lập hợp đồng, báo giá, biên bản và phiếu kho theo mẫu hiện hành đã duyệt. Mỗi loại chứng từ có mẫu mặc định cho tình huống phổ biến; có thể có thêm biến thể theo khách hàng/quy trình. Một bộ hồ sơ cho cùng một việc có thể gồm nhiều loại chứng từ. Ghi rõ phạm vi mẫu trong Wiki; không lấy hồ sơ giao dịch cũ làm mẫu hoặc mang thông tin khách cũ sang. [[Nguyên tắc giữ nguyên mẫu đã duyệt]]

## Tiếp nhận và đối chiếu

- Xác định loại văn bản, khách hàng, mục đích, nguồn dữ liệu và định dạng cần xuất.
- Thu thập ngày/số chứng từ, PO/hóa đơn, danh mục hàng/dịch vụ, model, đơn vị tính, số lượng, đơn giá, thuế, tổng tiền, thông tin giao nhận và điều khoản riêng nếu có.
- Áp dụng [[Ưu Tiên Tên Khách Hàng Và Hàng Hóa Theo Danh Mục]] khi tra tên pháp nhân, hàng hóa và dịch vụ; đối chiếu với chứng từ hiện tại, không tái sử dụng dữ liệu giao dịch cũ.
- Hỏi lại khi dữ liệu thiếu có thể làm thay đổi nghĩa vụ, giá trị hoặc nội dung xác nhận; các trường còn thiếu khác được biểu diễn bằng `...`.

## Quy tắc trường thiếu

Trong mọi giấy tờ phát hành, trường dữ liệu chưa được cung cấp hoặc chưa xác minh ghi `...`. Không để trống trường dữ liệu và không ghi `[CẦN BỔ SUNG]`. Không tự điền dựa trên suy đoán. Khoảng dành cho ký/ghi tay, khung ảnh, ô gộp và khoảng trống cấu trúc theo thiết kế mẫu không phải trường dữ liệu, giữ nguyên như mẫu. Quy tắc này chỉ áp dụng cho bản giấy tờ được tạo; không thay đổi dữ liệu nguồn hoặc cơ sở khách hàng. [[memory/facts/du-lieu-thieu-dung-dau-cham]]

## Số văn bản

Tra số kế tiếp trong [[Sổ Theo Dõi Số Văn Bản Victory]] trước khi lập. Chỉ tăng/cập nhật sổ sau khi tệp đã tạo thành công; nếu không có quy tắc đánh số đã chốt thì không tự tạo quy tắc mới, ghi `...` ở trường số.

## Kiểm tra trước khi gửi

- Đúng khách hàng, pháp nhân, vai trò bên mua/bán, MST, địa chỉ và người đại diện có căn cứ.
- Đúng ngày, số văn bản, PO/hóa đơn và định dạng đầu ra.
- Đối chiếu từng dòng hàng, đơn vị, số lượng, đơn giá, thành tiền, thuế và tổng.
- Tất cả trường dữ liệu thiếu dùng `...`; khoảng ký, ảnh và định dạng cấu trúc vẫn đúng mẫu.
- Mở lại tệp cuối, kiểm tra bố cục trang/bảng và đối chiếu với yêu cầu trước khi gửi.

## Bộ hồ sơ và biến thể

Các mẫu đang lưu là bộ mẫu hiện tại và đủ dùng cho nhu cầu hiện nay. Chưa tạo thêm loại chứng từ mới cho đến khi người dùng yêu cầu hoặc cung cấp mẫu. Khi một khách hàng/quy trình cần nội dung khác, tạo biến thể riêng và ghi rõ phạm vi; không xem khác biệt có chủ đích là trùng lặp. Các chứng từ khác loại có thể cùng nằm trong một bộ hồ sơ phục vụ một việc. [[Nguyên tắc giữ nguyên mẫu đã duyệt]] [[memory/facts/bo-mau-chung-va-mau-dac-thu]]

## Mẫu hiện hành

- [[Mẫu Báo Giá Dùng Chung Victory]]
- [[Mẫu Hợp Đồng Mua Bán Victory Bán Ra]] và [[Mẫu Hợp Đồng Nguyên Tắc Mua Bán Hàng Hóa]]
- [[Mẫu Biên Bản Bàn Giao Nghiệm Thu Hàng Hóa Victory]] và [[Mẫu Biên Bản Làm Việc Công Ty Thể Thao Xuân Thiện]]
- [[Mẫu Phiếu Xuất Kho Kiêm Bàn Giao Hàng Hóa Victory]] và [[Mẫu Phiếu Nhập Kho Kiêm Kiểm Nhận Hàng Hóa Victory]]
- [[Mẫu Biên Bản Đối Chiếu Công Nợ Victory]] và [[Mẫu Giấy Đề Nghị Thanh Toán Victory]]

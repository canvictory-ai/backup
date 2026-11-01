---
type: workflow
name: Tiếp nhận tin Zalo - phân công bot
slug: tiep-nhan-tin-zalo---phan-cong-bot
status: active
group: Chung
description: 'Xử lý tin nhắn Zalo theo vai trò và quy định đã huấn luyện: Luna Vũ
  phụ trách bán hàng, Tư vấn Kỹ thuật phụ trách kỹ thuật.'
steps:
- agent: luna-vu
  task: 'Tin nhắn Zalo đầu vào: {{input}}

    Thực hiện đúng vai trò, tài liệu và quy định đã huấn luyện của bạn. Chỉ xử lý
    phần bán hàng, giá, tồn kho và tiếp nhận/chuyển đơn thuộc nhiệm vụ. Nếu không
    thuộc chuyên môn thì im lặng theo quy định hiện có. Không tự tạo thêm quyền hoặc
    cam kết ngoài nhiệm vụ.'
- agent: tu-van-ky-thuat
  task: 'Tin nhắn Zalo gốc: {{input}}

    Kết quả bước trước: {{prev}}

    Thực hiện đúng vai trò và quy định kỹ thuật đã huấn luyện. Chỉ xử lý phần kỹ thuật
    thuộc nhiệm vụ; nếu không thuộc chuyên môn thì im lặng theo quy định hiện có.
    Không lặp lại nội dung bán hàng của Luna Vũ.'
updated: '2026-10-30'
---

Xử lý tin nhắn Zalo theo vai trò và quy định đã huấn luyện: Luna Vũ phụ trách bán hàng, Tư vấn Kỹ thuật phụ trách kỹ thuật.

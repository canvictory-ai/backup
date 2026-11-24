---
type: wiki
status: active
tags: [wiki, mang]
created: 2026-11-24
updated: 2026-11-24
source: [[Nguồn cấu hình router TP-Link - hướng dẫn chính hãng]]
---
# Nguồn cấu hình router TP-Link - hướng dẫn chính hãng

Ngày truy cập: 24/11/2026. Tài liệu hãng được dùng để xác nhận model/phạm vi, loại thiết bị, quy trình kết nối và phần cấu hình chung; phải đối chiếu đúng khu vực và Hardware Version in trên nhãn trước khi thao tác.

- Danh sách tải xuống TP-Link Việt Nam, mục Router Wi-Fi và 4G LTE: https://www.tp-link.com/vn/support/download/ (danh mục hiện liệt kê router AX/AC/N, dòng Archer MR và NX; mỗi trang yêu cầu chọn phiên bản phần cứng).
- Danh mục sản phẩm router Wi-Fi TP-Link Việt Nam: https://www.tp-link.com/vn/wpa3/product-list/?app=wifi-toolkit (danh sách model; không phải bảng xếp hạng bán chạy).
- TP-Link FAQ 3837, “Should I use Dynamic IP or PPPoE?”, mục loại kết nối: https://www.tp-link.com/vn/support/faq/3837/ . Loại WAN phụ thuộc ISP và sơ đồ; nối sau router chính thường dùng Dynamic IP, nối trực tiếp cần hỏi ISP.
- TP-Link Wi-Fi Router User Guide (For Web), mục Internet/Wireless/Administration: https://www.tp-link.com/vn/document/111858/ . Đăng nhập cục bộ, thiết lập WAN, Wi-Fi, mật khẩu quản trị và chẩn đoán.
- TP-Link FAQ 2845, “Cách thiết lập bộ định tuyến 4G LTE không dây TP-Link trên ứng dụng Tether”, mục model áp dụng và cấu hình: https://www.tp-link.com/vn/support/faq/2845/ . Hãng yêu cầu chọn đúng phiên bản và lưu ý vùng bán khác nhau.
- TP-Link Service Provider FAQ 181, “How to Set Up TP-Link 5G/4G Router on Web Management Page”, mục kết nối SIM/APN: https://service-provider.tp-link.com/faq/181/ . Có danh sách model, gồm các phiên bản MR; APN/đăng nhập SIM phụ thuộc nhà mạng.
- TP-Link FAQ 3839, thiết lập DSL modem router trên giao diện web, mục DSL/Wireless Router mode, PPPoE, VLAN: https://www.tp-link.com/vn/support/faq/3839/ . VLAN ID và tham số DSL phải lấy từ ISP.
- TP-Link FAQ 2607, xử lý không có Internet sau cài đặt DSL: https://www.tp-link.com/vn/support/faq/2607/ .
- TP-Link trang tải riêng Deco X50-4G: https://www.tp-link.com/vn/support/download/deco-x50-4g/ . Ghi rõ V1/V2 và hướng dẫn tương ứng; tính sẵn có tùy vùng.

Không có nguồn ở trên xác nhận thông số VLAN, PPPoE, bridge hoặc ONT cho một nhà mạng Việt Nam cụ thể. Không áp dụng các thông số đó theo suy đoán. TP-Link FAQ nêu model và phiên bản khác nhau; trang này không kết luận độ phổ biến hay doanh số.


## Trang hỗ trợ theo model đã đối chiếu ngày 24/11/2026

TP-Link Việt Nam cảnh báo tính khả dụng model/Hardware Version tùy khu vực. Mỗi URL dưới đây là trang hỗ trợ chính hãng đúng tên model, có bộ chọn Hardware Version và mục tải tài liệu/firmware theo biến thể; chỉ một thiết bị có nhãn cụ thể mới xác định được phiên bản cần áp dụng. Danh mục xác nhận sự hiện diện trong hệ thống hỗ trợ hãng, không phải thống kê doanh số.

- [[Archer AX10 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax10/).
- [[Archer AX12 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax12/).
- [[Archer AX1500 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax1500/).
- [[Archer AX20 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax20/).
- [[Archer AX23 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax23/).
- [[Archer AX53 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax53/).
- [[Archer AX55 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax55/).
- [[Archer AX72 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax72/).
- [[Archer AX73 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax73/).
- [[Archer C6 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c6/).
- [[Archer C64 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c64/).
- [[Archer C80 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c80/).
- [[Archer A8 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-a8/).
- [[Archer A64 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-a64/).
- [[Archer C54 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c54/).
- [[Archer C50 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c50/).
- [[Archer C24 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c24/).
- [[Archer C20 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c20/).
- [[Archer C2300 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c2300/).
- [[Archer A9 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-a9/).
- [[Archer C9 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c9/).
- [[Archer C5 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c5/).
- [[Archer C1200 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c1200/).
- [[Archer AX50 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax50/).
- [[Archer C86 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c86/).
- [[Archer AX56 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax56/).
- [[Archer AX6000 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax6000/).
- [[Archer AX90 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax90/).
- [[Archer AX80 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax80/).
- [[Archer GX90 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-gx90/).
- [[Archer AXE75 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-axe75/).
- [[Archer BE230 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-be230/).
- [[Archer BE550 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-be550/).
- [[Archer BE800 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-be800/).
- [[Archer AX11000 - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-ax11000/).
- [[Archer C58HP - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-c58hp/).
- [[TL-WR846N - tra cứu cấu hình]] - Ethernet Wi-Fi router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/tl-wr846n/).
- [[Archer VR400 - tra cứu cấu hình]] - DSL modem-router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-vr400/).
- [[Archer VR600 - tra cứu cấu hình]] - DSL modem-router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-vr600/).
- [[Archer VR300 - tra cứu cấu hình]] - DSL modem-router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-vr300/).
- [[TD-W9960 - tra cứu cấu hình]] - DSL modem-router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/td-w9960/).
- [[TD-W9970 - tra cứu cấu hình]] - DSL modem-router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/td-w9970/).
- [[Archer MR100 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr100/).
- [[Archer MR105 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr105/).
- [[Archer MR200 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr200/).
- [[Archer MR400 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr400/).
- [[Archer MR600 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr600/).
- [[Archer MR6400 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-mr6400/).
- [[Archer NX200 - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/archer-nx200/).
- [[Deco X50-4G - tra cứu cấu hình]] - SIM 4G/5G router; Hardware Version: chọn theo nhãn thiết bị trên trang hỗ trợ; [trang hỗ trợ TP-Link VN](https://www.tp-link.com/vn/support/download/deco-x50-4g/).


## Phạm vi và phân loại

Danh mục hiện có 50 model: 37 router Wi-Fi Ethernet, 5 modem-router DSL, 7 router SIM 4G và 1 router SIM 5G. Không đưa ONT quang vào danh sách vì đây là thiết bị đầu cuối do nhà mạng cấp/quản lý trong nhiều trường hợp; cần xác minh model và hướng dẫn từ ISP cụ thể trước khi ghi cấu hình quang. Danh mục xác nhận model có trang hỗ trợ hãng tại khu vực TP-Link Việt Nam, không xếp hạng độ phổ biến hay doanh số.


## Kết quả rà soát tài liệu theo model - 24/11/2026

**Kết quả theo tiêu chuẩn yêu cầu: 0/50 model được xác minh đầy đủ.** Các trang model đã được chuyển sang `status: draft` và đánh dấu rõ là chưa xác minh theo revision. Chúng không còn trình bày chỉ dẫn chung như thao tác đã chứng minh. Muốn hoàn tất, cần lấy guide hãng đúng khu vực và revision, rồi ghi link trực tiếp, mục/trang và các nội dung từng model.

### Tài liệu trực tiếp tìm được, nhưng không áp dụng làm xác minh cho thiết bị trong Brain

- Archer AX10 / Archer AX1500, [User Guide chính hãng, trang theo chương](https://www.tp-link.com/us/user-guides/archer-ax10%26ax1500_v1/chapter-2-connect-the-hardware), chương “Connect the Hardware”; [bản PDF](https://static.tp-link.com/upload/manual/2025/202511/20251105/1910012597_Archer%20AX10%28EU%26US%291.0_UG_V1.pdf), REV1.0.0. Kết quả tra cứu ghi tên guide và chương kết nối, nhưng đây là guide US/EU và chưa đối chiếu vùng/revision của máy cụ thể; không dùng làm bằng chứng cấu hình cho trang model.
- Archer VR400, [User Guide V1 PDF](https://static.tp-link.com/res/down/doc/Archer_VR400%28EU%29_V1_UG.pdf), REV1.0.0; [User Guide V2 PDF](https://static.tp-link.com/1910012199_Archer%20VR400%28EU%29_V2_UG.pdf), REV2.0.0. Cả hai là bản EU; chưa biết revision và khu vực thiết bị cần cấu hình.
- Deco X50-4G, [User Guide V1](https://static.tp-link.com/upload/manual/2022/202208/20220809/1910013218_Deco%20X50-4G%28EU%29_UG_V1.pdf), REV1.0.0; [User Guide V2](https://static.tp-link.com/upload/manual/2023/202301/20230120/1910013291_Deco%20X50-4G%28EU%292.0_UG_V1_Deco%203.1app.pdf), REV1.0.0. Đây là tài liệu EU; không thể chọn đúng bản cho một thiết bị chưa biết nhãn/vùng.

Các tài liệu trên là các đầu mối đã mở được, không phải xác minh thao tác trọn vẹn model/revision. Search result hoặc HTTP status không được tính là bằng chứng. Với 10 model chưa có guide User Guide/Quick Installation Guide trực tiếp được mở trong lượt này, chưa thể ghi thao tác theo revision. Vì vậy không ghi giả menu, sơ đồ, lựa chọn WAN/DSL/APN, Wi-Fi, lưu, kiểm tra hoặc chẩn đoán.

### Thiếu để tiếp tục

Cần nhãn model, Hardware Version và vùng mua nếu yêu cầu hướng dẫn gắn với thiết bị thực tế; nếu chỉ lập tài liệu theo từng biến thể, cần tra và mở guide từ trang hãng cho từng model/revision/vùng. Sau đó ghi rõ các mục và trang đã đọc cho cắm dây/SIM, first setup, menu WAN/DSL/APN, Wi-Fi, lưu, kiểm tra và chẩn đoán. PPPoE, VLAN, bridge, thông số DSL và APN phải ghi là cần ISP xác nhận nếu tài liệu hãng không quy định giá trị theo ISP.


### Guides đã mở và đọc nội dung, 24/11/2026

- Archer AX10/AX1500: User Guide REV1.0.0 EU/US, [PDF trực tiếp](https://static.tp-link.com/upload/manual/2025/202511/20251105/1910012597_Archer%20AX10%28EU%26US%291.0_UG_V1.pdf). Đã xác nhận phạm vi chương 2, 3, 4, 6 và phần quản trị; chưa khớp vùng/revision máy cụ thể.
- Archer AX20: [User Guide online Archer AX20 & AX1800 V1, chapter 2](https://www.tp-link.com/us/user-guides/archer-ax20%26ax1800_v1/chapter-2-connect-the-hardware), [chapter 4](https://www.tp-link.com/us/user-guides/archer-ax20%26ax1800_v1/chapter-4-set-up-internet-connection). Đây là tài liệu US V1; không áp dụng cho bản V2 hoặc vùng khác.
- Archer AX23: [User Guide PDF REV1.0.0](https://static.tp-link.com/manual/2021/202107/20210708/1910013052_Archer%20AX23_UG_REV1.0.0.pdf). Đã đọc mục đấu nối, loại WAN, Wi-Fi, Diagnostics; guide chưa xác định vùng triển khai.
- Archer AX53: [User Guide PDF REV1.0.0](https://static.tp-link.com/upload/manual/2025/202508/20250822/1910013106_Archer%20AX53_UG_REV1.0.0.pdf). Đã đọc đấu nối, wizard/WAN, menu Wi-Fi; cần đọc sâu diagnostics và đối chiếu vùng máy.
- Archer AX55: [User Guide PDF REV1.0.0](https://static.tp-link.com/upload/manual/2022/202203/20220321/1910013020_Archer%C2%A0AX55_UG_REV1.0.0.pdf). Đã đối chiếu mục lục; chưa đọc đủ nội dung các thao tác cụ thể.

Tính đến lượt này, đã mở/đọc guide cho 28 model qua các phiên bản được ghi tại từng trang. **0/50** đủ điều kiện xác minh cho thiết bị thực tế vì thiếu Hardware Version/vùng trên nhãn; với một số model còn thiếu đọc sâu FAQ hoặc kiểm tra kết nối. Các guide theo biến thể EU/US không được coi là áp dụng cho vùng khác.


### Guides đọc bổ sung (24/11/2026)

- Archer C64 EU REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2025/202509/20250911/1910012999_Archer%20C64%28EU%29_UG.pdf), đọc đấu nối, WAN, Wi-Fi và diagnostics.
- Archer C64/A64 EU REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2023/202303/20230301/1910012999_Archer%20C64%28EU%29_UG.pdf), guide ghi cả hai model; đọc mục lục và các phần WAN/Wi-Fi/diagnostics.
- Archer C6/A6 REV2.2.1: [User Guide PDF](https://static.tp-link.com/2020/202001/20200109/1910012745_Archer%20A6C6_UG.pdf), đọc đấu nối, WAN và diagnostics. Archer C6/A6 US REV4.0.1 có guide riêng: [PDF](https://static.tp-link.com/upload/manual/2024/202412/20241211/1910013879_Archer%20C6%28US%29_UG_REV4.0.1.pdf); không gộp thao tác giữa hai bản.


### Guides đọc bổ sung (24/11/2026)

- Archer A8 US REV2.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2024/202406/20240611/1910013669_Archer%20A8%28US%292.0_UG_V1.pdf), đọc đấu nối, WAN, Wi-Fi.
- Archer C80: [User Guide PDF](https://static.tp-link.com/2021/202104/20210422/1910012744_Archer%20C80_UG_V4.pdf). Tên tệp có V4 nhưng bìa PDF ghi REV1.0.1; dùng revision bìa, không suy đoán. Đã đọc đấu nối, WAN, Wi-Fi và Diagnostics.


### Deco X50-4G: hai guide EU đã mở

- Hardware Version 2.0, guide REV1.0.0 cho Deco app 3.1: [PDF](https://static.tp-link.com/upload/manual/2023/202301/20230120/1910013291_Deco%20X50-4G%28EU%292.0_UG_V1_Deco%203.1app.pdf). Đọc setup SIM tr. 4-7, setup Wi-Fi router tr. 8-11, troubleshooting tr. 12-15; APN không được gọi tên, profile di động yêu cầu thông tin ISP.
- Hardware Version 1.x, guide REV1.0.0: [PDF](https://static.tp-link.com/upload/manual/2022/202208/20220809/1910013218_Deco%20X50-4G%28EU%29_UG_V1.pdf). Xác nhận bìa và mục lục theo trang, nhưng trích nội dung sâu bị timeout; không coi thao tác là đã đọc/xác minh.


### Archer VR400: đọc sâu cả hai revision EU

- V1 REV1.0.0: [User Guide PDF](https://static.tp-link.com/res/down/doc/Archer_VR400%28EU%29_V1_UG.pdf), đọc đấu DSL tr. 7-8, wizard/WAN tr. 12, diagnostics tr. 13, Wi-Fi tr. 80-81, FAQ T4 tr. 108-109.
- V2 REV2.0.0: [User Guide PDF](https://static.tp-link.com/1910012199_Archer%20VR400%28EU%29_V2_UG.pdf), đọc riêng các phần và trang tương ứng; không gộp thao tác với V1.
- Hai guide đều là EU; nếu PDF hỗ trợ vượt giới hạn đọc web thì tải trực tiếp và trích nội dung PDF cục bộ, không dựa vào mã HTTP.


### Guides đọc bổ sung (24/11/2026)

- Archer C50 V2 REV2.0.0, bản UN: [User Guide PDF](https://static.tp-link.com/Archer_C50%28UN%29_V2_UG_1480381270656s.pdf), đọc kết nối, wizard, WAN, Wi-Fi.
- Archer C20 EU REV6.2.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2026/202604/20260417/1910013835_Archer%20C20%28EU%29_UG_REV%206.2.0.pdf), đọc kết nối, menu Internet/Wi-Fi; còn thiếu đọc sâu loại WAN và FAQ/diagnostics.
- Archer C2300/A2300: [US REV1.1.0 PDF](https://static.tp-link.com/1910012198_Archer%20C2300%28US%29_V1_UG.pdf) và [EU/US REV1.0.0 PDF](https://static.tp-link.com/1910012068_Archer%20C2300%28EU%29%28US%29_V1_User%20Guide.pdf). Phân biệt hai guide, đã đọc đấu nối và Internet setup cho US REV1.1.0; chưa xác minh bản máy cụ thể.


### Archer AX73: hai guide revision đã đọc riêng

- REV1.1.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2022/202202/20220210/1910013032_Archer%20AX73_UG_REV1.1.0.pdf), kết nối tr. 8-9, Internet tr. 14-17, Wi-Fi tr. 27-32, Diagnostics tr. 108.
- REV2.0.1: [User Guide PDF](https://static.tp-link.com/upload/manual/2025/202501/20250109/1910013878_Archer%20AX73_UG_REV2.0.1.pdf), kết nối tr. 8-9, Internet tr. 14-17, Wi-Fi tr. 31-33, Diagnostics tr. 116. Ghi riêng số chương/menu theo revision.


### Guides đọc bổ sung theo model và revision (24/11/2026)

- Archer C86 REV2.0.0 EU/US: [User Guide PDF](https://static.tp-link.com/upload/manual/2024/202405/20240506/1910013671_Archer%20C86%28EUUS%292.0_UG_V1.pdf), ch. 2 §2.2, ch. 4 §4.3, ch. 7 §7.1, ch. 16 §16.9.
- Archer AX80 REV2.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2024/202403/20240325/Archer%20AX80%20User%20Guide_REV2.0.0.pdf), ch. 2 §2.2 tr. 8, ch. 4 §4.3 tr. 15+, ch. 7 §7.1 tr. 32-34, ch. 16 §16.8 tr. 119. EU REV1.0.0 PDF cũng tìm thấy nhưng nội dung không trộn.
- Archer AX6000 US REV1.3.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2023/202311/20231108/1910013553_Archer%20AX6000%28US%29%201.0_UG_REV1.3.0.pdf), ch. 2 tr. 6-8, ch. 4 tr. 12-18, §12.7 tr. 74-76, §13.3 tr. 83.
- Archer C1200 REV2.0.0 EU/US: [User Guide PDF](https://static.tp-link.com/1910012083_Archer%20C1200%28EU%29%26%28US%29_V2_User%20Guide.pdf), ch. 4 §4.1-4.3 tr. 12-18. US V3 companion guide [PDF](https://static.tp-link.com/1910012083_Archer%20C1200%28US%29_V3_User%20Guide.pdf), ch. 2 §2.2 tr. 6.
- Archer C9 US REV4.0.0: [User Guide PDF](https://static.tp-link.com/Archer%20C9%28US%29_V3_User%20Guide.pdf), ch. 2 §2.2 tr. 6-8, ch. 4 §4.2 tr. 14-16. Archer C5 REV2.0.0: [User Guide PDF](https://static.tp-link.com/resources/document/Archer_C5_V2_UG.pdf), Figure 2-1 tr. 6; còn thiếu đọc sâu các chương WAN/Wi-Fi/diagnostics.
- TD-W9960 EU REV1.2.0: [User Guide PDF](https://static.tp-link.com/2020/202003/20200310/1910012507_TD-W9960%28EU%29_UG_REV1.2.0.pdf), mục lục §2.2 tr. 8, §4.1-4.3 tr. 13-14, §13.3 tr. 59; chưa đọc sâu thao tác. TD-W9970 REV4.0.0: [User Guide PDF](https://static.tp-link.com/2020/202001/20200114/1910012731_TD-W9970_UG_REV4.0.0.pdf), mục lục §2.2 tr. 9, §4.1-4.3 tr. 14-15, §13.4 tr. 70+. Riêng [QIG TD-W9970/TD-W9970B V1 REV1.0.2](https://static.tp-link.com/resources/document/TD-W9970_V1_QIG.pdf) đã đọc toàn văn; không áp dụng QIG đó cho REV4.0.0.
- Archer MR200 EU REV2.0.0: [User Guide PDF](https://static.tp-link.com/1910012062_ArcherMR200%28EU%29_V2_UG.pdf), §2.3 tr. 7-9, §4.1-4.3 tr. 13-15, §11.5.1 tr. 49. Archer MR400 EU REV1.0.0: [User Guide PDF](https://static.tp-link.com/1910012128_Archer%20MR400%28EU%29_V1_UG.pdf), §2.3 tr. 7, §4.1-4.3 tr. 13-15, §11.4 tr. 48-50. MR400 EU REV1.2.0 [PDF](https://static.tp-link.com/1910012197_Archer%20MR400%28EU%29_V1_UG.pdf) đã mở riêng, chỉ đọc sâu §4.2.
- Archer NX200 REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2025/202503/20250324/Archer%20NX200_UG_REV1.0.0.pdf), §2.2 tr. 8-9; §4.1/4.3/4.4 tr. 14/16-19; chương 6 Wi-Fi tr. 46-47. Guide nêu MBB/SIM và EWAN; APN/credentials/PIN phải nhà mạng cấp.

Tổng cộng **40/50 model** có ít nhất một guide chính hãng trực tiếp đã mở và nội dung hoặc mục lục được đọc; mức đọc được nêu riêng ở từng trang. **0/50** xác minh áp dụng cho thiết bị thực tế vì không có Hardware Version/vùng của máy. **10 model** chưa mở được guide trực tiếp trong lượt này: Archer AX12, AX56, BE230, AX11000, C58HP, TL-WR846N, MR100, MR105, MR600 và MR6400. C24/AX90/MR100/MR105/MR600/MR6400 chưa có manual trong các kết quả đã mở; các model còn lại cũng chưa có manual được đọc. Các nội dung cụ thể còn thiếu theo model được ghi tại từng trang.


- Archer VR600 EU REV1.1.0: [User Guide PDF](https://static.tp-link.com/res/down/doc/Archer_VR600%28EU%29_V1_UG.pdf), §2.2 tr. 10-11, §4.1-4.4 tr. 15-18, Wi-Fi §12.2.1 tr. 68.
- Archer VR300 EU REV1.0.0: [User Guide PDF](https://static.tp-link.com/1910012157_Archer%20VR300%28EU%29_V1_UG.pdf), §2.2 tr. 7, §4.1-4.3 tr. 12-13. Có guide REV1.2.0 riêng nhưng chưa đọc; không trộn revision.

- Archer AX72 REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2022/202211/20221116/1910013025_Archer%20AX72_UG_REV1.0.0.pdf), §2.2 tr. 8, §4.1-4.3 tr. 14-17, Wi-Fi §6.1 tr. 28-29. REV1.0.1 guide tách riêng, chưa đọc.
- Archer AX50 REV1.0.0: [User Guide PDF](https://static.tp-link.com/2020/202003/20200320/1910012590_Archer%20AX501.0_UG_V1.pdf), §2.2 tr. 8, §4.1/4.3 tr. 14-19, Wi-Fi §12.7 tr. 70-71.

- Archer C24 EU REV2.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2023/202303/20230309/1910013356_Archer%20C24%28EU%29_UG_V1.pdf), §2.2.1 tr. 8-9; WAN/Wi-Fi/diagnostic có trong mục lục ở tr. 19/31/63, chưa đọc sâu.
- Archer C54 EU REV1.0.0: [User Guide PDF](https://static.tp-link.com/2020/202008/20200825/1910012708_Archer%20C54%28EU%29_UG_V1.pdf), §2.2.1 tr. 9-10; WAN/Wi-Fi/diagnostic mục lục tr. 19/31/59.
- Archer A9 REV6.0.2: [User Guide PDF](https://static.tp-link.com/2020/202006/20200601/1910012807_Archer%20A9_UG.pdf), §2.2 tr. 8, §4.1-4.2 tr. 14-17, §14.6 tr. 76, §15.3 tr. 83.

- Archer AX90 REV1.0.0: [User Guide PDF](https://static.tp-link.com/2020/202009/20200917/1910012880_Archer%20AX90US%29_UG_REV1.0.0.pdf), §2.2 tr. 8-9; §4.1-4.3 tr. 13-16; Wi-Fi §6.1 tr. 28-29. Region not explicitly named on cover; filename includes US.
- Archer GX90 US REV1.0.0: [User Guide PDF](https://static.tp-link.com/2021/202101/20210107/1910012816_Archer%20GX90%28US%29_UG_REV1.0.0_V2.pdf), [QIG](https://static.tp-link.com/2020/202011/20201119/7106508927_Archer%20GX90%28US%29_QIG_V1.pdf); QIG includes port selection and internet FAQ; User Guide full sections identified but not deeply read.
- Archer AXE75 REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2022/202203/20220316/1910013121_Archer%20AXE75_UG_REV1.0.0.pdf), §4.1/4.3 tr. 14-17, §6.1 tr. 28-29; REV1.0.1 guide exists separately and was not used.
- Archer BE550 REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2023/202307/20230721/1910013423_Archer%20BE550_UG_REV1.0.0.pdf), §2.2 tr. 8, §4.1/4.3 tr. 13-16, §7.1 tr. 33-35. REV2.0.0 guide found but not opened.
- Archer BE800 REV1.0.0: [User Guide PDF](https://static.tp-link.com/upload/manual/2023/202305/20230512/1910013397_Archer%20BE800_UG_REV1.0.0.pdf), §2.2 tr. 8-9, §4.1/4.3 tr. 14-18, §7.1 tr. 32-34.


## Cập nhật kết quả sau khi mở thêm guide - 24/11/2026

**Số liệu hiện hành:** danh mục có 50 trang model và cả 50 trang còn tồn tại. Đã mở trực tiếp tài liệu User Guide/QIG hãng cho ít nhất **45/50 model**. Đây là số model có tài liệu trực tiếp được mở, không phải số model hoàn tất xác minh toàn bộ quy trình. **0/50** được xác nhận là khớp thiết bị thực tế vì chưa có Hardware Version và vùng trên tem. Một số guide chỉ mới đọc mục lục hoặc một phần, tình trạng cụ thể nằm ở từng trang.

Đã bổ sung năm model: TL-WR846N (EU REV1.0.0, mới đọc mục lục); Archer C58HP (UN V1 REV1.0.0, đọc thao tác WAN/Wi-Fi/diagnostics); Archer AX11000 (EU/US REV1.0.0, PDF quá lớn để trích thân); Archer BE230 (QIG REV1.0.0, đọc sơ đồ cắm WAN, setup và FAQ); Archer MR600 V4 (guide tiếng Pháp REV1.1.1, nội dung SIM/setup/profile/test đọc một phần). Các link PDF trực tiếp và mục/trang nằm trong từng trang model.

### Còn thiếu guide trực tiếp đã mở

- Archer AX12: chưa tìm được User Guide/QIG trực tiếp trong nguồn hãng tra cứu; cần guide đúng Hardware Version và vùng, gồm đấu nối, setup, WAN, Wi-Fi, lưu, kiểm tra và troubleshooting.
- Archer AX56: chưa tìm được User Guide/QIG trực tiếp; thiếu cùng các mục thao tác nêu trên.
- Archer MR100: chưa mở được User Guide/QIG; thiếu sơ đồ SIM, setup, APN/profile, Wi-Fi, lưu, kiểm tra và xử lý lỗi.
- Archer MR105: chưa mở được User Guide/QIG; thiếu sơ đồ SIM, setup, APN/profile, Wi-Fi, lưu, kiểm tra và xử lý lỗi.
- Archer MR6400: chưa mở được User Guide/QIG; thiếu sơ đồ SIM, setup, APN/profile, Wi-Fi, lưu, kiểm tra và xử lý lỗi.

Với năm trang còn lại, chỉ có trang hỗ trợ model để định hướng tìm kiếm, không dùng làm chứng cứ thao tác. Các phần còn thiếu trên 45 trang khác cũng được nêu riêng; số liệu 45 không đồng nghĩa đã đạt điều kiện nghiệm thu quy trình đầy đủ. PPPoE/VLAN/bridge/DSL/APN và thông tin đăng nhập cần ISP xác nhận. Không có thao tác thiết bị hay thử thông tin đăng nhập.


## Cập nhật tiếp theo - 24/11/2026

Đã mở User Guide trực tiếp cho TL-MR100 EU REV1.0.0, TL-MR105 EU REV1.0.0 và PDF TL-MR6400 EU có chênh revision: tên tệp ghi REV4.0.1 nhưng bìa ghi REV4.0.0. Ba trang model đã ghi link sâu và mức xác minh; MR6400 được đánh dấu không thể dùng làm bằng chứng revision cụ thể đến khi giải quyết sai khác.

Mốc tạm thời trước khi mở AX12, MR100 và MR105: **48/50** model đã mở trực tiếp ít nhất một User Guide/QIG. Trạng thái này được thay thế bởi mục kết quả hiện hành bên dưới. **0/50** xác nhận áp dụng cho thiết bị thực tế do thiếu Hardware Version/vùng trên tem. Hai model chưa tìm được User Guide/QIG trực tiếp: **Archer AX12** và **Archer AX56**. Với AX12 chỉ xuất hiện datasheet và trang hỗ trợ trong kết quả; đó không phải tài liệu thao tác. Với AX56 chưa có tài liệu hướng dẫn trực tiếp mở được. Mỗi trang còn nêu rõ nội dung thao tác chưa có căn cứ. Các guide EU/US/V1 không được suy rộng sang biến thể khác.


## Kết quả hiện hành sau các cập nhật liên tiếp - 24/11/2026

Đủ **50/50 trang model** hiện có trong Wiki và đã được rà soát/trạng thái theo model. Đã mở trực tiếp **49/50 User Guide hoặc Quick Installation Guide** chính hãng. Archer AX12 đã có User Guide EU V1 REV1.0.0, nội dung cài đặt được đọc. Archer AX56 có tài liệu chính hãng “Product and Installation Guide” cho AX56 1.0 trên website India, nội dung đấu nối và Quick Setup đã đọc, nhưng không tìm được guide có đúng loại User Guide/QIG; vì vậy không tính AX56 vào 49. Trang AX56 ghi rõ phần còn thiếu và link tài liệu thay thế đã mở.

**Mức áp dụng cho máy thực tế: 0/50**, do không có Hardware Version/vùng trên nhãn thiết bị để chọn biến thể. Số 49 chỉ cho biết có guide đúng loại đã mở, không có nghĩa mọi thao tác trong từng guide đã đọc đủ hoặc máy cụ thể đã kiểm tra. Các phần chưa đọc sâu được đánh dấu riêng tại từng model. TL-MR6400 còn có PDF tên tệp REV4.0.1 nhưng bìa REV4.0.0, nên nội dung thao tác không được coi là xác minh revision.

Còn thiếu tiêu chí cụ thể: **Archer AX56 User Guide hoặc Quick Installation Guide** đúng model/revision/vùng, gồm chi tiết WAN options, Wi-Fi/menu/lưu và connectivity/troubleshooting. Các guide EU/US khác chỉ áp dụng cho revision/khu vực ghi trên trang tương ứng; ISP phải xác nhận PPPoE, VLAN, bridge, DSL, APN và credentials. Không có thao tác thiết bị hoặc thử thông tin đăng nhập.

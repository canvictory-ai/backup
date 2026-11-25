# Javis Index (tầng vận hành)

> Tự sinh từ file - ĐỪNG sửa tay. Chỉ mục mọi năng lực của Javis trong brain này để bất kỳ AI/engine đọc 1 chỗ là hiểu Javis làm được gì. Song song `wiki/index.md` (tri thức).

**Tổng quan:** 7 agents · 9 skills · 0 workflows (0 bật) · 1 loops (0 bật) · 36 plugins (35 chạy)

## Agents
- **Dịch vụ và Theo dõi công việc** (`dich-vu-theo-doi-cong-viec`) - Tiếp nhận và theo dõi ca sửa chữa, bảo hành và công việc phát sinh đến khi có kết quả rõ ràng. · tags: Vận hành
- **Javis Core** (`javis-core`) - Trợ lý hệ thống nhận báo cáo và hỗ trợ công việc trong brain này.
- **Luna Vũ - Hỗ trợ kỹ thuật Zalo** (`luna-vu`) - Hỗ trợ kỹ thuật và cung cấp thông tin Victory khi khách hỏi trong nhóm Zalo được phép. · model gpt-6-luna · tags: Vận hành, Kỹ thuật
- **Lập Báo Giá** (`nhan-vien-sales-bao-gia`) - Lập, chỉnh sửa, kiểm tra và gửi báo giá Victory theo hồ sơ, bảng giá YSS và mẫu chuẩn đã lưu. · model gpt-6-luna · skills: lap-bao-gia-victory · tags: Bán hàng
- **Phương sai vặt** (`phuong-sai-vat`) - Trợ lý tổng hợp, cảnh báo và rà soát công việc của chủ. · tags: Điều phối
- **Pháp lý - Luật** (`tro-ly-phap-ly-viet-nam`) - Hỗ trợ tra cứu, giải thích và hệ thống hóa pháp luật Việt Nam dựa trên nguồn có thể kiểm chứng. · tags: Pháp lý
- **Hồ sơ - Hợp đồng** (`tro-ly-soan-thao-ho-so`) - Soạn thảo và rà soát hợp đồng, biên bản, phiếu xuất kho và hồ sơ hành chính Victory theo mẫu đã duyệt. · skills: soan-thao-ho-so-victory · tags: Văn bản, Vận hành

## Skills
### AI
- **Ingest Source** (`ingest-source`) - Tiêu hoá một source thô vào Second Brain, chưng cất thành tri thức wiki tích luỹ.
- **Javis Builder** (`javis-builder`) - Tạo hoặc sửa năng lực của Javis: agent, skill, workflow, loop, plugin. Kèm mẫu file chuẩn và luật chống trùng.
- **Lint Wiki** (`lint-wiki`) - Rà soát sức khoẻ wiki của Second Brain, trả về danh sách vấn đề. Không tự sửa hàng loạt.
- **Notes** (`notes`) - Lưu tin nhắn hiện tại nguyên văn vào sources/ (kèm ảnh), tự chưng cất lên wiki nếu note đáng.
- **Query Wiki** (`query-wiki`) - Khai thác tri thức trong Second Brain: tổng hợp, so sánh, giả thuyết. Trả lời có trích dẫn.
### Bán hàng
- **Lập báo giá Victory** (`lap-bao-gia-victory`) - Lập, kiểm tra và gửi báo giá Victory theo hồ sơ, bảng giá YSS và mẫu đã lưu.
### Marketing
- **HTML sang Webcake** (`html-to-webcake`) - Chuyển trang HTML thành file .pke mở được trong trình dựng Webcake, giữ đúng màu, cỡ chữ, ảnh và bố cục của bản gốc.
### Security
- **Security Audit** (`security-audit`) - Rà soát bảo mật mã nguồn, API, dịch vụ: tìm lỗ hổng có bằng chứng, kiểm chứng độc lập từng lỗi, báo cáo kèm cách sửa. Từ Cloudflare.
### Vận hành
- **Soạn thảo hồ sơ Victory** (`soan-thao-ho-so-victory`) - Soạn và rà soát hợp đồng, biên bản, phiếu xuất kho và hồ sơ hành chính Victory theo mẫu đã duyệt.

## Workflows
_(chưa có)_

## Loops
- **Theo dõi nhóm Nội bộ Sửa chữa - Bảo hành** (`theo-doi-nhom-noi-bo-sua-chua-bao-hanh`) - tắt · custom/auto · mỗi 5 phút

## Plugins (tool/hook native cho mọi engine)
- **Thời gian & ngày** (`datetime-vn`) - bundled/chạy · tools: javis_now, javis_date_add · Xem ngày giờ hiện tại theo múi giờ chọn ở Cài đặt và tính ngày tương đối (mai, mốt, N ngày nữa, tuần trước). Thuần stdlib, chỉ đọc, không cần mạng.
- **Điều khiển app trên máy** (`desktop-apps`) - bundled/chạy · tools: javis_app_list, javis_app_open, javis_app_close · Mở, đóng và liệt kê ứng dụng trên CHÍNH MÁY đang chạy Javis (Windows, macOS, Linux có màn hình) theo lời người dùng, ví dụ "mở Chrome", "tắt Excel", "đang mở app nào". Tự chặn và nói rõ khi Javis chạy trong Docker trên máy chủ, vì khi đó máy chạy Javis không phải máy của người dùng.
- **Tạo và xem ảnh (ChatGPT)** (`image-chatgpt`) - bundled/chạy · tools: javis_generate_image, javis_describe_image · Tạo ảnh từ mô tả bằng GÓI ChatGPT đang đăng nhập (OAuth) - không cần OpenAI API key. Dùng Codex Responses API + tool image_generation (gpt-image-2). Ảnh lưu vào attachments/ của vault để nhúng thẳng vào chat. Kèm tool XEM ảnh, để ChatGPT nhìn ảnh trong brain rồi tả lại bằng chữ, để cả engine không tự xem được ảnh (OpenRouter, Gemini API...) cũng biết trong ảnh có gì. Cần đã kết nối ChatGPT ở trang Model.
- **Trả lời khách từ Hội thoại** (`inbox-reply`) - bundled/chạy · tools: inbox_find, inbox_reply · Tìm hội thoại khách trên trang Hội thoại và gửi tin trả lời, ảnh hay file trong brain ngay vào đó, đúng kênh của cuộc chat (Messenger, Instagram, Telegram, Zalo...), như chủ gửi ở Hộp thư.
- **Đấu thêm MCP** (`javis-connect`) - bundled/chạy · tools: javis_add_mcp · Đấu một MCP server vào kho Kết nối của Javis ngay từ chat, để nó HIỆN ra trang Kết nối như mọi tài khoản khác. Trước tool này Javis chỉ còn đường `claude mcp add` - thứ rơi vào config riêng của Claude Code, không bộ não nào khác thấy và người dùng cũng không thấy trên trang Kết nối.
- **Tên và phong cách của Javis Core** (`javis-core-name`) - bundled/chạy · tools: javis_core_name · Cho người dùng đặt tên riêng và phong cách nói chuyện cho Javis Core của brain này, ngay trong chat. Tên hiện trên trang Cộng sự. Chỉ phiên của chủ thấy tool này.
- **GitHub trong khung chat** (`javis-github`) - bundled/chạy · tools: javis_github · Xem trạng thái repo GitHub của khung chat (nhánh, PR, CI, merge), xếp việc kế tiếp để Javis tự làm khi PR hiện tại đã merge xong, và review chéo PR khi người dùng yêu cầu.
- **Mục tiêu (Hệ thống cộng hưởng)** (`javis-goal`) - bundled/chạy · tools: javis_goal, javis_submit_deliverable · Cho bộ não tự lập một mục tiêu bền khi người dùng giao việc cần theo đuổi sau lượt chat, hoặc cập nhật mục tiêu đang mở khi người dùng bổ sung ý. Host kiểm đề xuất theo SMART và lưu có revision. Chỉ hiện ở brain đã bật Hệ thống cộng hưởng.
- **Tự cải tiến theo yêu cầu** (`javis-improve`) - bundled/chạy · tools: javis_improve · Khi chủ yêu cầu, Javis hay một trợ lý tự sửa chính nó và brain (trợ lý, skill, workflow, vòng lặp, bộ nhớ) có sao lưu và hoàn tác, sửa mã nguồn Javis qua GitHub. Không tự cập nhật, lên bản mới do chủ bấm ở trang Cập nhật. Chỉ phiên của chủ thấy tool này.
- **Việc chạy nền** (`javis-job`) - bundled/chạy · tools: javis_job · Theo dõi lệnh chạy ngầm engine bỏ lại (render, build, tải về). Dặn trước "xong thì làm tiếp gì", xem việc đang chạy, dừng một việc. Xong là Javis tự báo về đúng khung chat và tự làm tiếp.
- **Cookies** (`javis-login`) - bundled/chạy · tools: javis_login · Mở trang web cần đăng nhập bằng phiên chủ đã cất ở trang Cookies, đọc hoặc bấm và điền form trong trình duyệt. Không bao giờ trả cookie.
- **Trí nhớ qua chat** (`javis-memory`) - bundled/chạy · tools: javis_memory · Cho Javis xem, sửa, quên ghi nhớ của brain, bật tắt việc lưu ghi nhớ mới, sửa hồ sơ chung và thu hồi bài học của trợ lý khi người dùng nhắn. Thay cho các danh sách trí nhớ và bài học từng nằm ở cột Cài đặt. Chỉ phiên của chủ thấy tool này.
- **Việc của tôi và thói quen** (`javis-mine`) - bundled/chạy · tools: javis_mytask · Thêm, sửa, xoá việc, lịch hẹn và thói quen trong tab Của tôi trên trang Nhiệm vụ (đổi việc lặp thành lịch hẹn, đổi giờ, đổi lặp, bỏ qua một lần), xem lịch và tích xong khi người dùng báo đã làm, ngay từ chat.
- **Chỉ huy thông báo** (`javis-notify`) - bundled/chạy · tools: javis_notify · Xem và đổi thông báo nào được báo. Mỗi nhóm thông báo có một chế độ (tất cả, đáng chú ý trở lên, chỉ tin khẩn, tắt); lọc hoặc luôn báo một loại tin; hoàn tác thay đổi của Javis Core.
- **Tạo plugin qua chat** (`javis-plugin`) - bundled/chạy · tools: javis_plugin · Cho Javis tạo, đọc và sửa plugin của người dùng ngay tại chỗ khi được nhờ trong chat, không phải tải file zip về rồi tải lên lại. Plugin mới hoặc vừa đổi mã luôn nằm TẮT, chủ đọc mã rồi tự bật ở trang Plugins. Chỉ phiên của chủ thấy tool này.
- **Project tự học** (`javis-project`) - bundled/chạy · tools: javis_project · Cho Javis tự ghi điều học được về một project trong lúc làm việc, tự gắn file và link kèm mô tả một dòng cho project, cộng sự hay nhóm, và sửa hướng dẫn riêng của project khi người dùng bảo. Chỉ phiên của chủ thấy tool này.
- **Bộ phán xử của bot nhóm** (`javis-reply-policy`) - bundled/chạy · tools: javis_reply_policy, javis_reply_policy_tune · Cho Javis đọc số liệu bộ phán xử (bot nói hay im trong nhóm, vì sao, bị chấm sai ở đâu) và chỉnh nó khi chủ nhờ, rồi hoàn lại được. Chỉ phiên của chủ thấy hai tool này, bot chăm khách không bao giờ thấy.
- **Đặt việc định kỳ & nhắc hẹn** (`javis-schedule`) - bundled/chạy · tools: javis_schedule · Tạo/liệt kê/huỷ việc chạy định kỳ và nhắc hẹn ngay từ chat. Tự chọn kho - việc lặp và bền thì ghi Javis/loops/<slug>.md để sửa được trong Obsidian; nhắc một lần hoặc lịch cron thì vào kho nhắc hẹn (đã có sẵn cron 5 trường). Thay cho việc gõ YAML tay hoặc curl.
- **Giao việc Kanban** (`javis-task`) - bundled/chạy · tools: javis_task · Giao một việc nền vào hàng đợi Kanban và xem việc đang chạy tới đâu, ngay từ chat. Trước tool này chỉ engine chạy được lệnh máy (Claude Code, Codex) mới giao việc được, vì đường duy nhất là curl POST /kanban/task - năm engine API đứng ngoài.
- **Quản lý nhóm chat** (`javis-team`) - bundled/chạy · tools: javis_team · Tạo, sửa, lưu trữ và xoá nhóm chat, thêm bớt trợ lý, chọn trưởng nhóm, tạo trợ lý mới với model riêng rồi ghép vào nhóm, ngay từ chat và trên mọi engine. Trước tool này phải vào trang Nhóm bấm tay, hoặc điều khiển trình duyệt.
- **Việc nền tự điều chỉnh** (`javis-tune`) - bundled/chạy · tools: javis_tune · Cho Javis xem và chỉnh cách việc nền tự chọn model theo lời người dùng trong chat (tiết kiệm token, làm cho chắc, việc này làm sai). Chỉ phiên của chủ thấy tool này.
- **Điều khiển dashboard** (`javis-ui`) - bundled/chạy · tools: javis_ui · Mở trang, mở file trong brain, mở một việc Kanban hoặc cuộn khung chat trên dashboard đang mở, theo lời người dùng nói hoặc gõ. Dashboard xác nhận đã làm xong ngay trong lượt; không có tab nào mở thì tool nói rõ.
- **Theo dõi trang web** (`javis-watch`) - bundled/chạy · tools: javis_watch · Canh một trang web theo lịch mà không tốn token - báo khi trang đổi, khi xuất hiện một cụm chữ hoặc khi có giá dưới ngưỡng (hiểu 1.250.000đ, 1,5 triệu, 250k, $20). Chỉ gọi AI khi bật tóm tắt.
- **Lịch sử quy trình** (`javis-workflow`) - bundled/chạy · tools: javis_workflow · Xem các lần chạy quy trình gần đây và kết quả từng lần, ngay từ chat. Trước tool này, chạy quy trình xong là kết quả mất, hỏi "quy trình chạy gần nhất ra sao" Javis không có gì để tra.
- **Kiểm tra Messenger** (`messenger-health`) - bundled/chạy · tools: messenger_check, messenger_repair · Rà kết nối bot Messenger của từng Fanpage (token Trang, quyền, webhook, Trang gắn app, bot đang trực) và sửa tự động phần webhook khi bot im lặng.
- **Meta Ads (Graph API)** (`meta-ads-graph`) - bundled/chạy · tools: meta_ads_accounts, meta_ads_insights, meta_ads_campaigns, meta_ads_get · Đọc số liệu quảng cáo Facebook/Instagram (tài khoản ads, chiến dịch, hiệu suất) qua Graph API, dùng token của kết nối "Meta Ads (tự tạo app)". CHỈ ĐỌC, không tiêu tiền.
- **Facebook Trang (Graph API)** (`meta-pages-graph`) - bundled/chạy · tools: fb_pages_list, fb_page_posts, fb_page_comments, fb_page_scheduled, fb_page_post, fb_page_photo, fb_page_album, fb_page_video, fb_page_edit, fb_page_delete, fb_page_reply · Quản lý Trang/Fanpage Facebook qua Graph API - liệt kê Trang, đọc bài, bình luận và bài đang chờ đăng (chỉ đọc), đăng hoặc hẹn giờ bài/ảnh/album, đăng video, sửa chữ, xoá bài và trả lời bình luận (toàn quyền). Dùng Fanpage đã nối ở thẻ Facebook Messenger (trang Kết nối), hoặc kết nối "Facebook Trang" trong Kho nếu có.
- **Nhật ký dùng tool** (`tool-audit`) - bundled/tắt · tools: javis_tool_stats · hooks: post_tool_call · Đếm số lần MỖI tool được engine gọi (qua hook post_tool_call) và cho xem thống kê tool hay dùng. Đây là ví dụ minh hoạ cơ chế HOOK của plugin. Mặc định TẮT - bật qua POST /plugins/toggle (slug=tool-audit) để thử.
- **Tin thoại** (`voice-note`) - bundled/chạy · tools: javis_voice_note · Javis ghi một đoạn nói ngắn (tối đa 1000 ký tự) thành file mp3 trong attachments/voice/ rồi nhúng vào câu trả lời. Khung chat hiện trình phát, Telegram nhận file âm thanh. Dùng giọng Edge miễn phí theo ngôn ngữ của câu.
- **Đọc video YouTube** (`youtube-read`) - bundled/chạy · tools: javis_youtube_read · Đọc lời thoại (phụ đề) của video YouTube từ link để tóm tắt. Tự đổi qua 6 kiểu trình phát rồi tới yt-dlp khi YouTube chặn máy chủ. Không cần đăng nhập, không cần API key.
- **Zalo kết bạn - tìm người, xem và xử lý lời mời** (`zalo-friend`) - pack/chạy · tools: zalo_find_user, zalo_find_phones, zalo_search_friends, zalo_friend_status, zalo_friend_requests, zalo_sent_friend_requests, zalo_add_friend, zalo_accept_friend, zalo_reject_friend, zalo_undo_friend_request · Công cụ kết bạn trên Zalo cá nhân bằng chính tài khoản đã quét QR ở trang Kết nối - tìm người theo số điện thoại (một hay nhiều số) hoặc username, tìm theo tên trong danh sách bạn bè, xem trạng thái kết bạn, xem lời mời đang chờ duyệt và lời mời đã gửi, gửi, nhận, từ chối hoặc rút lại lời mời. Chỉ là công cụ, kết bạn với ai do model quyết định hoặc theo yêu cầu của người dùng.
- **Zalo nhóm - tag người, ghi chú, nhắc hẹn, poll** (`zalo-group`) - pack/chạy · tools: zalo_group_members, zalo_send_mention, zalo_create_note, zalo_create_reminder, zalo_create_poll · Tag ĐÚNG người trong nhóm Zalo (nói tên, Javis tự tìm ID Zalo thật), liệt kê thành viên, tạo ghi chú nhóm, tạo nhắc hẹn và tạo poll, bằng chính tài khoản đã quét QR ở trang Kết nối. Bù đúng chỗ MCP chuẩn của zalo-agent-cli còn thiếu - nó chỉ có bảy tool và tool gửi tin chỉ nhận chữ.
- **Gửi ảnh & file qua Zalo** (`zalo-image`) - pack/chạy · tools: zalo_send_image · Gửi ẢNH hoặc FILE qua Zalo kèm lời nhắn, bằng chính tài khoản đã quét QR ở trang Kết nối. Bù đúng chỗ MCP chuẩn của zalo-agent-cli còn thiếu - tool zalo_send_message của nó chỉ nhận chữ.
- **Đọc ảnh trong nhóm Zalo** (`zalo-read-images`) - pack/chạy · tools: zalo_read_images · Lấy ẢNH người ta gửi trong nhóm Zalo về brain (attachments/zalo/) rồi cho bộ não xem được nội dung ảnh, bằng chính tài khoản đã quét QR ở trang Kết nối. Engine tự xem được ảnh (Claude Code, Codex) mở thẳng file; engine khác nhận lời tả của ChatGPT trên gói đang đăng nhập. Bù đúng chỗ MCP chuẩn của zalo-agent-cli còn thiếu - nó chỉ trả link ảnh và giữ tin 2 giờ.
- **Danh bạ Zalo** (`zalo-contactbook`) - user/chạy · tools: zalo_contactbook · Lưu và tra cứu danh bạ dùng chung, phân loại thành viên Zalo là người công ty hoặc đối tác.
- **Theo dõi cơ hội bán hàng** (`theo-doi-co-hoi-ban-hang`) - vault/chạy · tools: sales_opportunity · Tạo, xem, cập nhật giai đoạn và lưu trữ cơ hội bán hàng ngay trong Javis.

## Cờ sức khoẻ
- Agent chưa workflow nào dùng: dich-vu-theo-doi-cong-viec, javis-core, luna-vu, nhan-vien-sales-bao-gia, phuong-sai-vat, tro-ly-phap-ly-viet-nam, tro-ly-soan-thao-ho-so

# Vault Schema (Javis Second Brain)

> AI làm việc trên vault này PHẢI đọc file này trước. Mục tiêu: biến vault thành một **wiki
> tích luỹ (compounding)** - tri thức được chưng cất MỘT LẦN từ nguồn rồi DUY TRÌ sống, không
> RAG lại mỗi câu hỏi. Vault tiến hoá dần theo người dùng; taxonomy tự mọc theo nội dung thật.

## 1. Ba lớp (phân quyền rõ)

| Lớp | Thư mục | Ai sửa | Tính chất |
|---|---|---|---|
| Nguồn thô | `sources/` | Người dùng | BẤT BIẾN với AI - chỉ đọc, không sửa nội dung (được đổi tên/thêm frontmatter). Source of truth. |
| Wiki | `wiki/` | AI | AI toàn quyền tạo/cập nhật/merge/archive. Người đọc và định hướng. |
| Schema | `CLAUDE.md` / `AGENTS.md` | Người + AI cùng tiến hoá | Quy ước; chỉnh khi workflow đổi. |
| Bộ nhớ | `memory/` | AI | Ký ức dài hạn về người dùng (facts + MEMORY.md index + conversations). |
| Vận hành | `agents/`, `workflows/`, `skills/` (mirror `.claude/skills`) | AI + người | Agent, workflow, kỹ năng. |

Nguyên lý: Sources -> (INGEST) -> Wiki. Tri thức TÍCH LUỸ, không tái phát hiện.

## 2. Đặt tên & wikilink
- Wiki: tên khái niệm rõ ràng (vd `Nguyên Lý Pareto.md`). Liên kết bằng `[[Tên Wiki]]`.
- Tên trùng giữa các folder -> dùng path `[[nhóm/Tên]]`. Khi 2 thực thể trùng tên -> hỏi người dùng trước khi tạo trang mới.
- Trong chat: ưu tiên `[[wikilink]]` để người dùng click mở.

## 3. Ba kỷ luật chống Wiki rỗng/sai (BẮT BUỘC)
1. **Citation trong thân bài.** Mọi khẳng định cụ thể (số liệu/quy trình/framework/trích dẫn) phải kèm `[[Nguồn]]` cuối câu/đoạn. Không nguồn = câu đáng ngờ, dễ bịa.
2. **Phân biệt mục tiêu vs thực tế.** Câu nói về tương lai/mong muốn -> ghi rõ "mục tiêu/kế hoạch". Câu về hiện trạng đo được -> ghi rõ "thực tế tính đến [thời điểm]". Không chắc -> trích nguyên văn + "(cần xác minh)" thay vì viết thành claim chắc nịch.
3. **Mâu thuẫn giữ rõ, không ghi đè.** Source mới mâu thuẫn Wiki cũ -> KHÔNG xoá cái cũ. Thêm section `## Mâu thuẫn` (ghi cả 2 quan điểm + nguồn) và append 1 dòng vào `wiki/_open-questions.md`. Người dùng quyết định hợp nhất.

## 4. Ba phép toán
### INGEST - tiêu hoá 1 source
Kiểm frontmatter source: `status: processed` -> DỪNG, hỏi re-ingest. `unprocessed`/chưa có -> làm.
- Source dài (>= ~10.000 dòng / sách / transcript) -> 3-pass: (1) đọc lướt lập mục lục theo dòng, (2) đọc sâu từng đoạn ~1.000-1.500 dòng và viết Wiki ngay từng đoạn (đừng nén cả file 1 lần), (3) tự hỏi 5 câu kiểm độ phủ, thiếu thì quét bổ sung.
- Các bước: đọc (kèm ảnh nếu có) -> tóm tắt 3-5 ý -> rút insight/framework -> xác định trang Wiki mới/cập nhật/merge -> viết Wiki (1 trang = 1 ý, có `[[...]]` ngược) -> cập nhật `wiki/index.md` -> set source `status: processed` + `wiki_links` -> append `wiki/log.md` -> đề xuất task nếu có (không tự thêm). Báo cáo ngắn.

### QUERY - trả lời câu hỏi
Đọc `wiki/index.md` trước -> đọc trang liên quan -> thiếu thì đọc `sources/` -> vẫn thiếu thì append `wiki/_open-questions.md`. Trả lời có `[[citation]]`. Câu trả lời giá trị tái dùng -> đề xuất lưu thành trang Wiki mới (compounding).

### LINT - health-check định kỳ (chỉ trả CHECKLIST, KHÔNG tự sửa 50 chỗ)
Quét `wiki/`: mâu thuẫn, claim cũ, orphan (không inbound link), khái niệm thiếu trang riêng, broken `[[link]]`, trùng lặp nên merge, vùng mỏng cần thêm source, open-question tồn lâu. Báo cáo -> người dùng chọn sửa từng cái.

## 5. Điều hướng
- `wiki/index.md` - catalog nội dung (link + mô tả 1 dòng), cập nhật mỗi INGEST. Đọc file này TRƯỚC khi QUERY.
- `wiki/log.md` - nhật ký thời gian, append-only, mỗi entry mở đầu `## [YYYY-MM-DD] loại | tiêu đề`.
- `wiki/_open-questions.md` - câu hỏi Wiki chưa trả lời đủ.
- `wiki/_session-handoff.md` - trạng thái phiên hiện hành để CHUYỂN GIỮA CÁC MODEL/AI (Claude <-> Codex...) không mất mạch. Ghi: mục tiêu, đã xong, đang làm, quyết định, chưa xác minh, bước tiếp, file liên quan. Khi xong đặt `status: clear`. AI nhận bàn giao đọc: schema -> handoff -> file liên kết.

## 6. Frontmatter
Wiki: `type: wiki`, `status: active|draft|archived`, `tags: [wiki, <nhóm>]`, `created`, `updated`, `source: [[...]]`.
Source: `type: source`, `source_kind: article|book|podcast|video|own-note|screenshot|chat`, `status: unprocessed|processed`, `created`, `processed_at`, `wiki_links: [...]`, `url`.

## 7. Chỉ mục năng lực
- `Javis/index.md` - chỉ mục MỌI năng lực (agents/skills/workflows/loops/lịch), tự sinh từ file (đừng sửa tay). Đọc file này để biết Javis đang có gì; kiểm TRƯỚC khi tạo năng lực mới để khỏi trùng. Song song `wiki/index.md` (tri thức).

## 8. Tiến hoá theo người dùng
- Nhóm chủ đề trong `wiki/` MỌC DẦN theo source thực tế (tạo subfolder khi một chủ đề đủ dày), không định sẵn theo ngành.
- Cần bộ khung sẵn (vd Bullet Journal, nghiên cứu, đọc sách) -> người dùng áp "gói mẫu" (opt-in), không seed mặc định.
- Viết bằng ngôn ngữ ghi ở khối `# === NGÔN NGỮ ===` của prompt (mặc định tiếng Việt); code/tag/frontmatter key luôn dùng tiếng Anh. Tone thực tế, ngắn gọn. KHÔNG dùng ký tự em dash.

## 9. Hợp đồng thực thi yêu cầu sửa và ghi nhớ
- Khi người dùng yêu cầu rõ ràng sửa, xóa, cập nhật hoặc ghi nhớ, thực hiện ngay trong lượt hiện tại trên đúng file/quy tắc có thẩm quyền. Không chỉ phân tích, đề xuất, hỏi lại điều đã rõ, hoặc dừng ở checklist.
- Trước khi sửa, tìm quy tắc hiện hành và các bản trùng liên quan. Quy tắc mới nhất do người dùng nói trực tiếp được ưu tiên; giữ phần cũ còn tương thích, xóa hẳn phần đã lỗi thời hoặc bị thay thế theo yêu cầu của người dùng. Cập nhật đồng bộ nơi có hiệu lực, gồm schema, skill/agent/workflow và memory index nếu liên quan.
- Khi người dùng yêu cầu ghi nhớ, sửa hoặc tạo ngay fact chuẩn trong `memory/facts/` và cập nhật `memory/MEMORY.md`; không để bản cũ mâu thuẫn tiếp tục được nạp. Nếu yêu cầu là xóa quy tắc cũ, xóa fact cũ và dòng index của nó, trừ khi người dùng yêu cầu lưu lịch sử.
- Chỉ nói "đã sửa", "đã ghi nhớ" hoặc "đã xong" sau khi đọc lại file/kết quả tool và xác nhận thay đổi thực sự tồn tại. Nếu mới hoàn thành một phần, nêu rõ phần đã làm và phần còn thiếu; không biến dự định thành kết quả.
- LINT mặc định chỉ báo checklist khi người dùng yêu cầu kiểm tra. Nếu người dùng đồng thời yêu cầu sửa hoặc đã chỉ rõ vấn đề cần khắc phục, hãy sửa các mục được chỉ định ngay; giới hạn "không sửa hàng loạt" chỉ áp dụng cho các lỗi ngoài phạm vi đó.

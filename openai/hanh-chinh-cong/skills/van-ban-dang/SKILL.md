---
name: van-ban-dang
description: Soạn văn bản của tổ chức Đảng đúng Quy định 399-QĐ/TW (09/01/2026) và Hướng dẫn 05-HD/VPTW (27/5/2026) về thể loại, thẩm quyền, thể thức và kỹ thuật trình bày — nghị quyết, quyết định, kết luận, chỉ thị, quy chế, kế hoạch, chương trình, báo cáo, tờ trình, thông báo, hướng dẫn, công văn, biên bản của đảng ủy xã/phường/cơ quan, chi bộ, ban thường vụ; tiêu đề "ĐẢNG CỘNG SẢN VIỆT NAM", dấu sao, số ký hiệu "Số 15-NQ/ĐU", thể thức đề ký T/M, K/T, T/L, nơi nhận "Lưu Văn phòng"; nghị quyết chi bộ hằng tháng, báo cáo kết quả lãnh đạo năm, nghị quyết đại hội chi bộ; xuất Word và cấp số theo sổ văn bản Đảng. Dùng khi người dùng nói "soạn nghị quyết chi bộ", "văn bản đảng ủy", "báo cáo của đảng ủy", "thể thức văn bản Đảng", "nghị quyết tháng chi bộ", "kết luận của ban thường vụ", "công văn của đảng ủy".
---

# Văn bản của Đảng

Đọc trước: `references/nguyen-tac-chung.md`, `references/the-thuc-van-ban-dang.md`, `references/mau-van-ban-dang.md`.

> Căn cứ hiện hành: **Quy định 399-QĐ/TW** và **Hướng dẫn 05-HD/VPTW**. Không dùng Quy định 66-QĐ/TW, Hướng dẫn 36-HD/VPTW làm căn cứ mới. Thông số kỹ thuật gắn [Cần đối chiếu HD 05] → nhắc người dùng kiểm tra với văn phòng cấp ủy (đơn vị thẩm định thể thức).

## Khác biệt với văn bản hành chính (hay nhầm)
| Nội dung | Văn bản Đảng | Văn bản hành chính |
|---|---|---|
| Phần đầu bên phải | "ĐẢNG CỘNG SẢN VIỆT NAM" | Quốc hiệu – Tiêu ngữ |
| Dưới tên cơ quan | Dấu sao (*) | Đường kẻ ngắn |
| Số ký hiệu | **Số 15-NQ/ĐU** (không dấu hai chấm, gạch nối) | Số: 15/QĐ-UBND |
| Đề ký | **T/M**, **K/T**, **T/L** | TM., KT., TL. |
| Nơi nhận | "Nơi nhận:" gạch chân; cuối dòng dấu phẩy; "- Lưu Văn phòng ..." | "Lưu: VT, ..." |
| Kết thúc nội dung | Không có "./." | Có "./." |
| Giãn dòng | 18–22 pt Exactly (HD 05) | Tối thiểu single, tối đa 1,5 lines |

## Quy trình
1. **Cấp ban hành, thể loại, thẩm quyền**: ban chấp hành, ban thường vụ, đảng ủy, chi bộ; thể loại có được cấp đó ban hành không (Quy định 399 quy định thẩm quyền theo cấp) [Cần đối chiếu cho từng cấp]. Ví dụ: chi bộ thường ban hành nghị quyết, báo cáo, kế hoạch, thông báo, biên bản.
2. **Nội dung** theo mẫu `references/mau-van-ban-dang.md`. Nghị quyết: đánh giá ngắn → mục tiêu, chỉ tiêu (số liệu thật) → nhiệm vụ, giải pháp → tổ chức thực hiện. Không sao chép nguyên văn nghị quyết cấp trên – cụ thể hóa cho đơn vị.
3. **Đề ký**: đúng thẩm quyền ("T/M ĐẢNG ỦY – BÍ THƯ"; "T/M CHI BỘ – BÍ THƯ"; "K/T BÍ THƯ – PHÓ BÍ THƯ"; "T/L BAN THƯỜNG VỤ – CHÁNH VĂN PHÒNG").
4. **Rà**: `kiem_tra_the_thuc` với `loai_the_thuc=dang`.
5. **File Word**: `tao_van_ban_docx` với `loai_the_thuc=dang` (tiêu đề Đảng, dấu sao, T/M; giãn dòng 18 pt).
6. **Cấp số sau khi ký**: `cap_so_van_ban_di` với `kieu=dang` (sổ văn bản Đảng tách riêng sổ chính quyền).

## Văn bản thường gặp ở cơ sở
- Nghị quyết chi bộ hằng tháng (sau sinh hoạt chi bộ thường kỳ).
- Báo cáo kết quả lãnh đạo, chỉ đạo 6 tháng/năm; báo cáo kiểm điểm tập thể cấp ủy.
- Kế hoạch học tập, quán triệt nghị quyết; kế hoạch kiểm tra, giám sát.
- Biên bản sinh hoạt chi bộ; biên bản hội nghị đảng ủy.
- Nghị quyết đại hội chi bộ/đảng bộ (theo hướng dẫn tổ chức đại hội của cấp ủy cấp trên).

## Đầu ra
Dự thảo đúng thể thức Đảng · thông tin cần bổ sung · kết quả rà thể thức · file .docx · danh sách điểm cần văn phòng cấp ủy xác nhận.

<!-- KET-NOI:BAT-DAU (sinh tự động từ scripts/ket_noi.json – sửa ở đó rồi chạy build) -->
## Kết nối ứng dụng

Connector dùng cho skill này: **Google Drive** · **Microsoft 365 (Outlook, OneDrive/SharePoint, Teams)**. Đọc quy tắc trong `references/ket-noi.md` trước khi dùng.

1. Lấy nghị quyết, báo cáo kỳ trước của chi bộ, đảng ủy (không mật) trên Drive/OneDrive để kế thừa số liệu, chỉ tiêu.
2. Lưu dự thảo vào thư mục của cấp ủy người dùng chỉ.

**Khi chưa kết nối:** làm đủ phần soạn thảo, tính toán; đưa nội dung sẵn để người dùng tự dán vào email, lịch, thư mục; nhắc **một lần** cách bật connector, không dừng việc chỉ vì chưa kết nối.
<!-- KET-NOI:KET-THUC -->

---
name: soan-van-ban-nha-nuoc
description: Soạn văn bản hành chính của cơ quan nhà nước, UBND xã/phường/đặc khu, sở ngành, đơn vị sự nghiệp công lập đúng Nghị định 30/2020/NĐ-CP trong mô hình chính quyền 2 cấp — công văn (đề nghị, đôn đốc, hướng dẫn, phúc đáp, xin ý kiến), quyết định cá biệt (giao nhiệm vụ, thành lập ban chỉ đạo/tổ công tác, kiện toàn, phê duyệt, ban hành quy chế), thông báo (kết luận, lịch công tác), kế hoạch, tờ trình, báo cáo, giấy mời, giấy giới thiệu; thẩm quyền ký TM. UBND, KT. CHỦ TỊCH, TL., TUQ.; tên cơ quan sau hợp nhất; xuất Word chuẩn và cấp số sau khi ký. Dùng khi người dùng nói "soạn công văn của UBND xã", "dự thảo quyết định thành lập tổ công tác", "kế hoạch triển khai", "thông báo kết luận", "tờ trình UBND", "công văn gửi Sở", "quyết định kiện toàn ban chỉ đạo".
---

# Soạn văn bản hành chính nhà nước

Đọc trước: `references/nguyen-tac-chung.md`, `references/the-thuc-nd30.md`, `references/mau-van-ban-nha-nuoc.md`.

## Bước 1 – Xác định đúng
1. **Cơ quan ban hành và thẩm quyền**: UBND (tập thể) hay Chủ tịch UBND; cơ quan chuyên môn (Sở, phòng chuyên môn thuộc UBND xã); đơn vị sự nghiệp. Văn bản thuộc thẩm quyền tập thể UBND → ký "TM. ỦY BAN NHÂN DÂN – CHỦ TỊCH"; Phó Chủ tịch ký thay → "TM. ỦY BAN NHÂN DÂN – KT. CHỦ TỊCH – PHÓ CHỦ TỊCH"; văn bản thuộc thẩm quyền Chủ tịch → "CHỦ TỊCH" hoặc "KT. CHỦ TỊCH".
2. **Tên loại** đúng 29 loại văn bản hành chính của NĐ 30 (công văn, quyết định cá biệt, thông báo, kế hoạch, báo cáo, tờ trình, giấy mời...). Quyết định có nội dung quy phạm → skill `van-ban-quy-pham-phap-luat`.
3. **Tên cơ quan sau sắp xếp 2025**: dùng tên đơn vị hành chính, cơ quan mới (Sở Nội vụ, Sở Tài chính, UBND phường X...). Người dùng ghi tên cũ (UBND huyện, Phòng LĐTBXH...) → cảnh báo và hỏi cơ quan tiếp nhận nhiệm vụ.

## Bước 2 – Nội dung (mẫu: `references/mau-van-ban-nha-nuoc.md`)
- **Công văn**: căn cứ/lý do → nội dung yêu cầu cụ thể (ai – làm gì – thời hạn – gửi kết quả về đâu) → kết thúc.
- **Quyết định cá biệt**: căn cứ (Luật Tổ chức chính quyền địa phương 2025; văn bản chuyên ngành; "Theo đề nghị của...") → Điều 1, 2, 3 (Điều cuối: Chánh Văn phòng/Văn phòng HĐND – UBND, thủ trưởng các cơ quan, đơn vị và cá nhân có liên quan chịu trách nhiệm thi hành).
- **Kế hoạch**: mục đích – yêu cầu → nhiệm vụ, giải pháp (bảng: Nhiệm vụ | Cơ quan chủ trì | Phối hợp | Thời gian | Sản phẩm) → kinh phí → tổ chức thực hiện, chế độ báo cáo.
- **Thông báo kết luận**: "Thông báo kết luận của đồng chí ... tại cuộc họp ..." → tóm tắt nội dung → kết luận và giao nhiệm vụ cụ thể (skill `hop-hoi-nghi-phat-bieu`).
- Số liệu, chỉ tiêu: chỉ dùng số liệu người dùng cung cấp; thiếu → `[CẦN SỐ LIỆU]`.
- Hạn hoàn thành ghi ngày cụ thể: tính bằng `ngay_lam_viec` / `cong_ngay_lich`.

## Bước 3 – Rà, xuất, cấp số
1. `kiem_tra_the_thuc` (`van_ban`) → sửa hết lỗi CHẶN, CẦN SỬA.
2. File Word: `tao_van_ban_docx` (A4, lề NĐ 30, Times New Roman, phần đầu 2 cột).
3. Không tự cấp số; sau khi ký: `cap_so_van_ban_di` (skill `van-thu-co-quan`). Văn bản điện tử: ký số người có thẩm quyền + chữ ký số cơ quan, phát hành trên hệ thống quản lý văn bản.

## Đầu ra
Dự thảo hoàn chỉnh · bảng thông tin cần bổ sung · kết quả tự rà thể thức · file .docx (nếu cần) · lưu ý thẩm quyền ký.

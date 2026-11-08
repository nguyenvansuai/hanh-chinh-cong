---
name: bao-cao-ke-hoach
description: Soạn báo cáo và kế hoạch cho cơ quan nhà nước, đảng ủy, đơn vị sự nghiệp — báo cáo định kỳ tháng/quý/6 tháng/năm với kỳ chốt số liệu theo Nghị định 09/2019 (15/12 năm trước đến 14/12), báo cáo chuyên đề, báo cáo sơ kết, tổng kết, báo cáo đột xuất, báo cáo kết quả thực hiện nghị quyết; kế hoạch năm, chương trình công tác, kế hoạch triển khai văn bản cấp trên; tổng hợp số liệu từ nhiều đơn vị (Excel), so sánh kế hoạch – cùng kỳ, phân tích nguyên nhân chủ quan/khách quan, phương hướng có chỉ tiêu, kiến nghị cụ thể; tránh văn phong sáo rỗng. Dùng khi người dùng nói "viết báo cáo 6 tháng", "báo cáo tổng kết năm", "báo cáo sơ kết", "kế hoạch năm 2027", "chương trình công tác", "tổng hợp số liệu báo cáo", "kỳ chốt số liệu báo cáo năm".
---

# Báo cáo – kế hoạch

Đọc trước: `references/nguyen-tac-chung.md`, `references/the-thuc-nd30.md`, `references/the-thuc-van-ban-dang.md`.

## Báo cáo
1. **Xác định**: loại (định kỳ/chuyên đề/sơ kết/tổng kết/đột xuất), cơ quan yêu cầu và văn bản yêu cầu (đề cương, biểu mẫu kèm theo – **bám đúng đề cương cấp trên**), kỳ chốt số liệu (`ky_bao_cao`), hạn gửi.
2. **Số liệu**: nhận file từ các đơn vị (Excel/CSV) → tổng hợp, kiểm tra cộng dồn, đơn vị tính, trùng lặp; tính % so kế hoạch, so cùng kỳ (tăng/giảm, điểm %). Thiếu → `[CẦN SỐ LIỆU: ...]`, liệt kê đơn vị chưa gửi. Không ước lượng thay.
3. **Cấu trúc** (khi không có đề cương riêng):
   - I. Đặc điểm tình hình (ngắn – chỉ yếu tố tác động thật)
   - II. Kết quả thực hiện (theo lĩnh vực/nhiệm vụ; mỗi nội dung có số liệu và so sánh; bảng chỉ tiêu: `Chỉ tiêu | ĐVT | Kế hoạch | Thực hiện | % KH | Cùng kỳ | % so cùng kỳ`)
   - III. Đánh giá chung: ưu điểm; hạn chế, khó khăn; **nguyên nhân** (khách quan, chủ quan – phải có chủ quan); bài học kinh nghiệm (tổng kết)
   - IV. Phương hướng, nhiệm vụ kỳ tới (chỉ tiêu cụ thể, giải pháp gắn với hạn chế đã nêu)
   - V. Đề xuất, kiến nghị (cụ thể: kiến nghị ai – việc gì)
4. **Văn phong**: số liệu thay tính từ ("tăng 12,3% so cùng kỳ" thay "tăng mạnh"); không lặp "đạt được nhiều kết quả quan trọng" nếu không có số liệu kèm; câu chủ động, chủ thể rõ.
5. **Thể thức**: báo cáo chính quyền (NĐ 30) hoặc Đảng (QĐ 399) – rà `kiem_tra_the_thuc`; số ký hiệu `.../BC-...` hoặc `Số ..-BC/ĐU`.

## Kế hoạch / chương trình công tác
- Kế hoạch năm: mục tiêu, chỉ tiêu (lấy từ nghị quyết, chỉ tiêu được giao) → nhiệm vụ, giải pháp → **bảng phân công** `Nhiệm vụ | Chủ trì | Phối hợp | Thời gian hoàn thành | Sản phẩm` → kinh phí → tổ chức thực hiện, chế độ báo cáo (kỳ, hạn).
- Kế hoạch triển khai văn bản cấp trên: cụ thể hóa từng nhiệm vụ được giao cho địa phương, không chép lại văn bản cấp trên.
- Thời gian: ngày cụ thể, tránh lễ Tết (`ngay_le_tet`), tính hạn theo ngày làm việc khi cần.
- Xuất lịch nhắc mốc: `tao_file_ics`.

## Đầu ra
Báo cáo/kế hoạch dự thảo · bảng số liệu tổng hợp (có công thức nếu xuất Excel) · danh sách số liệu còn thiếu và đơn vị chưa gửi · kỳ chốt số liệu và hạn gửi · lịch nhắc.

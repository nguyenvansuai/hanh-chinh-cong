---
name: van-ban-den
description: "Quy trình trọn gói: Tiếp nhận một văn bản đến – trích thông tin, phát hiện mức độ khẩn/mật, đề xuất đơn vị xử lý, tính hạn theo ngày làm việc, đăng ký sổ, soạn phiếu trình."
---

Thông tin cần có từ người dùng: [file/ảnh/nội dung văn bản đến]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Tiếp nhận văn bản đến: yêu cầu của người dùng

Dùng skill `van-thu-co-quan`. Nếu văn bản có dấu hiệu Mật/Tối mật/Tuyệt mật: dừng, nhắc không xử lý trên công cụ AI. Ngược lại: trích thông tin → đề xuất đơn vị xử lý → hạn (`ngay_lam_viec`) → hiển thị dòng sổ, chờ xác nhận → `dang_ky_van_ban_den` → phiếu trình lãnh đạo (nháp).

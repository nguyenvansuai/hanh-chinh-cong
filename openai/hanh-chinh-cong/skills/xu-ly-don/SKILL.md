---
name: xu-ly-don
description: "Quy trình trọn gói: Xử lý một đơn của công dân – phân loại (khiếu nại/tố cáo/kiến nghị), xác định thẩm quyền sau sắp xếp 2 cấp, tính thời hạn theo luật trước hoặc từ 01/7/2026, soạn văn bản xử lý."
---

Thông tin cần có từ người dùng: [nội dung đơn, ngày nhận đơn]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Xử lý đơn: yêu cầu của người dùng

Dùng skill `tiep-dan-khieu-nai-to-cao`: phân loại → thẩm quyền (có nhãn) → `thoi_han_khieu_nai_to_cao` → văn bản phù hợp (hướng dẫn/phiếu chuyển/thông báo thụ lý) → lịch nhắc (`tao_file_ics`). Ẩn thông tin người tố cáo trong mọi văn bản chuyển đi.

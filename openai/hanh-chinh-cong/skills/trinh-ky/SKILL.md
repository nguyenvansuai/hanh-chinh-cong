---
name: trinh-ky
description: "Quy trình trọn gói: Kiểm tra một văn bản (chính quyền hoặc Đảng) trước khi trình ký – rà thể thức tự động, soát thẩm quyền, căn cứ, tên cơ quan sau sắp xếp, báo lỗi 3 mức."
---

Thông tin cần có từ người dùng: [file .docx hoặc nội dung]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Kiểm tra trước trình ký: yêu cầu của người dùng

Dùng skill `kiem-tra-van-ban`: xác định thể thức (nhà nước/Đảng), chạy `kiem_tra_the_thuc`, soát nội dung theo bảng, báo cáo kết luận → bảng lỗi → điểm không kiểm tra được. Văn bản quan trọng: giao thêm skill `tham-dinh-van-ban` thẩm định độc lập.

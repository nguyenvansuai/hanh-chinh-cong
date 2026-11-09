# Hành chính công VN – gói cho ChatGPT / Codex

Thư mục này được sinh tự động bởi `scripts/build_openai.py` – không sửa tay.

12 skill cho cán bộ, công chức, viên chức Việt Nam trong mô hình chính quyền 2 cấp: văn bản hành chính đúng NĐ 30/2020, văn bản Đảng theo Quy định 399-QĐ/TW và Hướng dẫn 05-HD/VPTW, văn bản quy phạm pháp luật, kiểm tra thể thức, văn thư – văn bản điện tử, lập hồ sơ lưu trữ, báo cáo – kế hoạch (kỳ chốt số liệu NĐ 09/2019), một cửa (NĐ 118/2025), tiếp công dân – khiếu nại – tố cáo (Luật 136/2025), đánh giá cán bộ – kiểm điểm đảng viên, thi đua khen thưởng (NĐ 152/2025), hội nghị – bài phát biểu. Không dùng với tài liệu mật.

## Skill (19)

- `bao-cao-ke-hoach`
- `bao-cao-ky`
- `danh-gia-can-bo`
- `hen-tra-ket-qua`
- `hop-hoi-nghi-phat-bieu`
- `kiem-tra-van-ban`
- `lap-ho-so-luu-tru`
- `mot-cua-tthc`
- `phat-bieu`
- `soan-van-ban-nha-nuoc`
- `tham-dinh-van-ban`
- `thi-dua-khen-thuong`
- `tiep-dan-khieu-nai-to-cao`
- `trinh-ky`
- `van-ban-dang`
- `van-ban-den`
- `van-ban-quy-pham-phap-luat`
- `van-thu-co-quan`
- `xu-ly-don`

Chuyển từ lệnh/agent của bản Claude:

- commands/bao-cao-ky.md → skills/bao-cao-ky
- commands/hen-tra-ket-qua.md → skills/hen-tra-ket-qua
- commands/phat-bieu.md → skills/phat-bieu
- commands/trinh-ky.md → skills/trinh-ky
- commands/van-ban-den.md → skills/van-ban-den
- commands/xu-ly-don.md → skills/xu-ly-don
- agents/tham-dinh-van-ban.md → skills/tham-dinh-van-ban

## Cài đặt

Xem README ở gốc repo, mục **ChatGPT / Codex**.

Gói có MCP server chạy cục bộ (Python 3.8+) → chỉ dùng được trên **ChatGPT desktop / Codex**. Skill vẫn tự tính bằng `scripts/cong_cu.py` khi không có MCP.

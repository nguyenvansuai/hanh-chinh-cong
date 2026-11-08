# Plugin Hành chính công cho cán bộ, công chức, viên chức Việt Nam 2026

Plugin trọn bộ cho **cán bộ, công chức, viên chức, văn thư cơ quan nhà nước, UBND xã/phường/đặc khu, sở ngành, đơn vị sự nghiệp và văn phòng cấp ủy** trong mô hình **chính quyền địa phương 2 cấp** (từ 01/7/2025). Gồm **12 skill**, **6 lệnh quy trình**, **1 agent thẩm định** và **1 connector MCP** với 15 công cụ, cập nhật các thay đổi lớn 2025–2026:

- Văn bản hành chính: **Nghị định 30/2020/NĐ-CP** (còn hiệu lực).
- Văn bản Đảng: **Quy định 399-QĐ/TW** (09/01/2026) và **Hướng dẫn 05-HD/VPTW** (27/5/2026) – thay QĐ 66 và HD 36.
- Một cửa: **Nghị định 118/2025/NĐ-CP** (sửa đổi bởi NĐ 367/2025) – thay NĐ 61/2018.
- Khiếu nại, tố cáo, tiếp công dân: **Luật sửa đổi 136/2025/QH15** (hiệu lực 01/7/2026), NĐ 155/2026.
- Thi đua, khen thưởng: **Nghị định 152/2025/NĐ-CP** – thay NĐ 98/2023.
- Báo cáo định kỳ: kỳ chốt số liệu theo **NĐ 09/2019/NĐ-CP**.
- Bộ máy mới: không còn cấp huyện; hợp nhất sở ngành (công cụ kiểm tra tự cảnh báo tên cơ quan cũ).

Nguyên tắc: **không bịa số liệu, căn cứ**, **đúng thẩm quyền – đúng thể thức**, **viện dẫn có nhãn** [Chắc chắn]/[Cần kiểm tra], **không xử lý tài liệu mật**, **chỉ soạn dự thảo** ([POLICY.md](POLICY.md)).

## Thành phần

### Skill (12)
| Nhóm | Skill | Làm gì |
|---|---|---|
| Văn bản | `soan-van-ban-nha-nuoc` | Công văn, quyết định cá biệt, kế hoạch, tờ trình, thông báo của UBND, sở, đơn vị; thẩm quyền TM./KT. |
| | `van-ban-dang` | Nghị quyết, báo cáo, kế hoạch, công văn của đảng ủy, chi bộ theo QĐ 399, HD 05; số "Số 15-NQ/ĐU", T/M |
| | `van-ban-quy-pham-phap-luat` | Nghị quyết HĐND, quyết định quy phạm UBND: thẩm quyền, quy trình, kỹ thuật, tiếp thu giải trình |
| | `kiem-tra-van-ban` | Rà thể thức (nhà nước/Đảng) + soát thẩm quyền, căn cứ, bộ máy mới; lỗi 3 mức |
| Văn thư – lưu trữ | `van-thu-co-quan` | Văn bản đến/đi, cấp số (sổ chính quyền và sổ Đảng), văn bản điện tử ký số, đính chính, bản sao, con dấu |
| | `lap-ho-so-luu-tru` | Danh mục hồ sơ, lập hồ sơ, nộp lưu, bàn giao khi sắp xếp bộ máy, tiêu hủy |
| Điều hành | `bao-cao-ke-hoach` | Báo cáo tháng/quý/6 tháng/năm (kỳ chốt số liệu), tổng kết, kế hoạch năm, chương trình công tác |
| | `hop-hoi-nghi-phat-bieu` | Chương trình, kịch bản, biên bản, thông báo kết luận; bài phát biểu khai mạc, chỉ đạo, kỷ niệm |
| Phục vụ người dân | `mot-cua-tthc` | Hướng dẫn hồ sơ, giấy hẹn (tính ngày làm việc), phiếu bổ sung, từ chối, xin lỗi hẹn lại |
| | `tiep-dan-khieu-nai-to-cao` | Phân loại đơn, thẩm quyền sau sắp xếp, thời hạn luật mới, mẫu thụ lý, quyết định, kết luận |
| Cán bộ | `danh-gia-can-bo` | Tự đánh giá có sản phẩm, nhận xét, kiểm điểm đảng viên, kiểm điểm tập thể, KPI |
| | `thi-dua-khen-thuong` | Phát động, quy chế, xét danh hiệu, hồ sơ, báo cáo thành tích, quyết định khen thưởng |

### Lệnh quy trình (Claude Code)
`/hanh-chinh-cong:van-ban-den` · `/hanh-chinh-cong:trinh-ky` · `/hanh-chinh-cong:bao-cao-ky` · `/hanh-chinh-cong:xu-ly-don` · `/hanh-chinh-cong:hen-tra-ket-qua` · `/hanh-chinh-cong:phat-bieu`

### Agent
`tham-dinh-van-ban` – thẩm định độc lập văn bản quan trọng trước khi trình ký.

### Connector
MCP `hcc-cong-cu` chạy trên máy (Python 3.8+), không kết nối hệ thống công vụ – xem [CONNECTORS.md](CONNECTORS.md).

## Cài đặt

### Claude Code – cả bộ

```
/plugin marketplace add nguyenvansuai/hanh-chinh-cong
```

```
/plugin install hanh-chinh-cong@hanh-chinh-cong
```

### Claude Code – một skill

```
/plugin install van-ban-dang@hanh-chinh-cong
```

Cập nhật: `/plugin marketplace update hanh-chinh-cong`

### Claude Desktop / Cowork
Cài từ file [`dist/hanh-chinh-cong.plugin`](dist/).

### Claude.ai – từng skill
**Settings → Capabilities**: bật Code execution; **Skills → Upload skill** với file zip trong [`dist/`](dist/) (ví dụ `van-ban-dang.zip`).

### ChatGPT
Hướng dẫn trong [`chatgpt/`](chatgpt/).

## Ví dụ câu lệnh
- "Soạn nghị quyết chi bộ tháng 12/2026 của Chi bộ thôn X, xuất file Word đúng thể thức Đảng."
- "Kiểm tra giúp file quyet-dinh.docx của UBND phường trước khi trình chủ tịch ký."
- "Nhận hồ sơ cấp phép ngày 12/02/2026, thủ tục quy định 5 ngày làm việc. Hẹn trả ngày nào?"
- "Đơn khiếu nại nhận ngày 03/8/2026 về quyết định thu hồi đất của Chủ tịch UBND xã. Thẩm quyền và thời hạn?"
- "Kỳ chốt số liệu báo cáo năm 2026 là từ ngày nào? Lập báo cáo tổng kết theo số liệu đính kèm."
- "Viết bài phát biểu khai mạc hội nghị cán bộ công chức năm 2027, 7 phút."

## Phát triển

```bash
python3 tests/test_cong_cu.py
```

```bash
python3 scripts/build.py
```

## Lưu ý
Cập nhật đến **11/2026**. Nhiều văn bản mới (HD 05-HD/VPTW, Luật 136/2025, nghị định đánh giá cán bộ theo KPI, hướng dẫn Luật Lưu trữ 2024) – các mục gắn **[Cần kiểm tra]** phải đối chiếu toàn văn và hướng dẫn của tỉnh, của cấp ủy cấp trên. **Không dùng plugin với tài liệu mật.**

## Hệ sinh thái
[hanhchinh-nhansu](https://github.com/nguyenvansuai/hanhchinh-nhansu) (HCNS doanh nghiệp) · [phapche-hopdong](https://github.com/nguyenvansuai/phapche-hopdong) · [skill-ketoan-tai-chinh](https://github.com/nguyenvansuai/skill-ketoan-tai-chinh) · [skill-ho-kinh-doanh](https://github.com/nguyenvansuai/skill-ho-kinh-doanh) · [skill-sales-marketing](https://github.com/nguyenvansuai/skill-sales-marketing) · [20skill-van-phong](https://github.com/nguyenvansuai/20skill-van-phong)

## Giấy phép
MIT – xem [LICENSE](LICENSE).

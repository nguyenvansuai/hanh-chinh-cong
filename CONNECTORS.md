# Connectors

## 1. Có sẵn: `hcc-cong-cu` (MCP server cục bộ)

Khai báo trong `.mcp.json`; Claude Code / Claude Desktop tự khởi động. Cần **Python 3.8+**; tạo/đọc .docx cần `pip install python-docx`.

| Nhóm | Công cụ |
|---|---|
| Nghiệp vụ công vụ | `han_giai_quyet_tthc`, `thoi_han_khieu_nai_to_cao`, `ky_bao_cao` |
| Văn thư | `cap_so_van_ban_di` (chính quyền/Đảng), `dang_ky_van_ban_den`, `cap_nhat_van_ban_den`, `tra_cuu_so_van_ban`, `kiem_tra_the_thuc` (nhà nước/Đảng), `tao_van_ban_docx` (nhà nước/Đảng), `doc_so_thanh_chu` |
| Lịch | `ngay_lam_viec`, `cong_ngay_lich`, `ngay_le_tet`, `doi_lich_am_duong`, `tao_file_ics` |

Kiểm tra: `python3 mcp/server.py --tu-kiem-tra`. Windows: đổi `python3` thành `py`/`python` trong `.mcp.json` nếu cần.

## 2. Hệ thống của cơ quan – không tích hợp trực tiếp
| Hệ thống | Cách dùng với plugin |
|---|---|
| Hệ thống quản lý văn bản và điều hành (các tỉnh, bộ) | Không kết nối. Tải văn bản (PDF/Word) về rồi đưa cho Claude; sổ CSV của plugin chỉ để đối chiếu, nhắc việc cá nhân |
| Hệ thống thông tin giải quyết TTHC cấp tỉnh, Cổng Dịch vụ công quốc gia | Không kết nối. Dán nội dung thủ tục đã công bố, thông tin hồ sơ (đã ẩn danh nếu không cần) |
| Chữ ký số chuyên dùng Chính phủ | Không tích hợp – plugin **không ký số** |
| Thư công vụ | Không kết nối; soạn nháp để người dùng tự gửi |

Lý do: hệ thống công vụ thường nằm trong mạng riêng, có yêu cầu an toàn thông tin; plugin chỉ xử lý tài liệu người dùng chủ động đưa vào.

## 3. Bảo mật – bắt buộc đọc
- **Không** đưa tài liệu thuộc danh mục bí mật nhà nước (Mật, Tối mật, Tuyệt mật) vào bất kỳ công cụ AI nào.
- Tuân thủ quy chế của cơ quan về sử dụng AI, dịch vụ đám mây.
- Hồ sơ công dân, đơn thư: ẩn danh khi không cần thông tin định danh; thông tin người tố cáo luôn bảo mật.

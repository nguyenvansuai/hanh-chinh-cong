"""Công cụ nghiệp vụ hành chính công: hạn giải quyết thủ tục hành chính, thời hạn khiếu nại – tố cáo, kỳ chốt số liệu báo cáo."""
from datetime import date, timedelta

from . import lich_vn
from .lich_vn import _ngay


def han_giai_quyet_tthc(ngay_nhan_ho_so, so_ngay_lam_viec, lam_viec_sang_thu_bay=False, ngay_nghi_them=(), ngay_lam_bu=()):
    """Hạn trả kết quả TTHC tính theo ngày làm việc kể từ ngày nhận đủ hồ sơ hợp lệ."""
    kq = lich_vn.cong_cu_ngay_lam_viec(ngay_nhan_ho_so, so_ngay=int(so_ngay_lam_viec), nghi_thu_bay=True,
                                       ngay_nghi_them=list(ngay_nghi_them), ngay_lam_bu=list(ngay_lam_bu))
    kq["can_cu"] = ("Thời hạn giải quyết theo quy định của từng thủ tục hành chính (công bố trên Cổng Dịch vụ công quốc gia), tính "
                    "theo ngày làm việc kể từ ngày nhận đủ hồ sơ hợp lệ. Thực hiện theo Nghị định 118/2025/NĐ-CP (sửa đổi bởi NĐ "
                    "367/2025/NĐ-CP) về cơ chế một cửa, một cửa liên thông [Cần kiểm tra quy định về mốc giờ tiếp nhận].")
    kq["neu_tre_han"] = ("Hồ sơ quá hạn: cơ quan giải quyết gửi văn bản/phiếu xin lỗi và hẹn lại ngày trả kết quả cho tổ chức, cá nhân "
                         "(nêu rõ lý do) – đối chiếu mẫu theo văn bản hiện hành.")
    if lam_viec_sang_thu_bay:
        kq["ghi_chu_thu_bay"] = "Bộ phận một cửa làm việc sáng Thứ Bảy không làm thay đổi cách tính thời hạn theo ngày làm việc trừ khi văn bản quy định."
    return kq


KHIEU_NAI = {
    # (thụ lý, đơn vị thụ lý, giải quyết thường, phức tạp, vùng sâu xa thường, vùng sâu xa phức tạp)
    "lan_dau_truoc_01_7_2026": (10, "ngay", 30, 45, 45, 60, "Luật Khiếu nại 2011 (Điều 27, 28)", "Chắc chắn"),
    "lan_hai_truoc_01_7_2026": (10, "ngay", 45, 60, 60, 70, "Luật Khiếu nại 2011 (Điều 36, 37)", "Chắc chắn"),
    "lan_dau_tu_01_7_2026": (7, "ngay_lam_viec", 30, 45, 45, 60,
                             "Luật số 136/2025/QH15 sửa đổi Luật Tiếp công dân, Khiếu nại, Tố cáo (hiệu lực 01/7/2026); Nghị định 155/2026/NĐ-CP",
                             "Cần kiểm tra – nguồn thứ cấp nêu thụ lý rút còn 7 ngày (làm việc); thời hạn giải quyết chưa đối chiếu bản gốc"),
    "lan_hai_tu_01_7_2026": (7, "ngay_lam_viec", 45, 60, 60, 70, "Luật số 136/2025/QH15; Nghị định 155/2026/NĐ-CP",
                             "Cần kiểm tra"),
}


def thoi_han_khieu_nai_to_cao(loai, ngay_nhan_don, ngay_thu_ly=None, phuc_tap=False, vung_sau_vung_xa=False, so_lan_gia_han=0):
    """loai: khieu_nai_lan_dau | khieu_nai_lan_hai | to_cao. Tự chọn quy định trước/từ 01/7/2026 theo ngày nhận đơn."""
    dn = _ngay(ngay_nhan_don)
    if loai == "to_cao":
        thu_ly_han = lich_vn.cong_cu_ngay_lam_viec(dn.isoformat(), so_ngay=7)["ngay_ket_thuc"]
        d_tl = _ngay(ngay_thu_ly) if ngay_thu_ly else None
        kq = {"loai": "Tố cáo", "han_xem_xet_thu_ly": thu_ly_han,
              "can_cu": "Luật Tố cáo 2018 (sửa đổi bởi Luật 136/2025/QH15 từ 01/7/2026): thụ lý trong 07 ngày làm việc kể từ ngày nhận "
                        "(kiểm tra điều kiện thụ lý); thời hạn giải quyết không quá 30 ngày kể từ ngày thụ lý; vụ việc phức tạp gia hạn "
                        "01 lần không quá 30 ngày; đặc biệt phức tạp gia hạn 02 lần, mỗi lần không quá 30 ngày",
              "nhan": "Chắc chắn với Luật 2018; cần kiểm tra thay đổi từ 01/7/2026"}
        if d_tl:
            kq["han_giai_quyet"] = lich_vn.cong_cu_cong_ngay(d_tl.isoformat(), so_ngay=30 + 30 * min(int(so_lan_gia_han), 2))["ket_qua"]
        return kq
    khoa = ("lan_dau" if loai == "khieu_nai_lan_dau" else "lan_hai") + ("_tu_01_7_2026" if dn >= date(2026, 7, 1) else "_truoc_01_7_2026")
    tl, dv, t1, t2, v1, v2, can_cu, nhan = KHIEU_NAI[khoa]
    if dv == "ngay_lam_viec":
        han_tl = lich_vn.cong_cu_ngay_lam_viec(dn.isoformat(), so_ngay=tl)["ngay_ket_thuc"]
    else:
        han_tl = lich_vn.cong_cu_cong_ngay(dn.isoformat(), so_ngay=tl)["ket_qua"]
    so_ngay_gq = (v2 if phuc_tap else v1) if vung_sau_vung_xa else (t2 if phuc_tap else t1)
    kq = {"loai": "Khiếu nại " + ("lần đầu" if "dau" in khoa else "lần hai"), "quy_dinh_ap_dung": khoa,
          "han_thu_ly": han_tl, "thoi_han_giai_quyet": f"{so_ngay_gq} ngày kể từ ngày thụ lý",
          "can_cu": can_cu, "nhan": nhan,
          "luu_y": "Thời hạn giải quyết khiếu nại ghi 'ngày' (không ghi 'ngày làm việc') – nhiều ý kiến hiểu là ngày theo lịch; đối chiếu "
                   "văn bản hướng dẫn. Thời hiệu khiếu nại: 90 ngày kể từ ngày nhận được/biết quyết định, hành vi hành chính."}
    if ngay_thu_ly:
        kq["han_giai_quyet"] = lich_vn.cong_cu_cong_ngay(_ngay(ngay_thu_ly).isoformat(), so_ngay=so_ngay_gq)["ket_qua"]
    return kq


def ky_bao_cao(loai, nam, ky=None):
    """Thời gian chốt số liệu báo cáo định kỳ theo Điều 12 Nghị định 09/2019/NĐ-CP."""
    nam = int(nam)
    if loai == "thang":
        th = int(ky)
        tu = date(nam - 1, 12, 15) if th == 1 else date(nam, th - 1, 15)
        den = date(nam, th, 14)
    elif loai == "quy":
        q = int(ky)
        th_dau = 3 * (q - 1) + 1
        tu = date(nam - 1, 12, 15) if q == 1 else date(nam, th_dau - 1, 15)
        den = date(nam, th_dau + 2, 14)
    elif loai == "6thang":
        tu, den = date(nam - 1, 12, 15), date(nam, 6, 14)
    elif loai == "nam":
        tu, den = date(nam - 1, 12, 15), date(nam, 12, 14)
    else:
        return {"loi": "loai: thang | quy | 6thang | nam"}
    return {"ky": f"{loai} {ky or ''} {nam}".replace("  ", " "), "chot_so_lieu_tu": lich_vn._fmt(tu), "den": lich_vn._fmt(den),
            "can_cu": "Điều 12 Nghị định 09/2019/NĐ-CP về chế độ báo cáo của cơ quan hành chính nhà nước (vẫn được viện dẫn năm 2026). "
                      "Báo cáo chuyên ngành có thể quy định kỳ khác – kiểm tra văn bản yêu cầu báo cáo.",
            "luu_y": "Hạn gửi báo cáo do văn bản quy định chế độ báo cáo của từng bộ/tỉnh ấn định – không suy ra từ kỳ chốt số liệu."}


TOOLS = [
    {"name": "han_giai_quyet_tthc", "fn": han_giai_quyet_tthc,
     "description": "Tính ngày hẹn trả kết quả thủ tục hành chính theo số ngày làm việc kể từ ngày nhận đủ hồ sơ (bỏ Thứ Bảy, Chủ nhật, lễ Tết, "
                    "nghỉ bù) – dùng cho phiếu hẹn, theo dõi hồ sơ trễ hạn, phiếu xin lỗi và hẹn lại (NĐ 118/2025/NĐ-CP).",
     "schema": {"type": "object", "required": ["ngay_nhan_ho_so", "so_ngay_lam_viec"], "properties": {
         "ngay_nhan_ho_so": {"type": "string"}, "so_ngay_lam_viec": {"type": "integer"},
         "lam_viec_sang_thu_bay": {"type": "boolean"},
         "ngay_nghi_them": {"type": "array", "items": {"type": "string"}},
         "ngay_lam_bu": {"type": "array", "items": {"type": "string"}}}}},
    {"name": "thoi_han_khieu_nai_to_cao", "fn": thoi_han_khieu_nai_to_cao,
     "description": "Tính hạn thụ lý và hạn giải quyết khiếu nại lần đầu/lần hai (vụ việc thường, phức tạp, vùng sâu vùng xa) và tố cáo (có gia "
                    "hạn), tự áp dụng quy định trước hoặc từ 01/7/2026 (Luật 136/2025/QH15) theo ngày nhận đơn, kèm nhãn tin cậy.",
     "schema": {"type": "object", "required": ["loai", "ngay_nhan_don"], "properties": {
         "loai": {"type": "string", "enum": ["khieu_nai_lan_dau", "khieu_nai_lan_hai", "to_cao"]},
         "ngay_nhan_don": {"type": "string"}, "ngay_thu_ly": {"type": "string"},
         "phuc_tap": {"type": "boolean"}, "vung_sau_vung_xa": {"type": "boolean"},
         "so_lan_gia_han": {"type": "integer", "description": "Tố cáo: 0, 1 hoặc 2"}}}},
    {"name": "ky_bao_cao", "fn": ky_bao_cao,
     "description": "Thời gian chốt số liệu của báo cáo định kỳ tháng/quý/6 tháng/năm theo Điều 12 Nghị định 09/2019/NĐ-CP "
                    "(ví dụ báo cáo năm: 15/12 năm trước – 14/12).",
     "schema": {"type": "object", "required": ["loai", "nam"], "properties": {
         "loai": {"type": "string", "enum": ["thang", "quy", "6thang", "nam"]},
         "nam": {"type": "integer"}, "ky": {"type": "integer", "description": "Số tháng (1–12) hoặc số quý (1–4)"}}}},
]

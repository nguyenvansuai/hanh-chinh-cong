#!/usr/bin/env python3
"""Kiểm thử công cụ: python3 tests/test_cong_cu.py (không cần pytest)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import goi, tat_ca  # noqa: E402

LOI = []


def kiem(ten, dk, chi_tiet=""):
    print(("  ok  " if dk else "  LỖI ") + ten + ("" if dk else f" -> {chi_tiet}"))
    if not dk:
        LOI.append(ten)


def test_cong_vu():
    r = goi("han_giai_quyet_tthc", {"ngay_nhan_ho_so": "12/02/2026", "so_ngay_lam_viec": 5})
    kiem("TTHC 5 ngày làm việc qua Tết", r["ngay_ket_thuc"].endswith("26/02/2026"), r["ngay_ket_thuc"])
    r = goi("thoi_han_khieu_nai_to_cao", {"loai": "khieu_nai_lan_dau", "ngay_nhan_don": "02/03/2026", "ngay_thu_ly": "10/03/2026"})
    kiem("KN lần đầu trước 7/2026: thụ lý 10 ngày", r["han_thu_ly"].endswith("12/03/2026") and r["han_giai_quyet"].endswith("09/04/2026"), r)
    r = goi("thoi_han_khieu_nai_to_cao", {"loai": "khieu_nai_lan_dau", "ngay_nhan_don": "03/08/2026"})
    kiem("KN từ 7/2026: thụ lý 7 ngày làm việc, nhãn cần kiểm tra", r["han_thu_ly"].endswith("12/08/2026") and "Cần kiểm tra" in r["nhan"], r)
    r = goi("thoi_han_khieu_nai_to_cao", {"loai": "khieu_nai_lan_hai", "ngay_nhan_don": "02/03/2026", "ngay_thu_ly": "10/03/2026",
                                         "phuc_tap": True, "vung_sau_vung_xa": True})
    kiem("KN lần hai phức tạp vùng sâu 70 ngày", "70 ngày" in r["thoi_han_giai_quyet"], r)
    r = goi("thoi_han_khieu_nai_to_cao", {"loai": "to_cao", "ngay_nhan_don": "02/03/2026", "ngay_thu_ly": "10/03/2026", "so_lan_gia_han": 1})
    kiem("Tố cáo gia hạn 1 lần = 60 ngày", r["han_giai_quyet"].endswith("09/05/2026"), r)
    r = goi("ky_bao_cao", {"loai": "nam", "nam": 2026})
    kiem("Kỳ báo cáo năm 15/12/2025–14/12/2026", r["chot_so_lieu_tu"].endswith("15/12/2025") and r["den"].endswith("14/12/2026"), r)
    r = goi("ky_bao_cao", {"loai": "quy", "nam": 2026, "ky": 2})
    kiem("Quý II: 15/3–14/6", r["chot_so_lieu_tu"].endswith("15/03/2026") and r["den"].endswith("14/06/2026"), r)
    r = goi("ky_bao_cao", {"loai": "thang", "nam": 2026, "ky": 1})
    kiem("Tháng 1: 15/12/2025–14/01/2026", r["chot_so_lieu_tu"].endswith("15/12/2025"), r)


def test_van_thu():
    d = tempfile.mkdtemp()
    r = goi("cap_so_van_ban_di", {"loai_van_ban": "Quyết định", "viet_tat_co_quan": "UBND", "trich_yeu": "x", "ngay_van_ban": "05/03/2026", "thu_muc": d})
    kiem("Số QĐ UBND", r["da_cap_so"] == "Số: 01/QĐ-UBND", r)
    r = goi("cap_so_van_ban_di", {"loai_van_ban": "Nghị quyết", "viet_tat_co_quan": "ĐU", "trich_yeu": "x", "ngay_van_ban": "05/03/2026",
                                  "thu_muc": d, "kieu": "dang"})
    kiem("Số Đảng 01-NQ/ĐU", r["da_cap_so"] == "Số 01-NQ/ĐU", r)
    r = goi("cap_so_van_ban_di", {"loai_van_ban": "Công văn", "viet_tat_co_quan": "ĐU", "trich_yeu": "x", "ngay_van_ban": "06/03/2026",
                                  "thu_muc": d, "kieu": "dang"})
    kiem("Sổ Đảng riêng, CV số 02", r["da_cap_so"] == "Số 02-CV/ĐU", r)


def test_the_thuc_dang():
    try:
        import docx  # noqa: F401
    except ImportError:
        print("  bỏ qua (chưa cài python-docx)")
        return
    d = tempfile.mkdtemp()
    f = os.path.join(d, "nq.docx")
    goi("tao_van_ban_docx", {"duong_dan_ra": f, "loai_the_thuc": "dang", "co_quan_chu_quan": "Đảng bộ tỉnh X",
                             "co_quan_ban_hanh": "Đảng ủy xã Y", "ten_loai": "NGHỊ QUYẾT", "trich_yeu": "về nhiệm vụ năm 2027",
                             "so_ky_hieu": "Số 05-NQ/ĐU", "dia_danh": "Y", "ngay": "ngày 05 tháng 01 năm 2027",
                             "noi_dung": ["# I. ĐÁNH GIÁ", "Nội dung..."], "quyen_han_ky": "T/M ĐẢNG ỦY", "chuc_vu_ky": "Bí thư",
                             "nguoi_ky": "Nguyễn Văn A", "noi_nhan": ["- Ban Thường vụ Tỉnh ủy,", "- Lưu Văn phòng Đảng ủy."]})
    r = goi("kiem_tra_the_thuc", {"duong_dan": f, "loai_the_thuc": "dang"})
    kiem("Văn bản Đảng tạo ra không có lỗi CHẶN", not any(x["muc"] == "CHẶN" for x in r["danh_sach_loi"]), r["danh_sach_loi"])
    r = goi("kiem_tra_the_thuc", {"van_ban": "ĐẢNG ỦY XÃ Y\nSố: 05/NQ-ĐU\nTM. ĐẢNG ỦY", "loai_the_thuc": "dang"})
    vd = " | ".join(x["van_de"] for x in r["danh_sach_loi"])
    kiem("Bắt lỗi thiếu tiêu đề Đảng", "ĐẢNG CỘNG SẢN" in vd, vd)
    kiem("Bắt lỗi TM. trong văn bản Đảng", "T/M" in vd, vd)


if __name__ == "__main__":
    print(f"{len(tat_ca())} công cụ")
    for f in [test_cong_vu, test_van_thu, test_the_thuc_dang]:
        print(f.__name__)
        f()
    print("KẾT QUẢ:", "TẤT CẢ ĐẠT" if not LOI else f"{len(LOI)} LỖI")
    sys.exit(1 if LOI else 0)

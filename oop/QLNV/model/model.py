import random


class CongTy:
    def __init__(self, *arg, **kwargs):
        self.maCty = kwargs.get('maCty', '')
        self.tenCty = kwargs.get('tenCty', '')
        self.dsVanPhong = []
        self.dsBanHang = []

    def xuat_tat_ca_nhan_vien(self):
        print("Nhân viên văn phòng:")
        for nv in self.dsVanPhong:
            nv.xuat_VanPhong()
        print("Nhân viên kinh doanh:")
        for nv in self.dsBanHang:
            nv.xuat_BanHang()

    def tim_nv_by_maNV(self, maNV):

        for nv in self.dsBanHang + self.dsVanPhong:
            if nv.maNV == maNV:
                return nv

        return None

    def nv_bh_luong_thap_nhat(self):
        if not self.dsBanHang:
            return None
        return min(self.dsBanHang, key=lambda nv: nv.luongHT)

    def nv_co_luong_cao_nhat(self):
        if not self.dsVanPhong and not self.dsBanHang:
            return None

        all_nv = self.dsVanPhong + self.dsBanHang
        return max(all_nv, key=lambda nv: nv.luongHT)

    def tinh_luong_hang_thang(self):
        for nv in self.dsBanHang + self.dsVanPhong:
            nv.tinh_luong_hang_thang()

    def them_nhieu_nv_van_phong(self, ds_nv):
        self.dsVanPhong.extend(ds_nv)

    def them_nhieu_nv_kinh_doanh(self, ds_nv):
        self.dsBanHang.extend(ds_nv)


class vnVanPhong:
    def __init__(self, *arg, **kwargs):
        self.maNV = kwargs.get('maNV', '')
        self.hoTen = kwargs.get('hoTen', '')
        self.luonngCB = kwargs.get('luonngCB', 0)
        self.soNG = kwargs.get('soNG', 0)
        self.luongHT = 0

    def tinh_luong_hang_thang(self):
        self.luongHT = self.luonngCB + (self.soNG * 150_000)

    def xuat_VanPhong(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self.maNV)
        print("Họ tên nhân viên:", self.hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luonngCB))
        print("Số ngày làm việc:", self.soNG)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luongHT))


class nvBanHang:
    def __init__(self, *arg, **kwargs):
        self.maNV = kwargs.get('maNV', '')
        self.hoTen = kwargs.get('hoTen', '')
        self.luonngCB = kwargs.get('luonngCB', 0)
        self.soSP = kwargs.get('soSP', 0)
        self.luongHT = 0

    def tinh_luong_hang_thang(self):
        self.luongHT = self.luonngCB + (self.soSP * 18_000)

    def xuat_BanHang(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self.maNV)
        print("Họ tên nhân viên:", self.hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luonngCB))
        print("Số ngày làm việc:", self.soSP)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self.luongHT))


cty = CongTy(maCty='CT1', tenCty='Cong Ty 1')
# kd1 = nvBanHang(maNV='KD1', hoTen='Bán hàng 1', luonngCB=2000, soSP=245)
# kd2 = nvBanHang(maNV='KD2', hoTen='Bán hàng 2', luonngCB=1500, soSP=340)
# kd3 = nvBanHang(maNV='KD3', hoTen='Bán hàng 3', luonngCB=1500, soSP=200)
#
# vp1 = vnVanPhong(maNV='VP1', hoTen='Văn Phòng 1', luonngCB=2000, soSP=30)
# vp2 = vnVanPhong(maNV='VP2', hoTen='Văn Phòng 2', luonngCB=1400, soSP=290)
# vp3 = vnVanPhong(maNV='VP3', hoTen='Văn Phòng 3', luonngCB=1500, soSP=39)
#
# kd1.tinh_luong_hang_thang()
# kd2.tinh_luong_hang_thang()
# kd3.tinh_luong_hang_thang()
#
# vp1.tinh_luong_hang_thang()
# vp2.tinh_luong_hang_thang()
# vp3.tinh_luong_hang_thang()
#
# cty.dsBanHang.append(kd1)
# cty.dsBanHang.append(kd2)
# cty.dsBanHang.append(kd3)
#
# cty.dsVanPhong.append(vp1)
# cty.dsVanPhong.append(vp2)
# cty.dsVanPhong.append(vp3)


ds_vp = [vnVanPhong(maNV=f'VP{i}', hoTen=f'Van Phong {i}', luonngCB=random.randint(10_000_000, 50_000_000),
                    soNG=random.randint(20, 30)) for i in range(1, 6)]
ds_kd = [nvBanHang(maNV=f'BH{i}', hoTen=f'Ban Hang {i}', luonngCB=random.randint(20_000_000, 45_000_000),
                   soSP=random.randint(100, 500)) for i in range(1, 6)]

# for nv in ds_vp:
#     nv.tinh_luong_hang_thang()
#
# for nv in ds_kd:
#     nv.tinh_luong_hang_thang()


cty.them_nhieu_nv_van_phong(ds_vp)
cty.them_nhieu_nv_kinh_doanh(ds_kd)

cty.tinh_luong_hang_thang()

cty.xuat_tat_ca_nhan_vien()

nv_co_luong_cao_nhat = cty.nv_co_luong_cao_nhat()
if nv_co_luong_cao_nhat is not None:
    print('Nhân viên có lương cao nhất:', nv_co_luong_cao_nhat.hoTen)
else:
    print('Không có nhân viên')

nv_bh_co_luong_thap_nhat = cty.nv_bh_luong_thap_nhat()
if nv_bh_co_luong_thap_nhat is not None:
    print('Nhân viên kinh doanh có lương thấp nhất:', nv_bh_co_luong_thap_nhat.hoTen)
else:
    print('Không có nhân viên bán hàng')

nv_tim = cty.tim_nv_by_maNV('VP1')

if nv_tim is not None:
    print('Nhân viên tìm được là:',nv_tim.maNV)
else:
    print('Không có nhân viên cần tìm')
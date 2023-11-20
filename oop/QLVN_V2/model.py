import random
from abc import ABC, abstractmethod

class CongTy:
    soNV = 0
    def __init__(self, maCty: int, **kwargs):
        self.__maCty = maCty
        self.__tenCty = kwargs.get('tenCty', '')
        self.__dsNV = []

        CongTy.soNV += 1

    def tim_nv_by_maNV(self, maNV: int):

        for nv in self.__dsNV:
            if nv._maNV == maNV:
                return nv

        return None

    def nv_banhang_luong_thap_nhat(self):
        ds_luong = [(nv._luongHT, nv) for nv in self.__dsNV if isinstance(nv, BanHang)]

        if not ds_luong:
            return None

        luong_thap_nhat, nhan_vien = min(ds_luong, key=lambda x: x[0])
        return nhan_vien

    def nv_co_luong_cao_nhat(self):
        if not self.__dsNV:
            return None

        return max(self.__dsNV, key=lambda nv: nv._luongHT)

    def tinh_luong_hang_thang(self):
        for nv in self.__dsNV:
            nv.tinh_luong_hang_thang()

    def them_nhieu_nv(self, ds_nv):
        self.__dsNV.extend(ds_nv)

    def xuat_tat_ca_nhan_vien(self):
        for nv in self.__dsNV:
            print(nv)

    def xuat_nv_BanHang(self):
        for nv in self.__dsNV:
            # if type(nv) is BanHang:
            if isinstance(nv, BanHang):
                print(nv)

    @staticmethod
    def tienThuong(tien):
        return tien * 1.2

class abcNhanVien(ABC):
    @abstractmethod
    def xuat(self):
        pass
    @abstractmethod
    def tinh_luong_hang_thang(self):
        pass

class NhanVien(abcNhanVien):
    def __init__(self, maNV: int, **kwargs):
        self._maNV = maNV
        self._hoTen = kwargs.get('hoTen', '')
        self._luonngCB = kwargs.get('luonngCB', 0)
        self._luongHT = kwargs.get('luongHT', 0)


    def __str__(self):
        return str((self._maNV, self._hoTen, self._luonngCB, self._luongHT))

    def xuat(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self._maNV)
        print("Họ tên nhân viên:", self._hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luonngCB))
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luongHT))

    def tinhLuong(self):
        pass
class BanHang(NhanVien):
    soNV = 0

    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soSP = kwargs.get('soSP', 0)
        BanHang.soNV += 1
    @property
    def soSP(self):
        return self.__soSP
    @soSP.setter
    def soSP(self,valueNew):
        self.__soSP= valueNew

    def tinh_luong_hang_thang(self):
        self._luongHT = self._luonngCB + (self.__soSP * 18_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soSP)

    def __str__(self):
        return str((self._maNV, self._hoTen, self.__soSP, self._luonngCB, self._luongHT))

    @classmethod
    def soLuong(cls):
        print('Số lượng', BanHang.soNV)
class VanPhong(NhanVien):
    soNV = 0

    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soNG = kwargs.get('soNG', 0)
        VanPhong.soNV += 1

    @property
    def soNG(self):
        return self.__soNG
    @soNG.setter
    def soNG(self,valueNew):
        self.__soNG = valueNew

    def tinh_luong_hang_thang(self):
        self._luongHT = self._luonngCB + (self.__soNG * 150_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soNG)
    @classmethod
    def soLuong(cls):
        print('Số lượng', VanPhong.soNV)
    def __str__(self):
        return str((self._maNV, self._hoTen, self.__soNG, self._luonngCB, self._luongHT))


class NhanVienQL(VanPhong):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__heSoTN = kwargs.get('heSTN', 0)

    def __str__(self):
        return str((self._maNV, self._hoTen, self.soNG, self._luonngCB, self._luongHT, self.__heSoTN))


    def xuat(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self._maNV)
        print("Họ tên nhân viên:", self._hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luonngCB))
        print("Lương hằng tháng : {:,.0f} VNĐ".format(self._luongHT))

    def tinh_luong_hang_thang(self):
        if self.__heSoTN > 3.5:
            self._luongHT = ((self.__heSoTN * 250_000 * self.soNG) + self._luonngCB) * 1.2
        else:
            self._luongHT = (self.__heSoTN * 250_000 * self.soNG) + self._luonngCB

    def xuat(self):
        super().xuat()
        print("Hệ số trắc nghiệm:", self.__heSoTN)


if __name__ == '__main__':

    cty = CongTy(maCty='CT1', tenCty='Cong Ty 1')
    ds_vp = [VanPhong(maNV=i * 100, hoTen=f'Van Phong {i}', luonngCB=random.randint(10_000_000, 50_000_000),
                      soNG=random.randint(20, 30)) for i in range(1, 6)]

    ds_kd = [BanHang(maNV=i * 1000, hoTen=f'Ban Hang {i}', luonngCB=random.randint(20_000_000, 45_000_000),
                     soSP=random.randint(100, 500)) for i in range(1, 6)]

    ds_ql = [NhanVienQL(maNV=i * 300, hoTen=f'Quan ly{i}', luonngCB=random.randint(40_000_000, 100_000_000),
                     soNG=random.randint(100, 500), heSTN=random.randint(1, 3)) for i in range(1, 3)]

    cty.them_nhieu_nv(ds_vp)
    cty.them_nhieu_nv(ds_kd)
    cty.them_nhieu_nv(ds_ql)

    cty.tinh_luong_hang_thang()
    cty.xuat_tat_ca_nhan_vien()
    nv_co_luong_cao_nhat = cty.nv_co_luong_cao_nhat()

    if nv_co_luong_cao_nhat is not None:
        print('Nhân viên có lương cao nhất:', nv_co_luong_cao_nhat._hoTen)
    else:
        print('Không có nhân viên')

    nv_bh_co_luong_thap_nhat = cty.nv_banhang_luong_thap_nhat()
    if nv_bh_co_luong_thap_nhat is not None:
        print('Nhân viên kinh doanh có lương thấp nhất:', nv_bh_co_luong_thap_nhat._hoTen)
    else:
        print('Không có nhân viên bán hàng')

    nv_tim = cty.tim_nv_by_maNV(123)

    if nv_tim is not None:
        print('Nhân viên tìm được là:', nv_tim.maNV)
    else:
        print('Không có nhân viên cần tìm')

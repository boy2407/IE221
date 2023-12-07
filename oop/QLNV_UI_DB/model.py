import random
from abc import ABC, abstractmethod
from DataBase import DataBase


class CongTy:
    soNV = 0

    def __init__(self, maCty: int, **kwargs):
        self.__maCty = maCty
        self.__tenCty = kwargs.get('tenCty', '')
        self.__dsNV = []
        CongTy.soNV += 1

    """return dsNV"""

    @property
    def dsNV(self):
        self.loadDatabase()
        return self.__dsNV

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

        db = DataBase()
        db.save_monthly_salary(self.__dsNV)

    def them_nv(self, nv):
        db = DataBase()
        db.add_employee(nv)
        self.__dsNV.append(nv)

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

    """thao tác với db """

    def load_loaiNV(self):
        db = DataBase()
        loai_nhan_vien = db.employee_Type()
        return loai_nhan_vien

    def loadDatabase(self):
        self.__dsNV=[]
        # Sử dụng lớp Database
        db = DataBase()
        nhanvien = db.list_of_Employee()
        for nv in nhanvien:

            if nv[1] == 'Bán Hàng':
                temp = BanHang(maNV=nv[0], loaiNV=nv[1], hoTen=nv[2], luonngCB=float(nv[3]), soSP=nv[5],
                               luongHT=float(nv[6]))

                self.__dsNV.append(temp)

            elif nv[1] == 'Văn Phòng':

                temp = VanPhong(maNV=nv[0], loaiNV=nv[1], hoTen=nv[2], luonngCB=float(nv[3]), soNG=nv[4],
                                luongHT=float(nv[6]))

                self.__dsNV.append(temp)
            else:
                temp = NhanVien(maNV=nv[0], loaiNV=nv[1], hoTen=nv[2], luonngCB=float(nv[3]), luongHT=float(nv[6]))
                self.__dsNV.append(temp)


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
        self._luongCB = kwargs.get('luonngCB', 0)
        self._luongHT = kwargs.get('luongHT', 0)
        self._loaiNV = kwargs.get('loaiNV', 'Không Loại')

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luongCB, self._luongHT, self._loaiNV))

    def xuat(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self._maNV)
        print("Họ tên nhân viên:", self._hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luongCB))
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luongHT))

    def tinh_luong_hang_thang(self):
        pass

    def row(self, i):
        return (i, self._maNV, self._hoTen, self._luongCB, self._luongHT)


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
    def soSP(self, valueNew):
        self.__soSP = valueNew

    def tinh_luong_hang_thang(self):
        self._luongHT = self._luongCB + (self.__soSP * 18_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soSP)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luongCB, self._luongHT, self.__soSP,))

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
    def soNG(self, valueNew):
        self.__soNG = valueNew

    def tinh_luong_hang_thang(self):
        self._luongHT = self._luongCB + (self.__soNG * 150_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soNG)

    @classmethod
    def soLuong(cls):
        print('Số lượng', VanPhong.soNV)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luongCB, self._luongHT, self.__soNG,))


class NhanVienQL(VanPhong):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__heSoTN = kwargs.get('heSTN', 0)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luongCB, self._luongHT, self.__heSoTN, self.soNG,))

    def xuat(self):
        print("\n")
        print("Mã nhân viên Văn Phòng:", self._maNV)
        print("Họ tên nhân viên:", self._hoTen)
        print("Lương cơ bản: {:,.0f} VNĐ".format(self._luongCB))
        print("Lương hằng tháng : {:,.0f} VNĐ".format(self._luongHT))

    def tinh_luong_hang_thang(self):
        if self.__heSoTN > 3.5:
            self._luongHT = ((self.__heSoTN * 250_000 * self.soNG) + self._luongCB) * 1.2
        else:
            self._luongHT = (self.__heSoTN * 250_000 * self.soNG) + self._luongCB

    def xuat(self):
        super().xuat()
        print("Hệ số trắc nghiệm:", self.__heSoTN)

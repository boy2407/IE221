from abc import ABC, abstractmethod
class NhanVienABC(ABC):

    @abstractmethod
    def xuat(self):
        pass

    @abstractmethod
    def tinh_luong_ht(self):
        pass


class NhanVien(NhanVienABC):
    def __init__(self, maNV: int, **kwargs):
        self._maNV = maNV
        self._hoTen = kwargs.get('hoTen', '')
        self._luongCB = kwargs.get('luongCB', 0)
        self._luongHT = kwargs.get('luongHT', 0)

    def xuat(self):
        print(self._maNV, self._hoTen, self._luongCB, self._luongHT)

    def tinh_luong_ht(self):
        pass


class QuanLy(NhanVien):

    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__heSoChucVu = kwargs.get('heSoChucVu', 0)
        self.__thuong = kwargs.get('thuong', 0)

    def xuat(self):
        print(self._maNV, self._hoTen, self._luongCB, self.__heSoChucVu,self.__thuong,self._luongHT)


    def tinh_luong_ht(self):
        self._luongHT = self._luongCB * self.__heSoChucVu + self.__thuong


class VanPhong(NhanVien):

    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soGioLam = kwargs.get('soGioLam', 0)

    def xuat(self):
        print(self._maNV, self._hoTen, self._luongCB,self.__soGioLam, self._luongHT )

    def tinh_luong_ht(self):
        if self.__soGioLam > 100:
            self._luongHT = self._luongCB + self.__soGioLam * 220_000 + 5_000_000
        else:
            self._luongHT = self._luongCB + self.__soGioLam * 220_000


class SanXuat(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__soSanPham = kwargs.get('soSanPham', 0)

    def xuat(self):
        print(self._maNV, self._hoTen, self._luongCB, self.__soSanPham,self._luongHT)

    def tinh_luong_ht(self):
        if self.__soSanPham > 150:
            self._luongHT = (self._luongCB + self.__soSanPham * 175_000) * 1.2
        else:
            self._luongHT = (self._luongCB + self.__soSanPham * 175_000)


class DaiLy:
    def __init__(self, maDL: int, **kwargs):
        self.__maDL = maDL
        self.__tenDl = kwargs.get('tenDl', '')
        self.__dsNV = []

    """  câu 1 """

    def loadNV(self):
        self.__dsNV.append(VanPhong(maNV=101, hoTen="Nguyen van A", luongCB=4_500_000, soGioLam=200))
        self.__dsNV.append(VanPhong(maNV=102, hoTen="Nguyen van B", luongCB=5_600_000, soGioLam=100))
        self.__dsNV.append(VanPhong(maNV=103, hoTen="Nguyen van C", luongCB=8_900_000, soGioLam=90))

        self.__dsNV.append(SanXuat(maNV=201, hoTen="Nguyen D", luongCB=7_800_000, soSanPham=250))
        self.__dsNV.append(SanXuat(maNV=202, hoTen="Nguyen E", luongCB=4_500_000, soSanPham=110))
        self.__dsNV.append(SanXuat(maNV=203, hoTen="Nguyen F", luongCB=6_600_000, soSanPham=360))

        self.__dsNV.append(QuanLy(maNV=301, hoTen="Nguyễn G", luongCB=8_500_000, heSoChucVu=1.3, thuong=19_500_000))
        self.__dsNV.append(QuanLy(maNV=302, hoTen="Nguyễn H", luongCB=7_600_000, heSoChucVu=1.2, thuong=18_600_000))

    """  câu 2 """
    def xuat(self):
        for nv in self.__dsNV:
            nv.xuat()

    """ cau 3"""
    def tinh_luong_ht(self):
        for nv in self.__dsNV:
            nv.tinh_luong_ht()

    """ cau 4"""
    def tim_nhanvien_theo_maNV(self, maNV: int):
        for nv in self.__dsNV:
            if nv._maNV == maNV:
                return nv

    """ cau 5"""
    def tinhLuongTB(self):
        return sum([nv._luongHT for nv in self.__dsNV]) / len(self.__dsNV) if self.__dsNV else 0

    """ cau 6"""
    def capnhat_luongcb_theo_maNV(self, maNV: int, luongCB: int):
        for nv in self.__dsNV:
            if nv._maNV == maNV:
                nv._luongCB = luongCB
                nv.tinh_luong_ht()
                return nv

    """ cau 7"""
    def nvLuong_caoNhat(self):
        if not self.__dsNV:
            return None
        return max(self.__dsNV, key=lambda nv: nv._luongHT)

    """ cau 8"""
    def nvLuongCB_thapNhat(self):
        if not self.__dsNV:
            return None
        return min(self.__dsNV, key=lambda nv: nv._luongCB)

if __name__ == '__main__':
    print('--------------------câu 1 và 2---------------------')
    dl = DaiLy(maDL=1, tenDl='Dai Ly ABC')
    dl.loadNV()
    dl.xuat()


    print('---------------cau 3--------------')
    dl.tinh_luong_ht()
    dl.xuat()

    print('---------------cau 4--------------')
    nv = dl.tim_nhanvien_theo_maNV(maNV=101)
    if nv != None:
         nv.xuat()
    else:
        print('không tìm thấy nhân viên')

    print('---------------cau 5--------------')
    print(dl.tinhLuongTB())

    print('---------------cau 6--------------')
    nv  =  dl.capnhat_luongcb_theo_maNV(maNV=101,luongCB=10_000_000)
    nv.xuat()

    print('---------------cau 7--------------')
    nv = dl.nvLuong_caoNhat()
    if nv != None:
        nv.xuat()
    else:
        print('danh sách không có nhân viên')

    print('---------------cau 8--------------')
    nv = dl.nvLuongCB_thapNhat()
    if nv != None:
        nv.xuat()
    else:
        print('danh sách không có nhân viên')


from abc import abstractclassmethod, ABC


class NhanVienAbs(ABC):

    @abstractclassmethod
    def tinhluong(self):
        pass


class NhanVien(NhanVienAbs):
    def __init__(self, maNV: int, **kwargs):
        self._maNV = maNV
        self._hoTen = kwargs.get("hoTen")
        self._luongCB = kwargs.get("luongCB", 0)
        self._luongHT = kwargs.get("luongHT", 0)

    def xuat(self):
        print("Ma NV :", self._maNV)
        print("ho ten : ", self._hoTen)
        print("luong cb ", self._luongCB)
        print("luong ht: ", self._luongHT)


class NVVanPhong(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        NhanVien.__init__(self, maNV, **kwargs)
        self.__soGL = kwargs.get("soGL")

    def tinhluong(self):
        if (self.__soGL > 100):
            self._luongHT = self._luongCB + (self.__soGL * 220000) + 5000000
        else:
            self._luongHT = self._luongCB + (self.__soGL * 220000)

    def xuat(self):
        super().xuat()
        print("so gio lam :", self.__soGL)


class NVSX(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        NhanVien.__init__(self, maNV, **kwargs)
        self.__soSP = kwargs.get("soSP")

    def tinhluong(self):
        if (self.__soSP > 150):
            self._luongHT = (self._luongCB + (self.__soSP * 175_000)) * 1.2
        else:
            self._luongHT = (self._luongCB + (self.__soSP * 175_000))

    def xuat(self):
        super().xuat()
        print("so sp :", self.__soSP)


class NVQL(NhanVien):
    def __init__(self, maNV: int, **kwargs):
        NhanVien.__init__(self, maNV, **kwargs)
        self.__hSCV = kwargs.get("hSCV")
        self.__thuong = kwargs.get("thuong")

    def tinhluong(self):
        self._luongHT = (self._luongCB * self.__hSCV) + self.__thuong

    def xuat(self):
        super().xuat()
        print("so thuong  :", self.__thuong)
        print("he so chuc vu :", self.__hSCV)


class Daily:
    def __init__(self, **kwargs):
        self.__maDL = kwargs.get("maDL")
        self.__tenDL = kwargs.get("tenDL")
        self.__dsNV = []

    def loadNV(self):
        # Nhanvien VP
        self.__dsNV.append(NVVanPhong(maNV=101, hoTen="Nguyen van a", luongCB=4_500_000, soGL=200))
        self.__dsNV.append(NVVanPhong(maNV=102, hoTen="Nguyen van b", luongCB=5600000, soGL=100))
        self.__dsNV.append(NVVanPhong(maNV=103, hoTen="Nguyen van c", luongCB=8900000, soGL=90))

        # NHAN VIEN Sx
        self.__dsNV.append(NVSX(maNV=201, hoTen="Nguyen van d", luongCB=7_800_000, soSP=250))
        self.__dsNV.append(NVSX(maNV=202, hoTen="Nguyen van e", luongCB=4_500_000, soSP=110))
        self.__dsNV.append(NVSX(maNV=203, hoTen="Nguyen van f", luongCB=6_600_000, soSP=360))

        # # Quan ly
        self.__dsNV.append(NVQL(maNV=301, hoTen="Nguyen van g", luongCB=8_500_000, hSCV=1.3, thuong=19500000))
        self.__dsNV.append(NVQL(maNV=302, hoTen="Nguyen van h", luongCB=7_600_000, hSCV=1.2, thuong=18600000))

    def tinhluong(self):
        for nv in self.__dsNV:
            nv.tinhluong()

    def xuat(self):
        for nv in self.__dsNV:
            nv.xuat()

    def tim(self, maNV: int):
        for nv in self.__dsNV:
            if (nv._maNV == maNV):
                return nv

    def luongtb(self):
        return sum([x._luongHT for x in self.__dsNV]) / len(self.__dsNV)

    def capnhat(self, maNV: int, luongCB: int):
        for nv in self.__dsNV:
            if (nv._maNV == maNV):
                nv._luongCB = luongCB
                return nv

    def luongCaoNhat(self):
        max_luong = max(self.__dsNV, key=lambda nv: nv._luongHT)
        return max_luong

    def luongThatNhat(self):
        min_luong = min(self.__dsNV, key=lambda nv: nv._luongCB)
        return min_luong


if __name__ == "__main__":
    # cau 1 khoi tao du lieu
    dl = Daily(maDL="HEH", tenDL="hehe")
    dl.loadNV()

    # #cau 2 xuat nhan vien
    # dl = Daily(maDL="HEH",tenDL ="hehe")
    # dl.loadNV()
    # dl.xuat()

    # cau 3 tinh luong
    # dl = Daily(maDL="HEH", tenDL="hehe")
    # dl.loadNV()
    # dl.tinhluong()
    # dl.xuat()

    # cau 4 tim nv
    # dl = Daily(maDL="HEH",tenDL ="hehe")
    dl.loadNV()
    # nv = dl.tim(101)
    # if nv != None:
    #     nv.xuat()
    # else:
    #     print ("huu k co nv")
    # cau 5 luong tb
    # dl.tinhluong()
    # tb =dl.luongtb()
    # print(tb)
    # cau 6
    # nv  =   dl.capnhat(101,100)
    # nv.xuat()
    # cau 7
    dl.tinhluong()
    nvmax =dl.luongCaoNhat()
    nvmax.xuat()
    # # cau 8
    dl.tinhluong()
    nvmin =dl.luongThatNhat()
    nvmin.xuat()

# 124992000000000.0

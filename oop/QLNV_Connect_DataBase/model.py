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

    """Database"""

    def luu_luong_hang_thang(self):
        db = DataBase(driver='SQL Server', server='DESKTOP-IHQL3VH', database='qlnv', username='sa', password='12345')
        db.connect()

        query = """
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'LuongHangThang')
        BEGIN
            CREATE TABLE LuongHangThang (
                MaNhanVien VARCHAR(255) PRIMARY KEY,
                LuongHT DECIMAL(10, 2),
                FOREIGN KEY (MaNhanVien) REFERENCES NhanVien(MaNhanVien)
            );
        END
        """
        db.execute_query(query)

        # Duyệt qua danh sách nhân viên
        for nv in self.__dsNV:
            luongHT = nv._luongHT

            # Kiểm tra xem MaNhanVien đã tồn tại trong bảng LuongHangThang chưa
            query = f"""IF EXISTS (SELECT 1 FROM LuongHangThang WHERE MaNhanVien = '{nv._maNV}')
                        BEGIN
                            -- Nếu MaNhanVien đã tồn tại trong bảng, cập nhật LuongHT
                            UPDATE LuongHangThang SET LuongHT = {luongHT} WHERE MaNhanVien = '{nv._maNV}';
                        END
                        ELSE
                        BEGIN
                            -- Nếu MaNhanVien chưa tồn tại trong bảng, thêm bản ghi mới
                            INSERT INTO LuongHangThang (MaNhanVien, LuongHT) VALUES ('{nv._maNV}', {luongHT});
                        END"""
            db.execute_query(query)

        # Đảm bảo thay đổi được lưu vào cơ sở dữ liệu
        db.conn.commit()

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

    def loadDatabase(self):
        # Sử dụng lớp Database
        db = DataBase(driver='SQL Server', server='DESKTOP-IHQL3VH', database='qlnv', username='sa', password='12345')
        db.connect()

        # Truy vấn dữ liệu từ bảng NhanVien
        query = """select * from NhanVien;"""
        db.execute_query(query)
        records_nhanvien = db.fetch_all()

        # Truy vấn dữ liệu từ bảng ChamCongTongHop
        query = """select * from ChamCongTongHop;"""
        db.execute_query(query)
        records_chamcong = db.fetch_all()

        # Tạo đối tượng BanHang hoặc VanPhong hoặc NhanVienQL cho mỗi bản ghi và thêm vào danh sách
        for record in records_nhanvien:

            for record_chamcong in records_chamcong:

                if record[0] == record_chamcong[0]:  # So sánh MaNhanVien

                    if record_chamcong[1] == 'Bán Hàng':
                        nv = BanHang(maNV=record[0], hoTen=record[1], luonngCB=float(record[2]),
                                     SoNG=record_chamcong[2], soSP=record_chamcong[3])

                    elif record_chamcong[1] == 'Văn Phòng':
                        nv = VanPhong(maNV=record[0], hoTen=record[1], luonngCB=float(record[2]),
                                      soNG=record_chamcong[2])

                    else:  # Giả sử tất cả nhân viên khác là NhanVienQL
                        nv = NhanVienQL(maNV=record[0], hoTen=record[1], luonngCB=float(record[2]), heSTN=0,
                                        soNG=record_chamcong[2])

                    self.__dsNV.append(nv)


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

    def tinh_luong_hang_thang(self):
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
    def soSP(self, valueNew):
        self.__soSP = valueNew

    def tinh_luong_hang_thang(self):
        self._luongHT = self._luonngCB + (self.__soSP * 18_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soSP)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luonngCB, self._luongHT, self.__soSP,))

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
        self._luongHT = self._luonngCB + (self.__soNG * 150_000)

    def xuat(self):
        super().xuat()
        print("Số ngày làm việc:", self.__soNG)

    @classmethod
    def soLuong(cls):
        print('Số lượng', VanPhong.soNV)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luonngCB, self._luongHT, self.__soNG,))


class NhanVienQL(VanPhong):
    def __init__(self, maNV: int, **kwargs):
        super().__init__(maNV, **kwargs)
        self.__heSoTN = kwargs.get('heSTN', 0)

    def __str__(self):
        return str((self._maNV, self._hoTen, self._luonngCB, self._luongHT, self.__heSoTN, self.soNG,))

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
    cty.loadDatabase()
    cty.tinh_luong_hang_thang()
    cty.xuat_tat_ca_nhan_vien()
    cty.luu_luong_hang_thang()

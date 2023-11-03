#!/usr/bin/python
#-*- coding: utf-8 -*-

class SinhVien:
    """định nghĩa sinh viên"""

    def __init__(self,*arg,**kagr):
        self.MaSV = kagr.get('MaSV')
        self.HoTen = kagr.get('HoTen')
        self.DiemTB = kagr.get('DiemTB')
        self.DiemRL = kagr.get('DiemRL')

    def XetThi(self, ):
        pass

    def XetHB(self, ):
        pass

    def XetTB(self, ):
        pass

    def InThongTin(self, ):
        """đây là phương thức in thông tin"""
        print('\n')
        print("\t+Mã Sinh Viên:", self.MaSV)
        print("\t+Họ Tên:", self.HoTen)
        print("\t+Điểm Trung Bình:", self.DiemTB)
        print("\t+Tình Trạng:", self.DiemRL)


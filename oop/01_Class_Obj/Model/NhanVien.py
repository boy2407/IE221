#!/usr/bin/python
#-*- coding: utf-8 -*-

class NhanVien:
    """định nghĩa sinh viên"""
    def __init__(self,maNV,hoTen,luonngCB,):
        self.maNV = maNV
        self.hoTen = hoTen
        self.luonngCB = luonngCB

    def __init__(self,*arg,**kagr):

        if  kagr.get('MaNV') is None:
            self.maNV = kagr.get('MaNV')
        else:
            self.maNV = ''

        if kagr.get('hoTen') is None:
            self.hoTen = kagr.get('hoTen')
        else:
            self.hoTen = ''

        if kagr.get('luonngCB') is None:
            self.luonngCB = kagr.get('luonngCB')
        else:
            self.luonngCB = 0

        self.maNV = kagr.get('MaNV')
        self.hoTen = kagr.get('hoTen')
        self.luonngCB = kagr.get('luonngCB')


    def InThongTin(self, ):
        """đây là phương thức in thông tin"""
        print('\n')
        print("\t+Mã nhân viên:", self.maNV)
        print("\t+Họ Tên:", self.hoTen)
        print("\t+Lương CB:", self.luonngCB)



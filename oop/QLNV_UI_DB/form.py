#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from model import CongTy, VanPhong,BanHang,NhanVienQL,NhanVien


class QlnvApp(tk.Tk):
    def __init__(self, cty:CongTy):
        super().__init__()
        self.geometry("800x600")
        self.cty=cty

        # build ui
        frame1 = ttk.Frame(self)
        frame1.configure(height=600, width=800)
        label1 = ttk.Label(frame1)
        label1.configure(text='Quản Lý Nhân Viên')
        label1.place(anchor="nw", relx=0.45, x=0, y=0)
        label2 = ttk.Label(frame1)
        label2.configure(text='Mã NV')
        label2.place(anchor="nw", relx=0.05, rely=0.1, x=0, y=0)
        label3 = ttk.Label(frame1)
        label3.configure(text='Họ Tên')
        label3.place(anchor="nw", relx=0.05, rely=0.15, x=0, y=0)
        label4 = ttk.Label(frame1)
        label4.configure(text='Loại NV')
        label4.place(anchor="nw", relx=0.45, rely=0.15, x=0, y=0)

        """Loại Nhân viên"""
        self.cmbLoaiNV = ttk.Combobox(frame1)
        self.cmbLoaiNV.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.52,
            rely=0.15,
            x=0,
            y=0)
        self.cmbLoaiNV['values'] = [row[0] for row in self.cty.load_loaiNV()]

        """Entry thông tin """
        self.entryHoTen = ttk.Entry(frame1)
        self.entryHoTen.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.12,
            rely=0.15,
            x=0,
            y=0)

        self.entryMaNV = ttk.Entry(frame1)
        self.entryMaNV.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.12,
            rely=0.1,
            x=0,
            y=0)
        label5 = ttk.Label(frame1)
        label5.configure(text='Lương CB')
        label5.place(anchor="nw", relx=0.45, rely=0.1, x=0, y=0)

        self.entry_luongCB = ttk.Entry(frame1)
        self.entry_luongCB.place(
            anchor="nw",
            relwidth=0.24,
            relx=0.52,
            rely=0.1,
            x=0,
            y=0)
        self.btnThem = ttk.Button(frame1, text='Thêm NV', command=self.them_nv)
        self.btnThem.place(anchor="nw", relx=0.45, rely=0.3, x=0, y=0)

        self.btnTinhLuong = ttk.Button(frame1, text='Tình Lương', command=self.tinh_luong)
        self.btnTinhLuong.place(anchor="nw", relx=0.3, rely=0.3, x=0, y=0)

        self.btnLoad = ttk.Button(frame1, text='Load', command=self.load)
        self.btnLoad.place(anchor="nw", relx=0.15, rely=0.3, x=0, y=0)

        self.treeview1 = ttk.Treeview(frame1)
        self.treeview1.configure(selectmode="extended")

        self.treeview1["columns"] = ("c1", "c2", "c3", "c4", "c5")
        # ẩn cột mặc định
        self.treeview1["show"] = "headings"
        self.treeview1.column("c1", width=50)
        self.treeview1.column("c2", width=60)
        self.treeview1.column("c3", width=100)
        self.treeview1.column("c4", width=100)
        self.treeview1.column("c5", width=160)
        self.treeview1.heading("c1", text="STT")
        self.treeview1.heading("c2", text="Mã NV")
        self.treeview1.heading("c3", text="Họ Tên")
        self.treeview1.heading("c4", text="Lương CB")
        self.treeview1.heading("c5", text="Lương HT")

        self.treeview1.place(
            anchor="nw",
            relwidth=1.0,
            relx=0.0,
            rely=0.4,
            x=0,
            y=0)
        frame1.place(anchor="nw", x=0, y=0)

        self.message1 = tk.Message(frame1)
        self.message1.place(
            anchor="nw",
            relwidth=0.16,
            relx=0.8,
            rely=0.1,
            x=0,
            y=0)
        frame1.place(anchor="nw", x=0, y=0)

        # Main widget
        self.mainwindow = frame1

    def load(self):
        for i in self.treeview1.get_children():
            self.treeview1.delete(i)

        for i, nv in enumerate(self.cty.dsNV, start=1):
            self.treeview1.insert('', 'end', values=nv.row(i))

    def them_nv(self):
        try:
            maNV = self.entryMaNV.get()
            hoTen = self.entryHoTen.get()
            luongCB = self.entry_luongCB.get()
            loaiNV = self.cmbLoaiNV.get()

            # Check if any field is empty
            if not maNV or not hoTen or not luongCB or not loaiNV:
                raise ValueError("All fields must be filled.")

            # Check if luongCB is a number
            try:
                luongCB = float(luongCB)
            except ValueError:
                raise ValueError("luongCB must be a number.")

            # Check if maNV already exists
            if self.cty.tim_nv_by_maNV(maNV) is not None:
                raise ValueError(f"A NhanVien with maNV {maNV} already exists.")

            nv = NhanVien(maNV=maNV, hoTen=hoTen, luonngCB=luongCB, loaiNV=loaiNV)
            print(nv)
            # Add the new NhanVien object to the dsNV list
            self.cty.them_nv(nv)
            # Update the Treeview
            self.load()
            # Clear the input fields
            self.entryMaNV.delete(0, 'end')
            self.entryHoTen.delete(0, 'end')
            self.entry_luongCB.delete(0, 'end')
            self.cmbLoaiNV.set('')

        except Exception as e:
            self.message1.config(text=str(e))



    def tinh_luong(self):
        try:
            # Iterate over the dsNV list and calculate the salary for each NhanVien
            self.cty.tinh_luong_hang_thang()
            # Update the Treeview
            self.load()
        except Exception as e:
           self.message1.config(text=str(e))

    def run(self):
        self.mainwindow.mainloop()

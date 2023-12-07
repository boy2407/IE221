import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()

tree = ttk.Treeview(window)

tree["columns"] = ("c1", "c2", "c3")

tree.heading("c1", text="Cột 1")
tree.heading("c2", text="Cột 2")
tree.heading("c3", text="Cột 3")

tree.insert("", tk.END, text="Dòng 1", values=("Gia tri 1", "Gia tri 1", "Gia tri 3"))
tree.insert("", tk.END, text="Dòng 2", values=("Gia tri 1", "Gia tri 1", "Gia tri 3"))
tree.insert("", tk.END, text="Dòng 3", values=("Gia tri 1", "Gia tri 1", "Gia tri 3"))

tree.pack()

window.mainloop()
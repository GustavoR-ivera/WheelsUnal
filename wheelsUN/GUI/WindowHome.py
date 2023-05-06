import tkinter as tk
from tkinter import ttk, messagebox

class WindowHome(tk.Tk):
    def __init__(self):
        super().__init__()
        # basic config
        self.geometry('900x500')
        self.title('Home Wheels UN')
        # self.iconbitmap(windowIcon)
        self.resizable(False, False)


if __name__ == '__main__':
    w = WindowHome()
    w.mainloop()
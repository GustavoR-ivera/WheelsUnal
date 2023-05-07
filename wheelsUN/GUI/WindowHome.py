import tkinter as tk
from tkinter import ttk, messagebox

from BusinessLogic.AvailableTrips import AvailableTrips
from Data.UserDAOImpl import UserDAOImpl
from GUI.Card import Card





class WindowHome(tk.Tk):
    def __init__(self):
        super().__init__()
        # basic config
        self.geometry('1000x600')
        self.title('Home Wheels UN')
        # self.iconbitmap(windowIcon)
        self.resizable(False, False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=10)
        self.columnconfigure(3, weight=10)
        self.columnconfigure(4, weight=10)
        self.columnconfigure(5, weight=10)
        self.components()

    def components(self):
        #menu
        # Crear un objeto Canvas que contenga el widget que queremos desplazar
        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        # Crear un objeto Frame dentro del Canvas y agregar varios widgets al Frame
        self.frame = tk.Frame(canvas)
        self.frame.pack()
        # look for available trips and insert them to the frame and show them
        #execute query and fetchall data from user_rides
        self.availableTrips()
        # Configurar la barra de desplazamiento vertical
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)
        # Agregar el objeto Frame al Canvas
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        # Ajustar el tamaño del Canvas para que se adapte al contenido
        self.frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def availableTrips(self):
        userDAO = UserDAOImpl()
        a = AvailableTrips()
        # available rides
        rides = a.fetchall()
        for i in rides:
            user = userDAO.getUserById(i._creator_id)
            Card(self.frame, user.user_name, i._created_at, i._pickup_location, i._destination, i._departure_date,
                 i._charge, i._space_available, 'nissan', 'Verde', 'FGR-443', user.phoneNumber, i._description)

if __name__ == '__main__':
    w = WindowHome()
    w.mainloop()

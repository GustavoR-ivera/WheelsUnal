import sys
import tkinter as tk
from tkinter import ttk, messagebox

from BusinessLogic.AvailableTrips import AvailableTrips
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from GUI.Card import Card
from GUI.NewRide import NewRide


class WindowHome(tk.Tk):
    def __init__(self, active_user:User):
        super().__init__()
        # active_user
        self._active_user = active_user
        # basic config
        width_window = 1000
        heignt_window = 600
        x = self.winfo_screenwidth() // 2 - width_window // 2
        y = self.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y-50)
        self.geometry(position)
        # title
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
        self.create_menu()
        self.components()


    #get
    @property
    def active_user(self):
        return self._active_user

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

    def create_menu(self):
        #create de principal menu
        principal_menu = tk.Menu(self)
        #=========================create submenu=========================
        submenu_trips = tk.Menu(principal_menu, tearoff=False)
        #add item to submenu
        submenu_trips.add_command(label='Create trip', command=self.newRide)
        submenu_trips.add_separator()
        submenu_trips.add_command(label='Created trips')
        submenu_trips.add_command(label='Scheduled trips')
        #=========================create submenu=========================
        submenu_reports = tk.Menu(principal_menu, tearoff=False)
        #add item to submenu
        submenu_reports.add_command(label='History trips')
        submenu_reports.add_separator()
        submenu_reports.add_command(label='Generate report')
        #=========================create submenu=========================
        submenu_options = tk.Menu(principal_menu, tearoff=False)
        # add item to submenu
        submenu_options.add_command(label='Edit profile')
        submenu_options.add_separator()
        submenu_options.add_command(label='Exit', command=self.exit_app)
        # add new seccions into the principal menu=========================
        principal_menu.add_cascade(menu=submenu_trips, label='My trips')
        principal_menu.add_cascade(menu=submenu_reports, label='Reports')
        principal_menu.add_cascade(menu=submenu_options, label='Options')
        self.config(menu=principal_menu)

    def exit_app(self):
        self.quit()
        self.destroy()
        sys.exit()

    def newRide(self):
        #self.quit()
        n = NewRide(self.active_user)
        n.mainloop()

    def availableTrips(self):
        userDAO = UserDAOImpl()
        a = AvailableTrips()
        # available rides
        rides = a.fetchall()
        for ride in rides:
            user_ride_creator = userDAO.getUserById(ride._creator_id)
            # compare if the ride creator is equal to the active_user
            if user_ride_creator.user_id == self.active_user.user_id:
                Card(self.frame, user_ride_creator.user_name, ride._created_at, ride._pickup_location,
                     ride._destination, ride._departure_date, ride._charge,
                     ride._space_available, 'nissan', 'Verde', 'FGR-443', user_ride_creator.phoneNumber,
                     ride._description, True)
            else:
                Card(self.frame, user_ride_creator.user_name, ride._created_at, ride._pickup_location,
                     ride._destination, ride._departure_date, ride._charge,
                     ride._space_available, 'nissan', 'Verde', 'FGR-443', user_ride_creator.phoneNumber,
                     ride._description, False)

if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    alexa = userdao.getUserById(25)
    w = WindowHome(alexa)
    w.mainloop()

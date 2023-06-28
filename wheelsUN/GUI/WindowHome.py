import sys
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

from BusinessLogic.AvailableTrips import AvailableTrips
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from GUI.Card import Card
from GUI.NewRide import NewRide
from GUI.NewVehicle import NewVehicle


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
        #create threat 1
        #self.hilo1 = threading.Thread(target=self.availableTrips)
        #self.hilo1.start()
        # creates the canvas and the frame with the card objects
        self.components()
        self.create_menu()

    #get
    @property
    def active_user(self):
        return self._active_user

    def components(self):
        self.updateFeedbackBtn = ttk.Button(self, text='Update feedback', command=self.updateFeedback)
        # especify cell's coordinates
        self.updateFeedbackBtn.pack()
        #updateFeedbackBtn.grid(row=0, column=0, sticky='NSWE', padx=10, pady= 10)

        # Crear un objeto Canvas que contenga el widget que queremos desplazar
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Crear un objeto Frame dentro del Canvas y agregar varios widgets al Frame
        self.frame = tk.Frame(self.canvas)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # look for available trips and insert them to the frame and show them
        #execute directly the method fetchall data from user_rides
        self.availableTrips()

        # Configurar la barra de desplazamiento vertical
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        #canvas.config(yscrollcommand=scrollbar.set)
        # Agregar el objeto Frame al Canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        # Ajustar el tamaño del Canvas para que se adapte al contenido
        self.frame.update_idletasks()
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def create_menu(self):
        #create de principal menu
        principal_menu = tk.Menu(self)
        #=========================create submenu=========================
        submenu_trips = tk.Menu(principal_menu, tearoff=False)
        #add item to submenu
        submenu_trips.add_command(label='Create trip', command=self.newRide)
        submenu_trips.add_separator()
        submenu_trips.add_command(label='Created trips',command=self.newRide)
        submenu_trips.add_command(label='Scheduled trips', command=self.newRide)
        # =========================create submenu=========================
        submenu_vehicles = tk.Menu(principal_menu, tearoff=False)
        submenu_vehicles.add_command(label='Register vehicle', command=self.newVehicle)
        submenu_vehicles.add_command(label='My vehicles', command=self.myVehicles)
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
        principal_menu.add_cascade(menu=submenu_vehicles, label='Vehicles')
        principal_menu.add_cascade(menu=submenu_reports, label='Reports')
        principal_menu.add_cascade(menu=submenu_options, label='Options')
        self.config(menu=principal_menu)

    def exit_app(self):
        #finish threat
        #self.hilo1.join()
        self.quit()
        self.destroy()
        sys.exit()

    def newRide(self):
        #close current window
        self.quit()
        self.destroy()
        #open new window form
        n = NewRide(self.active_user, self)
        n.mainloop()

    def newVehicle(self):
        # open new window form
        n = NewVehicle(self.active_user)
        n.mainloop()

    def myVehicles(self):
        pass

    def updateFeedback(self):
        #Obtener una lista de todos los widgets dentro del frame
        widgets = self.frame.winfo_children()
        # Eliminar cada widget del frame
        for widget in widgets:
            widget.destroy()

        # Ajustar el tamaño del Canvas para que se adapte al contenido
        self.frame.update_idletasks()
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.availableTrips()
        # self.scrollbar.destroy()
        # self.frame.destroy()
        # self.canvas.destroy()
        # self.updateFeedbackBtn.destroy()
        # #create all again
        # self.components()
        #


    def availableTrips(self):
        userDAO = UserDAOImpl()
        vehicleDAO = VehicleDAOImpl()
        a = AvailableTrips()
        # available rides
        rides = a.fetchall()
        for ride in rides:
            #get the current vehicle of the ride
            v = vehicleDAO.getVehicleById(ride._vehicle_id)
            #get the creator of the ride
            user_ride_creator = userDAO.getUserById(ride._creator_id)
            # compare if the ride creator is equal to the active_user
            if user_ride_creator.user_id == self.active_user.user_id:
                match_user = True
            else:
                match_user = False

            Card(self.frame, self ,user_ride_creator.user_name, ride._created_at, ride._pickup_location,
                 ride._destination, ride._departure_date, ride._charge,
                 ride._space_available, v.brand, v.color, v.vehicle_plate, user_ride_creator.phoneNumber,
                 ride._description, match_user, ride._ride_id, self.active_user.user_id)


if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    alexa = userdao.getUserById(27)
    w = WindowHome(alexa)
    w.mainloop()

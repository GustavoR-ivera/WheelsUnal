import sys
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox
import tkintermapview
from BusinessLogic.AvailableTrips import AvailableTrips
from BusinessLogic.DLL import DLL
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from GUI.Card import Card
from GUI.CardFrame import CardFrame
from GUI.NewReport import NewReport
from GUI.NewRide import NewRide
from GUI.NewVehicle import NewVehicle
from PIL import Image, ImageTk


class WindowHome(tk.Tk):
    def __init__(self, active_user:User):
        super().__init__()
        # active_user
        self._active_user = active_user
        # ------------------basic config
        # width_window = 1500
        # heignt_window = 800
        # x = self.winfo_screenwidth() // 2 - width_window // 2
        # y = self.winfo_screenheight() // 2 - heignt_window // 2
        # position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y-50)
        # self.geometry(position)
        #------------------full screen
        self.attributes('-fullscreen', True)
        # Mostrar los botones de minimizar y cerrar
        self.overrideredirect(False)
        #----------------------------
        # title
        self.title('Home Wheels UN')
        # self.iconbitmap(windowIcon)
        #self.resizable(False, False)
        # 1. grid configuration
        # 3 rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=100)
        self.grid_rowconfigure(2, weight=30)
        # 1 column
        self.grid_columnconfigure(0, weight=1)
        #create threat 1
        #self.hilo1 = threading.Thread(target=self.availableTrips)
        #self.hilo1.start()
        # creates the canvas and the frame with the card objects
        self.create_menu()
        self.add_shortcuts()
        self.frameList()
        self.footer()

    #get
    @property
    def active_user(self):
        return self._active_user
#-----------------------------------------------------------------------------------------------------
    def frameList(self):
        #create the list
        self.list = DLL()
        #create the initial frame (principal content -> rides available)
        f1 = CardFrame(self, self.active_user, True, self.list)
        #add the frame to the list
        self.list.append(f1)
        #list.head.data.tkraise()

# ------------------------------------------------------------------------------------------------------------
    def add_shortcuts(self):
        # shortcuts section row 0 of the window
        #----------------------------------------------------------------------
        self.shortCuts = tk.LabelFrame(self, text="shorcuts")
        self.shortCuts.columnconfigure(0, weight=10)
        self.shortCuts.columnconfigure(1, weight=10)
        self.shortCuts.columnconfigure(2, weight=10)
        self.shortCuts.columnconfigure(3, weight=10)
        self.shortCuts.columnconfigure(4, weight=1)
        self.shortCuts.columnconfigure(5, weight=1)
        self.shortCuts.columnconfigure(6, weight=1)
        self.shortCuts.grid(row=0, column=0, sticky="nswe")
        #self.shortCuts.pack()

        # userProfileIcon
        imagen = Image.open(r"C:\Users\adibl\OneDrive\Escritorio\Proyectos\WheelsUnal\wheelsUN\Icons\userProfile.png")  # Reemplaza "icono.png" con la ruta de tu imagen
        #imagen = imagen.resize((20, 20))
        self.photo = ImageTk.PhotoImage(imagen)
        self.testbtn = ttk.Button(self.shortCuts, image=self.photo)
        # especify cell's coordinates
        #self.testbtn.pack(side="right")
        self.testbtn.grid(row=0, column=4)

        #notificationsIcon
        imagen2 = Image.open(
            r"C:\Users\adibl\OneDrive\Escritorio\Proyectos\WheelsUnal\wheelsUN\Icons\notificationsIcon.jpg")
        # imagen = imagen.resize((20, 20))
        self.photo2 = ImageTk.PhotoImage(imagen2)
        self.testbtn2 = ttk.Button(self.shortCuts, image=self.photo2)
        # especify cell's coordinates
        #self.testbtn2.pack(side="right")
        self.testbtn2.grid(row=0, column=5)


        #update feedback icon
        imagen3 = Image.open(
            r"C:\Users\adibl\OneDrive\Escritorio\Proyectos\WheelsUnal\wheelsUN\Icons\updateFeedbackIcon.png"
        )
        self.photo3 = ImageTk.PhotoImage(imagen3)
        self.updateFeedbackBtn = ttk.Button(self.shortCuts, image=self.photo3, command=self.updateFeedback)
        # especify cell's coordinates
        #self.updateFeedbackBtn.pack(side="right")
        self.updateFeedbackBtn.grid(row=0, column=6)

#------------------------------------------------------------------------------------------------------------
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
        submenu_reports.add_command(label='Generate report', command=self.makeReport)
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

    def footer(self):
        self.test = tk.LabelFrame(self, text="footer")
        self.test.grid(row=2, column=0, sticky="nswe")
        self.label = ttk.Label(self.test, text="footer")
        self.label.grid(row=0, column=0)

    def exit_app(self):
        #finish threat
        #self.hilo1.join()
        self.quit()
        self.destroy()
        sys.exit()

    def newRide(self):

        #set False in current Frame
        n = self.list.head
        flag = True
        while (flag):
            if (n.data.currentFrame == True or n.next == None):
                flag = False
            else:
                n = n.next
        #with the currentFrame we can
        #set False in the currentFrame value
        n.data.currentFrame = False

        #open new window form
        n = NewRide(self, self.active_user, True, self.list)
        #add the new frame to the list
        self.list.append(n)
        self.list.getTail().data.tkraise()

    def newVehicle(self):
        # open new window form
        n = NewVehicle(self.active_user)
        n.mainloop()

    def myVehicles(self):
        pass

    def makeReport(self):
        n = NewReport(self.active_user)
        n.mainloop()

    def updateFeedback(self):
        # #Obtener una lista de todos los widgets dentro del frame
        # widgets = self.frame.winfo_children()
        # # Eliminar cada widget del frame
        # for widget in widgets:
        #     widget.destroy()
        #
        # # Ajustar el tamaño del Canvas para que se adapte al contenido
        # self.frame.update_idletasks()
        # self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        #
        # self.availableTrips()
        # # self.scrollbar.destroy()
        # # self.frame.destroy()
        # # self.canvas.destroy()
        # # self.updateFeedbackBtn.destroy()
        # # #create all again
        # # self.components()

        #notificar la accion realizada en la etiqueta comodin
        from datetime import datetime
        currentDate = datetime.now().time()
        #value = f"updated at {str(currentDate.hour)} {str(currentDate.minute)} {str(currentDate.second)}"
        value = f"updated at: {currentDate}"
        self.labelComodin = ttk.Label(self.shortCuts, text= value)
        # especify cell's coordinates
        #self.testbtn.pack(side="right")
        self.labelComodin.grid(row=0, column=0)





if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    alexa = userdao.getUserById(27)
    w = WindowHome(alexa)
    w.mainloop()

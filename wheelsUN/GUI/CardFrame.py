import tkinter as tk

from BusinessLogic.AvailableTrips import AvailableTrips
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from GUI.Card import Card


class CardFrame(tk.LabelFrame):
        def __init__(self, parent, active_user, currentFrame, frameList):
                super().__init__(parent)
                #parent is the window object
                self.parent = parent
                self.active_user = active_user
                # initialize the list of frames
                self.frameList = frameList
                # currentFrame
                self.currentFrame = currentFrame
                #-------------------------------------------------------------------
                # 1. grid configuration
                # 1 row
                self.grid_rowconfigure(0, weight=1)
                #7 columns
                self.columnconfigure(0, weight=1)
                self.columnconfigure(1, weight=1)
                self.columnconfigure(2, weight=1)
                self.columnconfigure(3, weight=1)
                self.columnconfigure(4, weight=1)
                self.columnconfigure(5, weight=1)
                self.columnconfigure(6, weight=1)
                #--------------------------------------------------------------------
                #frame home
                # Crear un objeto Canvas que contenga el widget que queremos desplazar
                self.canvas = tk.Canvas(self)
                self.canvas.grid(row=0, column=0, columnspan=7, sticky="nsew")
                #self.canvas.pack(side="left", fill="both", expand=True)

                # Crear un objeto Frame dentro del Canvas y agregar varios widgets al Frame
                self.frameScrollbar = tk.Frame(self.canvas)
                self.frameScrollbar.grid(row=0, column=7,  sticky="nsew")
                #self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # look for available trips and insert them to the frame and show them
                #execute directly the method fetchall data from user_rides
                self.availableTrips()

                # Configurar la barra de desplazamiento vertical
                self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
                self.scrollbar.grid(row=0, column=7, sticky="ns")
                #self.scrollbar.pack(side="right", fill="y")

                self.scrollbar.config(command=self.canvas.yview)
                self.canvas.config(yscrollcommand=self.scrollbar.set)

                #canvas.config(yscrollcommand=scrollbar.set)
                # Agregar el objeto Frame al Canvas
                self.canvas.create_window((0, 0), window=self.frameScrollbar, anchor="nw")
                # Ajustar el tamaño del Canvas para que se adapte al contenido
                self.frameScrollbar.update_idletasks()
                # Configurar desplazamiento con el mouse en el lienzo
                self.canvas.bind_all("<MouseWheel>",
                                      lambda event: self.canvas.yview_scroll(-1 * (event.delta // 120), "units"))
                self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

                #ubicacion del cardframe en la ventana
                #los frames dinamicos inician en la fila 1 de la ventana
                #ocuparan el espacio completo de la ventana horizontalmente
                self.grid(row=1, column=0, sticky='NSWE')

        def availableTrips(self):
                userDAO = UserDAOImpl()
                vehicleDAO = VehicleDAOImpl()
                a = AvailableTrips()
                # available rides
                rides = a.fetchall()
                for ride in rides:
                        # get the current vehicle of the ride
                        v = vehicleDAO.getVehicleById(ride._vehicle_id)
                        # get the creator of the ride
                        user_ride_creator = userDAO.getUserById(ride._creator_id)
                        # compare if the ride creator is equal to the active_user
                        if user_ride_creator.user_id == self.active_user.user_id:
                                match_user = True
                        else:
                                match_user = False

                        Card(self.frameScrollbar, self.parent, user_ride_creator.user_name, ride._created_at, ride._pickup_location,
                             ride._destination, ride._departure_date, ride._charge,
                             ride._space_available, v.brand, v.color, v.vehicle_plate, user_ride_creator.phoneNumber,
                             ride._description, match_user, ride._ride_id, self.active_user.user_id)

if __name__ == "__main__":
        u = User()
        userdao = UserDAOImpl()
        alexa = userdao.getUserById(27)

        root = tk.Tk()
        CardFrame(root, alexa)

        root.mainloop()
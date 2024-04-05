import tkinter as tk
from tkinter import ttk, messagebox
from Data.Ride import Ride
from Data.RideDAOImpl import RideDAOImpl
from Data.RideEventRegister import RideEventRegister
from Data.RideEventRegisterDAOImpl import RideEventRegisterDAOImpl
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from Data.Vehicle import Vehicle
from datetime import datetime




class NewRide(tk.LabelFrame):

    def __init__(self, parent,  active_user: User, currentFrame, frameList):
        super().__init__(parent)
        #initialize active user
        self.active_user = active_user
        #initialize the principal window reference
        self.parent = parent
        #initialize the list of frames
        self.frameList = frameList
        # currentFrame
        self.currentFrame = currentFrame

        # 1. grid configuration
        #1 row
        #self.rowconfigure(0, weight=1)
        #6 columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.components()



    def components(self):
        if(self.getVehicles()):
            #create a label frame for the form
            self.formFrame = ttk.LabelFrame(self, text="form", border=2)
            # 2 columns
            self.formFrame.columnconfigure(0, weight=1)
            self.formFrame.columnconfigure(1, weight=1)


            #add elements to formFrame
            self.lable_Text = tk.Label(self.formFrame, text='Create a new ride')
            self.lable_Text.grid(row=0, column=0, sticky='NSWE', columnspan=2)

            #label pick up location
            pickupLocationLabel = tk.Label(self.formFrame, text='Pickup location: ')
            pickupLocationLabel.grid(row=2, column=0, sticky='E')
            #text field pickupLocation
            self.pickupLocationEntry = tk.Entry(self.formFrame, width=30)
            self.pickupLocationEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

            #label destination
            destinationLabel = tk.Label(self.formFrame, text='Destination: ')
            destinationLabel.grid(row=3, column=0, sticky='E')
            #text field destinationLabel
            self.destinationEntry = tk.Entry(self.formFrame, width=30)
            self.destinationEntry.grid(row=3, column=1, sticky='W', padx= 10, pady=15)

            # label space available
            spaceAvailableLabel = tk.Label(self.formFrame, text='Space available: ')
            spaceAvailableLabel.grid(row=4, column=0, sticky='E')
            # text field DNI type
            self.spaceAvailableEntry = tk.Entry(self.formFrame, width=30)
            self.spaceAvailableEntry.grid(row=4, column=1, sticky='W', padx=10, pady=15)

            # label departureDate
            departureDateLabel = tk.Label(self.formFrame, text='Departure date (aaaa/mm/dd hh:mm:ss): ')
            departureDateLabel.grid(row=5, column=0, sticky='E')
            # text field departureDate
            self.departureDateEntry = tk.Entry(self.formFrame, width=30)
            self.departureDateEntry.grid(row=5, column=1, sticky='W', padx=10, pady=15)

            # label charge
            chargeLabel = tk.Label(self.formFrame, text='Charge (COP): ')
            chargeLabel.grid(row=6, column=0, sticky='E')
            # text field charge
            self.chargeEntry = tk.Entry(self.formFrame, width=30)
            #self.chargeEntry.insert(tk.END, ".00")
            self.chargeEntry.grid(row=6, column=1, sticky='W', padx=10, pady=15)

            #label vehicles
            vehiclesLabel = tk.Label(self.formFrame, text='Select vehicle: ')
            vehiclesLabel.grid(row=7, column=0, sticky='E')

            # Crea la lista desplegable
            user_vehicle_details=self.getVehicles()
            #options = ["color, placa, dd"]
            self.selected_option = tk.StringVar(self.formFrame, value='select a vehicle')
            vehiclesList = ttk.Combobox(self.formFrame, textvariable=self.selected_option, values=user_vehicle_details, state="readonly")
            vehiclesList.grid(row=7, column=1, sticky='WE', padx=10, pady=15)

            #label description
            descriptionLabel = tk.Label(self.formFrame, text='Description: ')
            descriptionLabel.grid(row=8, column=0, sticky='E')
            # campo de texto
            self.descriptionText = tk.Text(self.formFrame, width=5, height=5)
            self.descriptionText.grid(row=8, column=1, sticky='NSWE', padx= 10, pady=5)

            self.btnCreate = ttk.Button(self.formFrame, text='Create', command=self.createNewRide)
            # especify cell's coordinates
            self.btnCreate.grid(row=10, column=0, sticky='NSWE', padx=50, pady= 10)

            self.btnCancel = ttk.Button(self.formFrame, text='Back', command=self.back)
            # especify cell's coordinates
            self.btnCancel.grid(row=10, column=1, sticky='NSWE', padx=50, pady= 10)

            # location of formFrame on the big frame
            self.formFrame.grid(row=0, column=2, sticky='NSWE', columnspan=2)

            # ubicacion del frame en la ventana
            # los frames dinamicos inician en la fila 1 de la ventana
            # ocuparan el espacio completo de la ventana horizontalmente
            self.grid(row=1, column=0, sticky='NSWE')
        else:
            messagebox.showwarning("warning", "You don't have any vehicle available")
            self.cancel()

    def createNewRide(self):
        # create a ride object and capture data from the form fields
        #get the vehicle id with the vehicle plate
        list_vehicle_details = self.selected_option.get().split(',')
        #print(list_vehicle_details)
        vehicle_plate = list_vehicle_details[len(list_vehicle_details)-1]
        #print(vehicle_plate)
        v = VehicleDAOImpl()
        selected_vehicle = v.getVehicleByPlate(vehicle_plate)
        if isinstance(selected_vehicle, Vehicle):
            #create ride object
            r = Ride(creator_id=self.active_user.user_id,pickup_location=self.pickupLocationEntry.get(),
                     destination=self.destinationEntry.get(),space_available=self.spaceAvailableEntry.get(),
                     departure_date=self.departureDateEntry.get(),charge=self.chargeEntry.get(),
                     vehicle_id=selected_vehicle.vehicle_id,description=self.descriptionText.get("1.0", tk.END))
            #print(self.selected_option.get(), self.descriptionText.get("1.0", tk.END))
            rideDAO = RideDAOImpl()
            if rideDAO.insert(r):
                #self.cancel()
                #clear the text fields
                self.pickupLocationEntry.delete(0, tk.END)
                self.destinationEntry.delete(0, tk.END)
                self.spaceAvailableEntry.delete(0, tk.END)
                self.departureDateEntry.delete(0, tk.END)
                self.chargeEntry.delete(0, tk.END)
                self.descriptionText.delete(1.0, tk.END)
                self.selected_option.set('select a vehicle')
                #successful ride creation
                #self.parent.updateFeedback()


                # record event
                #capture last ride for the current user
                lastRide = rideDAO.getLastRideCreatedByUser(self.active_user)
                #create event description
                event_description = f"the user with id: {self.active_user.user_id} ({self.active_user.user_name})" \
                                    f" created the ride with id: {lastRide._ride_id}"
                event = RideEventRegister(lastRide._ride_id, self.active_user.user_id, event_description, datetime.now())
                eventDAO = RideEventRegisterDAOImpl()
                #insert record
                if eventDAO.insert(event):
                    messagebox.showinfo("Informative", "Ride created successfully")

        else:
            self.pickupLocationEntry.delete(0, tk.END)
            self.destinationEntry.delete(0, tk.END)
            self.spaceAvailableEntry.delete(0, tk.END)
            self.departureDateEntry.delete(0, tk.END)
            self.chargeEntry.delete(0, tk.END)
            self.descriptionText.delete(1.0, tk.END)
            self.selected_option.set('select a vehicle')
            #failed ride creation
            messagebox.showinfo("Warning", "Failed to create trip, try again")


    def getVehicles(self):
        #execute the query in order to get the data of the user vehicles
        # list vehicles
        v = VehicleDAOImpl()
        user_vehicles = v.getVehiclesByOwnerId(self.active_user.user_id)
        if user_vehicles:
            vehicle_details = []
            for vehicle in user_vehicles:
                details = f"{vehicle.type},{vehicle.brand},{vehicle.color},{vehicle.vehicle_plate}"
                vehicle_details.append(details)
            # getVehicles()
            #print(vehicle_details)
            return vehicle_details
        else:
            return 0

    def back(self):
        # set False in current Frame
        n = self.frameList.head
        flag = True
        while (flag):
            if (n.data.currentFrame == True or n.next == None):
                flag = False
            else:
                n = n.next
        # with the currentFrame we can
        # set False in the currentFrame value
        n.data.currentFrame = False
        #get the prev node
        previousFrame = n.prev
        #once we know the prev node get the data and set the atribute currentFrame in true
        previousFrame.data.currentFrame = True
        #show the new frame
        previousFrame.data.tkraise()

if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    alexa = userdao.getUserById(27)

    root = tk.Tk()
    NewRide(root, alexa)

    root.mainloop()
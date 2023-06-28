import tkinter as tk
from tkinter import ttk, messagebox
from Data.Ride import Ride
from Data.RideDAOImpl import RideDAOImpl
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from Data.Vehicle import Vehicle



class NewRide(tk.Tk):

    def __init__(self, active_user: User, pwindow):
        super().__init__()
        #initialize active user
        self.active_user = active_user
        #initialize the principal window reference
        self.pwindow = pwindow
        # basic config
        width_window = 500
        heignt_window = 500
        x = self.winfo_screenwidth() // 2 - width_window // 2
        y = self.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y - 50)
        self.geometry(position)
        #title
        self.title('Create a new ride')
        #self.iconbitmap(windowIcon)
        self.resizable(False,False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)

        self.components()



    def components(self):
        if(self.getVehicles()):
            appName = tk.Label(self, text='Wheels UN')
            appName.grid(row=0, column=0, sticky='NSWE', columnspan=2)

            self.lable_Text = tk.Label(self, text='Create a new ride')
            self.lable_Text.grid(row=1, column=0, sticky='NSWE', columnspan=2)

            #label pick up location
            pickupLocationLabel = tk.Label(self, text='Pickup location: ')
            pickupLocationLabel.grid(row=2, column=0, sticky='E')
            #text field pickupLocation
            self.pickupLocationEntry = tk.Entry(self, width=30)
            self.pickupLocationEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

            #label destination
            destinationLabel = tk.Label(self, text='Destination: ')
            destinationLabel.grid(row=3, column=0, sticky='E')
            #text field destinationLabel
            self.destinationEntry = tk.Entry(self, width=30)
            self.destinationEntry.grid(row=3, column=1, sticky='W', padx= 10, pady=15)

            # label space available
            spaceAvailableLabel = tk.Label(self, text='Space available: ')
            spaceAvailableLabel.grid(row=5, column=0, sticky='E')
            # text field DNI type
            self.spaceAvailableEntry = tk.Entry(self, width=30)
            self.spaceAvailableEntry.grid(row=5, column=1, sticky='W', padx=10, pady=15)

            # label departureDate
            departureDateLabel = tk.Label(self, text='Departure date (aaaa/mm/dd hh:mm:ss): ')
            departureDateLabel.grid(row=4, column=0, sticky='E')
            # text field departureDate
            self.departureDateEntry = tk.Entry(self, width=30)
            self.departureDateEntry.grid(row=4, column=1, sticky='W', padx=10, pady=15)

            # label charge
            chargeLabel = tk.Label(self, text='Charge (COP): ')
            chargeLabel.grid(row=6, column=0, sticky='E')
            # text field charge
            self.chargeEntry = tk.Entry(self, width=30)
            #self.chargeEntry.insert(tk.END, ".00")
            self.chargeEntry.grid(row=6, column=1, sticky='W', padx=10, pady=15)

            #label vehicles
            vehiclesLabel = tk.Label(self, text='Select vehicle: ')
            vehiclesLabel.grid(row=7, column=0, sticky='E')

            # Crea la lista desplegable
            user_vehicle_details=self.getVehicles()
            #options = ["color, placa, dd"]
            self.selected_option = tk.StringVar(self, value='select a vehicle')
            vehiclesList = ttk.Combobox(self, textvariable=self.selected_option, values=user_vehicle_details, state="readonly")
            vehiclesList.grid(row=7, column=1, sticky='WE', padx=10, pady=15)

            #label description
            descriptionLabel = tk.Label(self, text='Description: ')
            descriptionLabel.grid(row=8, column=0, sticky='E')
            # campo de texto
            self.descriptionText = tk.Text(self, width=5, height=5)
            self.descriptionText.grid(row=8, column=1, sticky='NSWE', padx= 10, pady=5)

            self.btnCreate = ttk.Button(self, text='Create', command=self.createNewRide)
            # especify cell's coordinates
            self.btnCreate.grid(row=10, column=0, sticky='NSWE', padx=50, pady= 10)

            self.btnCancel = ttk.Button(self, text='Cancel', command=self.cancel)
            # especify cell's coordinates
            self.btnCancel.grid(row=10, column=1, sticky='NSWE', padx=50, pady= 10)
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
                messagebox.showinfo("Informative", "Ride created successfully")
                #self.pwindow.updateFeedback()

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

    def cancel(self):
        from GUI.WindowHome import WindowHome
        # close current window
        self.quit()
        self.destroy()
        # open a new window home
        w = WindowHome(self.active_user)
        w.mainloop()
        #update principal window
        #self.pwindow.updateFeedback()

if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    user = userdao.getUserById(25)
    w = NewRide(user)
    w.mainloop()
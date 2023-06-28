import tkinter as tk
from tkinter import ttk, messagebox
from Data.Ride import Ride
from Data.RideDAOImpl import RideDAOImpl
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.VehicleDAOImpl import VehicleDAOImpl
from Data.Vehicle import Vehicle



class NewVehicle(tk.Tk):

    def __init__(self, active_user: User):
        super().__init__()
        #initialize active user
        self.active_user = active_user
        # basic config
        width_window = 500
        heignt_window = 550
        x = self.winfo_screenwidth() // 2 - width_window // 2
        y = self.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y - 50)
        self.geometry(position)
        #title
        self.title('Register a new vehicle')
        #self.iconbitmap(windowIcon)
        self.resizable(False,False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)

        self.components()



    def components(self):

        appName = tk.Label(self, text='Wheels UN')
        appName.grid(row=0, column=0, sticky='NSWE', columnspan=2)

        labelText = tk.Label(self, text='Register your vehicle')
        labelText.grid(row=1, column=0, sticky='NSWE', columnspan=2)

        #label
        vehiclePlateLabel = tk.Label(self, text='Vehicle plate: ')
        vehiclePlateLabel.grid(row=2, column=0, sticky='E')
        #text field
        self.vehiclePlateEntry = tk.Entry(self, width=30)
        self.vehiclePlateEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

        #label
        colorLabel = tk.Label(self, text='Color: ')
        colorLabel.grid(row=3, column=0, sticky='E')
        #text
        self.colorEntry = tk.Entry(self, width=30)
        self.colorEntry.grid(row=3, column=1, sticky='W', padx= 10, pady=15)

        # label
        typeLabel = tk.Label(self, text='Vehicle type: ')
        typeLabel.grid(row=4, column=0, sticky='E')
        # text
        self.typeEntry = tk.Entry(self, width=30)
        self.typeEntry.grid(row=4, column=1, sticky='W', padx=10, pady=15)

        # label
        spaceAvailableLabel = tk.Label(self, text='Space available: ')
        spaceAvailableLabel.grid(row=5, column=0, sticky='E')
        # text
        self.spaceAvailableEntry = tk.Entry(self, width=30)
        self.spaceAvailableEntry.grid(row=5, column=1, sticky='W', padx=10, pady=15)

        # label
        modelLabel = tk.Label(self, text='Vehicle model: ')
        modelLabel.grid(row=6, column=0, sticky='E')
        # text field
        self.modelEntry = tk.Entry(self, width=30)
        self.modelEntry.grid(row=6, column=1, sticky='W', padx=10, pady=15)

        # label
        soatLabel = tk.Label(self, text='SOAT: ')
        soatLabel.grid(row=7, column=0, sticky='E')
        # text field
        self.soatEntry = tk.Entry(self, width=30)
        self.soatEntry.grid(row=7, column=1, sticky='W', padx=10, pady=15)

        # label
        mechanicalConditionLabel = tk.Label(self, text='Mechanical condition: ')
        mechanicalConditionLabel.grid(row=8, column=0, sticky='E')
        # text field
        self.mechanicalConditionEntry = tk.Entry(self, width=30)
        self.mechanicalConditionEntry.grid(row=8, column=1, sticky='W', padx=10, pady=15)

        # label
        transitLicenseLabel = tk.Label(self, text='Transit license: ')
        transitLicenseLabel.grid(row=9, column=0, sticky='E')
        # text field
        self.transitLicenseEntry = tk.Entry(self, width=30)
        self.transitLicenseEntry.grid(row=9, column=1, sticky='W', padx=10, pady=15)

        # label
        brandLabel = tk.Label(self, text='Brand: ')
        brandLabel.grid(row=10, column=0, sticky='E')
        # text field
        self.brandEntry = tk.Entry(self, width=30)
        self.brandEntry.grid(row=10, column=1, sticky='W', padx=10, pady=15)

        btnCreate = ttk.Button(self, text='Register', command=self.registerNewVehicle)
        # especify cell's coordinates
        btnCreate.grid(row=11, column=0, sticky='NSWE', padx=50, pady= 10)

        btnCancel = ttk.Button(self, text='Cancel', command=self.cancel)
        # especify cell's coordinates
        btnCancel.grid(row=11, column=1, sticky='NSWE', padx=50, pady= 10)

    def registerNewVehicle(self):
        # create a vehicle object and capture data from the form fields
        v = Vehicle(vehicle_plate=self.vehiclePlateEntry.get(),color=self.colorEntry.get(),type=self.typeEntry.get(),
                    space_available=self.spaceAvailableEntry.get(),model=self.modelEntry.get(),
                    owner_id=self.active_user.user_id,
                    soat_policy=self.soatEntry.get(),mechanical_condition_policy=self.mechanicalConditionEntry.get(),
                    transit_license=self.transitLicenseEntry.get(),brand=self.brandEntry.get())
        #print(self.selected_option.get(), self.descriptionText.get("1.0", tk.END))
        vehicleDAO = VehicleDAOImpl()
        if vehicleDAO.insert(v):
            #self.cancel()
            #clear the text fields
            self.vehiclePlateEntry.delete(0, tk.END)
            self.colorEntry.delete(0, tk.END)
            self.typeEntry.delete(0, tk.END)
            self.spaceAvailableEntry.delete(0, tk.END)
            self.modelEntry.delete(0, tk.END)
            self.soatEntry.delete(0, tk.END)
            self.mechanicalConditionEntry.delete(0, tk.END)
            self.transitLicenseEntry.delete(0, tk.END)
            self.brandEntry.delete(0, tk.END)
            #successful ride creation
            messagebox.showinfo("Informative", "Vehicle registered successfully")
        else:
            self.vehiclePlateEntry.delete(0, tk.END)
            self.colorEntry.delete(0, tk.END)
            self.typeEntry.delete(0, tk.END)
            self.spaceAvailableEntry.delete(0, tk.END)
            self.modelEntry.delete(0, tk.END)
            self.soatEntry.delete(0, tk.END)
            self.mechanicalConditionEntry.delete(0, tk.END)
            self.transitLicenseEntry.delete(0, tk.END)
            self.brandEntry.delete(0, tk.END)
            #failed ride creation
            messagebox.showinfo("Warning", "Failed to create trip, try again")


    def cancel(self):
        from GUI.WindowHome import WindowHome
        # close current window
        self.quit()
        self.destroy()
        # # open new window form
        # w = WindowHome(self.active_user)
        # w.mainloop()

if __name__ == '__main__':
    u = User()
    userdao = UserDAOImpl()
    user = userdao.getUserById(25)
    w = NewVehicle(user)
    w.mainloop()
import tkinter
from tkinter import messagebox
from Data.Ride import Ride
from Data.RideDAOImpl import RideDAOImpl
from Data.User import User
from Data.VehicleDAOImpl import VehicleDAOImpl
from GUI.NewRide import NewRide


class UpdateRide(NewRide):
    def __init__(self, active_user: User, ride_id, pwindow):
        super().__init__(active_user, pwindow)
        self.pwindow = pwindow
        #config form
        self.ride_id = ride_id
        self.title("Update ride")
        self.lable_Text.config(text='Update the ride')
        self.btnCreate.config(text='Save', command=self.update)
        #get the ride info
        self.getRideInformation()

    def update(self):
        #get the current ride object
        r = RideDAOImpl()
        currentRide = r.getRideById(self.ride_id)
        #===================================
        #get and update the new ride info
        list_vehicle_details = self.selected_option.get().split(',')
        # print(list_vehicle_details)
        vehicle_plate = list_vehicle_details[len(list_vehicle_details) - 1]
        # print(vehicle_plate)
        v = VehicleDAOImpl()
        selected_vehicle = v.getVehicleByPlate(vehicle_plate)
        #update vehicle id
        currentRide._vehicle_id = selected_vehicle.vehicle_id
        #=================================
        currentRide._pickup_location=self.pickupLocationEntry.get()
        currentRide._destination=self.destinationEntry.get()
        #currentRide._space_available=self.spaceAvailableEntry.get()
        currentRide._departure_date=self.departureDateEntry.get()
        currentRide._charge=self.chargeEntry.get()
        currentRide._description=self.descriptionText.get("1.0", tkinter.END)
        #update db with the new data
        rideDAO = RideDAOImpl()
        if rideDAO.update(currentRide):
            messagebox.showinfo("Informative", "Ride updated successfully")
            self.pwindow.updateFeedback()
            self.quit()
            self.destroy()
            #self.cancel()
        else:
            messagebox.showinfo("Informative", "Ride can't be updated, try again")

    def getRideInformation(self):
        r = RideDAOImpl()
        currentRide = r.getRideById(self.ride_id)
        if isinstance(currentRide, Ride):
            #set and show the ride info into the text fields
            self.pickupLocationEntry.insert(0, currentRide._pickup_location)
            self.destinationEntry.insert(0, currentRide._destination)
            self.spaceAvailableEntry.insert(0, currentRide._space_available)
            self.spaceAvailableEntry.configure(state='readonly')
            self.departureDateEntry.insert(0, currentRide._departure_date)
            self.chargeEntry.insert(0, currentRide._charge)
            self.descriptionText.insert(1.0, currentRide._description)




# ud = UserDAOImpl()
# u = ud.getUserById(25)
# up = UpdateRide(u, 32)
# up.mainloop()
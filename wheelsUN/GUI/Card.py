#implementar plantilla de visualizacion de viaje
import tkinter as tk
#
#from GUI.WindowHome import WindowHome
from tkinter import ttk, messagebox
from Data.RideDAOImpl import RideDAOImpl
from Data.UserDAOImpl import UserDAOImpl
from GUI.NewRide import NewRide
from GUI.UpdateRide import UpdateRide


class Card(tk.LabelFrame):
    dynamicRow = 1
    def __init__(self, master=None,pwindow=None, user_name=None, published=None, pickup_location=None,
                 destination=None, departure_date=None, charge=None, space_available=None, brand_vehicle = None,
                 color_vehicle = None, plate_vehicle = None, phone_number=None,description = None, match_user=None,
                 ride_id=None, user_id=None,**kw ):
        super().__init__(master, **kw)
        #card parameters
        Card.dynamicRow += 1
        #current row
        self.row = Card.dynamicRow
        #match users (if the ride creator is equal to the active_user)
        self.pwindow = pwindow
        self._match_user = match_user
        self.user_name=user_name
        self.published=published
        self.pickup_location = pickup_location
        self.destination = destination
        self.departure_date = departure_date
        self.charge = charge
        self.space_available = space_available
        self.vehicle_details = {'brand':brand_vehicle, 'color':color_vehicle, 'plate':plate_vehicle}
        self.phone_number = phone_number
        self.description = description
        self.ride_id=ride_id
        self.user_id = user_id
        #components
        self.components()


    # card creation
    def components(self):
        self.config(bg="black")
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)
        # location on home window
        self.grid(row=self.row, column=1, columnspan=4, sticky='NSWE', padx=150, pady=10)
        # card components
        # ====================seccion 1 creation========================
        seccion1 = tk.LabelFrame(self, text='ride organizer')
        seccion1.columnconfigure(0, weight=1)
        seccion1.columnconfigure(1, weight=1)
        # location on home window
        seccion1.grid(row=0, column=0, columnspan=2, sticky='NSWE')
        # seccion1 components
        # user name label
        user_name_label = tk.Label(seccion1, text=f'user: {self.user_name}')
        user_name_label.grid(row=0, column=0, sticky='W', padx=10)
        # published at label
        published_label = tk.Label(seccion1, text=f'published: {self.published}')
        published_label.grid(row=0, column=2, sticky='E', padx=10)
        # =================seccion 2 creation======================
        seccion2 = tk.LabelFrame(self, text='ride data')
        seccion2.columnconfigure(0, weight=1)
        seccion2.columnconfigure(1, weight=1)
        # location on home window
        seccion2.grid(row=1, column=0, columnspan=2, sticky='NSWE')
        # seccion2 components
        # pickup location
        pickup_location_label = tk.Label(seccion2, text=f'pickup location: {self.pickup_location}')
        pickup_location_label.grid(row=0, column=0, sticky='E', padx=50)
        # destination
        destination_label = tk.Label(seccion2, text=f'destination: {self.destination}')
        destination_label.grid(row=1, column=0, sticky='E', padx=50)
        # departureDate
        departure_date_label = tk.Label(seccion2, text=f'departure date: {self.departure_date}')
        departure_date_label.grid(row=2, column=0, sticky='E', padx=50)
        # charge
        charge_label = tk.Label(seccion2, text=f'charge: {self.charge}')
        charge_label.grid(row=0, column=1, sticky='W', padx=50)
        # space available
        space_available_label = tk.Label(seccion2, text=f'space available: {self.space_available}')
        space_available_label.grid(row=1, column=1, sticky='W', padx=50)
        # vehicle details
        vehicle_details_label = tk.Label(seccion2, text=f"vehicle details: {self.vehicle_details['brand']}, "
                                                        f"{self.vehicle_details['color']}, "
                                                        f"{self.vehicle_details['plate']}")
        vehicle_details_label.grid(row=2, column=1, sticky='W', padx=50)
        # contact
        phone_number_label = tk.Label(seccion2, text=f"contact me: {self.phone_number}")
        phone_number_label.grid(row=3, column=1, sticky='W', padx=50)
        # ====================seccion 3 creation========================
        seccion3 = tk.LabelFrame(self, text='description')
        seccion3.columnconfigure(0, weight=1)
        seccion3.columnconfigure(1, weight=1)
        # location on home window
        seccion3.grid(row=2, column=0, columnspan=2, sticky='NSWE')
        # description
        description_label = tk.Label(seccion3, text=self.description)
        description_label.grid(row=0, column=0, sticky='NSWE', columnspan=2, padx=10)
        # ====================seccion 4 creation========================
        #compare if the ride creator is equal to the active_user
        #if match user == true then there was a coincidence in the users
        if(self._match_user):
            seccion4 = tk.LabelFrame(self, text='acctions')
            seccion4.columnconfigure(0, weight=1)
            seccion4.columnconfigure(1, weight=1)
            # location on home window
            seccion4.grid(row=3, column=0, columnspan=2, sticky='NSWE')
            # crete components for labelFrame
            delete_btn = ttk.Button(seccion4, text='delete', command=self.delete_ride)
            delete_btn.grid(row=0, column=0, sticky='NSWE', padx=20)
            update_btn = ttk.Button(seccion4, text='update', command=self.update_ride)
            update_btn.grid(row=0, column=1, sticky='NSWE', padx=20)
        else:
            #if the user is already enrolled with the ride then the system allows him to exit
            r = RideDAOImpl()
            value = r.validateUserRides(self.user_id, self.ride_id)
            if value:
                seccion4 = tk.LabelFrame(self, text='acctions')
                seccion4.columnconfigure(0, weight=1)
                seccion4.columnconfigure(1, weight=1)
                # location on home window
                seccion4.grid(row=3, column=0, columnspan=2, sticky='NSWE')
                # crete components for labelFrame
                self.action_btn = ttk.Button(seccion4, text='exit ride', command=self.exit_ride)
                self.action_btn.grid(row=0, column=0, columnspan=2, sticky='NSWE', padx=100)
            #if the user is not in the ride, then he can join it
            else:
                seccion4 = tk.LabelFrame(self, text='acctions')
                seccion4.columnconfigure(0, weight=1)
                seccion4.columnconfigure(1, weight=1)
                # location on home window
                seccion4.grid(row=3, column=0, columnspan=2, sticky='NSWE')
                # crete components for labelFrame
                self.action_btn = ttk.Button(seccion4, text='join', command=self.join_ride)
                self.action_btn.grid(row=0, column=0, columnspan=2, sticky='NSWE', padx=100)

    def delete_ride(self):
        value = messagebox.askyesno(message="Do you wanna continue?", title="Delete ride")
        if value:
            #change the ride status in db
            r = RideDAOImpl()
            currentRide = r.getRideById(self.ride_id)
            r.delete(currentRide)
            #delete card in the home window
            self.destroy()

    def update_ride(self):
        userDAO = UserDAOImpl()
        active_user = userDAO.getUserById(self.user_id)
        n = UpdateRide(active_user, self.ride_id, self.pwindow)
        n.mainloop()

    def exit_ride(self):
        r = RideDAOImpl()
        if (r.exitRide(self.ride_id, self.user_id)):
            self.space_available += 1
            self.action_btn.config(text='join', command=self.join_ride)
            messagebox.showinfo("Info", "you have left the trip!")
            self.pwindow.updateFeedback()
        else:
            messagebox.showinfo("Info", "sorry, this ride is not available")

    def join_ride(self):
        r = RideDAOImpl()
        if (r.joinRide(self.ride_id, self.user_id)):
            self.space_available -= 1
            self.action_btn.config(text='exit ride', command=self.exit_ride)
            messagebox.showinfo("Info", "you have joined the ride!")
            self.pwindow.updateFeedback()
        else:
            messagebox.showinfo("Info", "sorry, this ride is not available or you are already inside")

# if __name__ == '__main__':
#     w = WindowHome()
#     c = Card(w, 'Fiu', '06/05/2023 14:37', 'Santa Rosita', 'Universidad Nal', '07/05/2023 10:00', '3500 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '', 'descripcion...')
#     c2 = Card(w, 'Fiu', '06/05/2023 14:37', 'Suba', 'Engativa', '07/05/2023 10:00', '2000 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '', 'descripcion...')
#     c3 = Card(w, 'Fiu', '06/05/2023 14:37', 'Kennedy', 'Rosales', '07/05/2023 10:00', '4500 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '3223877590', 'descripcion...')
#     w.mainloop()

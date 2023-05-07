#implementar plantilla de visualizacion de viaje
import tkinter as tk
#
#from GUI.WindowHome import WindowHome


class Card(tk.LabelFrame):
    dynamicRow = 1
    def __init__(self, master=None, user_name=None, published=None, pickup_location=None,
                 destination=None, departure_date=None, charge=None, space_available=None, brand_vehicle = None,
                 color_vehicle = None, plate_vehicle = None, phone_number=None,description = None, **kw ):
        super().__init__(master, **kw)
        #card parameters
        Card.dynamicRow += 1
        #current row
        self.row = Card.dynamicRow
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


# if __name__ == '__main__':
#     w = WindowHome()
#     c = Card(w, 'Fiu', '06/05/2023 14:37', 'Santa Rosita', 'Universidad Nal', '07/05/2023 10:00', '3500 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '', 'descripcion...')
#     c2 = Card(w, 'Fiu', '06/05/2023 14:37', 'Suba', 'Engativa', '07/05/2023 10:00', '2000 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '', 'descripcion...')
#     c3 = Card(w, 'Fiu', '06/05/2023 14:37', 'Kennedy', 'Rosales', '07/05/2023 10:00', '4500 COP', '5', 'nissan',
#              'Verde', 'FGR-443', '3223877590', 'descripcion...')
#     w.mainloop()

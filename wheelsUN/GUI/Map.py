import tkinter as tk
from tkinter import ttk

import tkintermapview

class Map():

    def __init__(self, organizator_name, departure_date, pickup_location, destination):
        self._organizator_name = organizator_name
        self._departure_date = departure_date
        self._pickup_location = pickup_location
        self._destination = destination
        #add all the elements to the window
        self.components()

    def components(self):

        # create map widget
        #map_widget = tkintermapview.TkinterMapView(self.ventana_actual, width=500, height=400, corner_radius=0)
        #map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        #map_widget.grid(row=0, column=1, sticky='E', padx=10)
        #map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #create window in order to show the map
        window_map = tk.Toplevel()

        # basic config
        width_window = 715
        heignt_window = 415
        x = window_map.winfo_screenwidth() // 2 - width_window // 2
        y = window_map.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y - 50)
        window_map.geometry(position)
        # title
        window_map.title('Visualize the path')
        # self.iconbitmap(windowIcon)
        window_map.resizable(False, False)
        # 1. grid configuration
        window_map.columnconfigure(0, weight=10)
        window_map.columnconfigure(1, weight=10)

        # information about the ride
        seccion1 = tk.LabelFrame(window_map, text='ride details')
        #seccion1.columnconfigure(0, weight=1)
        #seccion1.columnconfigure(1, weight=1)
        # location on home window
        seccion1.grid(row=0, column=0, sticky='NSWE')
        # seccion1 components
        # organizer name label
        organizer_name_label = tk.Label(seccion1, text=f'organizer name: {self._organizator_name}')
        organizer_name_label.grid(row=0, sticky='W', pady=10)
        # departure date label
        departure_date_label = tk.Label(seccion1, text=f'departure date: {self._departure_date}')
        departure_date_label.grid(row=1, sticky='W', pady=10)
        # pickup location label
        pickup_location_label = tk.Label(seccion1, text=f'pickup location: {self._pickup_location}')
        pickup_location_label.grid(row=2, sticky='W', pady=10)
        # destination label
        destination_label = tk.Label(seccion1, text=f'destination: {self._destination}')
        destination_label.grid(row=3, sticky='W', pady=10)


        #map configuration
        #create widget for the map
        map_widget = tkintermapview.TkinterMapView(window_map, width=500, height=380, corner_radius=0)
        #set google maps
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        #set a default position
        # set current widget position and zoom
        map_widget.set_position(4.7000515, -74.0846337)  # Paris, France
        #map_widget.set_zoom(8)

        try:
            # configure the path
            # set current widget position by address
            marker_1 = map_widget.set_address(f"{self._pickup_location}", marker=True)
            marker_2 = map_widget.set_address(f"{self._destination}", marker=True)
            marker_1.set_text(f"{self._pickup_location}")  # set new text
            marker_2.set_text(f"{self._destination}")  # set new text
            # set a path
            #map_widget.set_path([marker_1.position, marker_2.position])
            # set a polygon
            #map_widget.set_polygon([marker_1.position, marker_2.position])
        except Exception as e:
            print("locations not available",e)

        # try:
        #     # set the specified points into the map
        #     map_widget.fit_bounding_box((marker_1.position), (marker_2.position))
        # except Exception as e:
        #     print("fit bounding failed", e)

        # locate the map on the window
        map_widget.grid(row=0, column=1, sticky='E', padx=5, pady=5)
        #map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #close btn
        close_btn = ttk.Button(window_map, text='close', command=window_map.destroy)
        close_btn.grid(row=1, sticky='NSWE', padx=10)

if __name__ == "__main__":

    m = Map()
    #m.mainloop()

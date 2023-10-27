import datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from BusinessLogic.DownloadFile import DownloadFile
from BusinessLogic.GenerateReport import GenerateReport
from Data.Ride import Ride
from Data.RideDAOImpl import RideDAOImpl
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from Data.Vehicle import Vehicle
from Data.VehicleDAOImpl import VehicleDAOImpl


class NewReport(tk.Tk):

    def __init__(self, active_user: User):
        super().__init__()
        #initialize active user
        self.active_user = active_user
        # basic config
        width_window = 800
        heignt_window = 515
        x = self.winfo_screenwidth() // 2 - width_window // 2
        y = self.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y - 50)
        self.geometry(position)
        #title
        self.title('Report')
        #self.iconbitmap(windowIcon)
        self.resizable(False,False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)

        self.components()



    def components(self):

        appName = tk.Label(self, text='Wheels UN')
        appName.grid(row=0, column=0, sticky='W')

        labelText = tk.Label(self, text='Generate new report')
        labelText.grid(row=1, column=0, sticky='NSWE', columnspan=2)

        #label
        startDateLabel = tk.Label(self, text='start date (aaaa/mm/dd hh:mm:ss): ')
        startDateLabel.grid(row=2, column=0, sticky='E')
        #text field
        self.startDateEntry = tk.Entry(self, width=30)
        self.startDateEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

        # label
        endDateLabel = tk.Label(self, text='end date (aaaa/mm/dd hh:mm:ss): ')
        endDateLabel.grid(row=3, column=0, sticky='E')
        # text field
        self.endDateEntry = tk.Entry(self, width=30)
        self.endDateEntry.grid(row=3, column=1, sticky='W', padx=10, pady=15)

        # label
        listLabel = tk.Label(self, text='Select a report type: ')
        listLabel.grid(row=4, column=0, sticky='E')

        # Crea la lista desplegable
        options = ["created trips", "trips I have joined"]
        # default option
        self.selected_option = tk.StringVar(self, value='select an option')
        list = ttk.Combobox(self, textvariable=self.selected_option, values=options,
                                    state="readonly")
        list.grid(row=4, column=1, sticky='W', padx=5, pady=15)

        #actions
        btnCreate = ttk.Button(self, text='Generate report', command=self.makeReport)
        # especify cell's coordinates
        btnCreate.grid(row=11, column=0, sticky='NSWE', padx=20, pady= 10)

        btnCancel = ttk.Button(self, text='Cancel', command=self.cancel)
        # especify cell's coordinates
        btnCancel.grid(row=11, column=1, sticky='NSWE', padx=50, pady= 10)

    def makeReport(self):

        #get the values for the report
        reporType = self.selected_option.get()
        startDate = self.startDateEntry.get()
        endDate = self.endDateEntry.get()
        #validate data
        if (reporType != 'select an option' and startDate != '' and endDate != ''):

            # create an object GenerateReport(activeUser, startDate, endDate, reportType)
            r = GenerateReport(self.active_user, startDate, endDate, reporType)

            #invoke method "make" which generate the respective report if the user has data
            #data is a list with tuples, every tuple is a ride
            data = r.getData()
            if data == 0:
                #self.cancel()
                #clear the text fields
                self.startDateEntry.delete(0, tk.END)
                self.endDateEntry.delete(0, tk.END)
                self.selected_option.set('select a report type')
                # failed ride creation
                messagebox.showinfo("Warning", "Failed to generate report, try again")
            else:
                #if the user has data to report, then generate file and then dowmload
                #makeTable and return the list of rides
                rideRecordList = self.makeTable(data)

                #create a dowmload button
                btnDownload = ttk.Button(self, text='Download report', command=lambda: self.downloadReport(rideRecordList))
                btnDownload.grid(row=0, column=1, sticky='E')

                # clear the text fields
                self.startDateEntry.delete(0, tk.END)
                self.endDateEntry.delete(0, tk.END)
                self.selected_option.set('select a report type')

                #successful ride creation
                messagebox.showinfo("Informative", "report generated successfully")
        else:
            messagebox.showinfo("Warning", "Failed to generate report, try again")

    def downloadReport(self, rideRecordList):
        from datetime import datetime

        #ask for destination directory
        destinationDirectory = filedialog.askdirectory()
        #generate the file's name
        currentDate = datetime.now()

        nameFile= "report_"+ str(currentDate.year) + str(currentDate.month) + str(currentDate.day)
        #create object and pass arguments
        d = DownloadFile(nameFile,destinationDirectory, rideRecordList)
        d.makeFile()



    def makeTable(self, data):
        # Crear un objeto Canvas que contenga el widget que queremos desplazar
        self.canvas = tk.Canvas(self)
        #self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.grid(row=12, columnspan=2, sticky="nsew")

        # Crear un objeto Frame dentro del Canvas y agregar varios widgets al Frame

        # Crear un marco para la tabla
        self.tabla_frame = tk.Frame(self.canvas)
        self.tabla_frame.grid(row=12, columnspan=2, sticky="nsew")

        # Configurar la barra de desplazamiento vertical
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.grid(row=12, column=7, sticky="ns" )

        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        #canvas.config(yscrollcommand=scrollbar.set)
        # Agregar el objeto Frame al Canvas
        self.canvas.create_window((0, 0), window=self.tabla_frame, anchor="nw")
        # Ajustar el tamaño del Canvas para que se adapte al contenido
        self.tabla_frame.update_idletasks()
        # Configurar desplazamiento con el mouse en el lienzo
        self.canvas.bind_all("<MouseWheel>",
                              lambda event: self.canvas.yview_scroll(-1 * (event.delta // 120), "units"))
        self.canvas.bind_all("<Shift-MouseWheel>",
                              lambda event: self.canvas.xview_scroll(-1 * (event.delta // 120), "units"))

        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # table data
        rides = [
            ["Organizer", "Published at", "Pickup location", "Destination", "Departure date", "Charge",
             "vehicle_details"]
        ]

        def makeRecords(data, rides):
            for record in data:
                #clean variables
                ride_record = []
                self.organizer = ""
                #self.published_at
                self.pickupLocation = ""
                self.destination = ""
                #self.departureDate
                self.charge = ""
                self.vehicle_details = ""

                #get the organizer name
                creator_id = record[1]
                u = UserDAOImpl()
                creator = u.getUserById(creator_id)
                if isinstance(creator, User):
                    self.organizer = creator.user_name
                    ride_record.append(self.organizer)


                #get published date
                self.published_at = record[2]
                ride_record.append(self.published_at)
                #get pickupLocation
                self.pickupLocation = record[5]
                ride_record.append(self.pickupLocation)
                #get destination
                self.destination = record[6]
                ride_record.append(self.destination)
                #get departure date
                self.departureDate = record[8]
                ride_record.append(self.departureDate)
                #get charge
                self.charge = record[9]
                ride_record.append(self.charge)

                #get vehicle details
                vehicle_id = record[10]
                v = VehicleDAOImpl()
                vehicle = v.getVehicleById(vehicle_id)
                if isinstance(vehicle, Vehicle):
                    self.vehicle_details = f"{vehicle.brand}, {vehicle.color}, {vehicle.vehicle_plate}"
                    ride_record.append(self.vehicle_details)

                #append the generated record to the general list
                rides.append(ride_record)

        #fill the table rides with the data
        makeRecords(data, rides)

        # Encabezados de columna labels
        for col, encabezado in enumerate(rides[0]):
            etiqueta = tk.Label(self.tabla_frame, text=encabezado, relief=tk.RIDGE)
            etiqueta.grid(row=0, column=col, sticky="nsew")

        # Datos de la tabla labels
        for fila, fila_datos in enumerate(rides[1:], start=1):
            for col, dato in enumerate(fila_datos):
                etiqueta = tk.Label(self.tabla_frame, text=dato, relief=tk.RIDGE)
                etiqueta.grid(row=fila, column=col, sticky="nsew")

        # Configuración para que las celdas se ajusten al contenido
        for i in range(4):
            self.tabla_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.tabla_frame.grid_rowconfigure(i, weight=1)

        #return list of rides
        return rides

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
    w = NewReport(user)
    w.mainloop()
import tkinter as tk
import tkinter.filedialog as filedialog
import tempfile
import webbrowser
import os

class DownloadFile():

    def __init__(self, nameFile, destinationDirectory,rideRecordList):
        self.nameFile = nameFile
        self.destinationDirectory = destinationDirectory
        self.rideRecordList = rideRecordList


    def makeFile(self):

        # Crea un archivo temporal en la carpeta especificada
        file = os.path.join(self.destinationDirectory, self.nameFile)
        with open(file, 'w') as temp_file:
            for record in self.rideRecordList:
                for value in record:
                    temp_file.write(f"{str(value)} ")
                temp_file.write("\n")

        # Abre el archivo temporal en el visor de texto predeterminado
        webbrowser.open(file)



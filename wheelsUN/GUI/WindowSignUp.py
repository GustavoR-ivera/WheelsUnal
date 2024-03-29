import tkinter as tk
from tkinter import ttk, messagebox

from BusinessLogic.SignUp import SignUp
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl
from GUI.WindowHome import WindowHome


class WindowSignUp(tk.Tk):
    def __init__(self):
        super().__init__()
        # basic config
        width_window = 500
        heignt_window = 500
        x = self.winfo_screenwidth() // 2 - width_window // 2
        y = self.winfo_screenheight() // 2 - heignt_window // 2
        position = str(width_window) + "x" + str(heignt_window) + "+" + str(x) + "+" + str(y - 50)
        self.geometry(position)
        #title
        self.title('Sign Up')
        #self.iconbitmap(windowIcon)
        self.resizable(False,False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)
        self.components()

    def components(self):
        appName = tk.Label(self, text='Wheels UN')
        appName.grid(row=0, column=0, sticky='NSWE', columnspan=2)

        loginText = tk.Label(self, text='Sign Up')
        loginText.grid(row=1, column=0, sticky='NSWE', columnspan=2)

        #label username
        userNameLabel = tk.Label(self, text='Name: ')
        userNameLabel.grid(row=2, column=0, sticky='E')
        #text field username
        self.userNameEntry = tk.Entry(self, width=30)
        self.userNameEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

        #label email user
        emailLabel = tk.Label(self, text='Email: ')
        emailLabel.grid(row=3, column=0, sticky='E')
        #text field email
        self.emailEntry = tk.Entry(self, width=30)
        self.emailEntry.grid(row=3, column=1, sticky='W', padx= 10, pady=15)

        # label country user
        countryLabel = tk.Label(self, text='Country: ')
        countryLabel.grid(row=4, column=0, sticky='E')
        # text field country
        self.countryEntry = tk.Entry(self, width=30)
        self.countryEntry.grid(row=4, column=1, sticky='W', padx=10, pady=15)

        # label dni type user
        dniTypeLabel = tk.Label(self, text='DNI type: ')
        dniTypeLabel.grid(row=5, column=0, sticky='E')
        # text field DNI type
        self.dniTypeEntry = tk.Entry(self, width=30)
        self.dniTypeEntry.grid(row=5, column=1, sticky='W', padx=10, pady=15)

        # label dni number
        dniNumberLabel = tk.Label(self, text='DNI number: ')
        dniNumberLabel.grid(row=6, column=0, sticky='E')
        # text field DNI number
        self.dniNumberEntry = tk.Entry(self, width=30)
        self.dniNumberEntry.grid(row=6, column=1, sticky='W', padx=10, pady=15)

        # label phone number
        phoneNumberLabel = tk.Label(self, text='Phone number: ')
        phoneNumberLabel.grid(row=7, column=0, sticky='E')
        # text field phone number
        self.phoneNumberEntry = tk.Entry(self, width=30)
        self.phoneNumberEntry.grid(row=7, column=1, sticky='W', padx=10, pady=15)

        # label driving license
        drivingLicenseLabel = tk.Label(self, text='Driving license: ')
        drivingLicenseLabel.grid(row=8, column=0, sticky='E')
        # text driving license
        self.drivingLicenseEntry = tk.Entry(self, width=30)
        self.drivingLicenseEntry.grid(row=8, column=1, sticky='W', padx=10, pady=15)

        #label password
        passLabel = tk.Label(self, text='Password: ')
        passLabel.grid(row=9, column=0, sticky='E')
        # campo de texto pass
        self.passEntry = tk.Entry(self, width=30, show='*')
        self.passEntry.grid(row=9, column=1, sticky='W', padx= 10, pady=15)

        btnSignup = ttk.Button(self, text='Sign Up', command=self.signUp)
        # especify cell's coordinates
        btnSignup.grid(row=10, column=0, sticky='NSWE', columnspan=2, padx=90, pady= 10)


    def signUp(self):
        # create sign up object and capture data from the form fields
        s = SignUp(self.userNameEntry.get(),self.passEntry.get(), self.countryEntry.get(),
                   self.dniTypeEntry.get(),self.dniNumberEntry.get(), self.emailEntry.get(),
                   self.phoneNumberEntry.get(), self.drivingLicenseEntry.get())

        if s.register():
            # informative message
            messagebox.showinfo('informative', 'Successful registration')
            # redirect to home window
            u = UserDAOImpl()
            userRegistered = u.getUserByDni(self.dniNumberEntry.get())
            self.destroy()
            w = WindowHome(userRegistered)
            w.mainloop()

        else:
            # delete text field content
            self.emailEntry.delete(0, tk.END)
            self.passEntry.delete(0, tk.END)
            self.drivingLicenseEntry.delete(0, tk.END)
            self.dniNumberEntry.delete(0, tk.END)
            self.dniTypeEntry.delete(0, tk.END)
            self.countryEntry.delete(0, tk.END)
            self.userNameEntry.delete(0, tk.END)
            self.phoneNumberEntry.delete(0, tk.END)
            messagebox.showwarning('warning', 'Please fill in all fields')


if __name__ == '__main__':
    w = WindowSignUp()
    w.mainloop()
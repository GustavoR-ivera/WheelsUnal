import tkinter as tk
from tkinter import ttk, messagebox
import WindowLogin


class WindowSignUp(tk.Tk):
    def __init__(self):
        super().__init__()
        # basic config
        self.geometry('600x600')
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

        #label password
        passLabel = tk.Label(self, text='Password: ')
        passLabel.grid(row=7, column=0, sticky='E')
        # campo de texto pass
        self.passEntry = tk.Entry(self, width=30, show='*')
        self.passEntry.grid(row=7, column=1, sticky='W', padx= 10)

        btnSignup = ttk.Button(self, text='Sign Up', command=self.signUp)
        # especify cell's coordinates
        btnSignup.grid(row=8, column=0, sticky='NSWE', columnspan=2, padx=90, pady= 10)


    def signUp(self):
        print(f'user: {self.emailEntry.get()}, password: {self.passEntry.get()}')
        # delete text field content
        self.emailEntry.delete(0, tk.END)
        self.passEntry.delete(0, tk.END)

    # def signUp(self):
    #     #messagebox.showinfo('informative', 'informativo')
    #     #messagebox.showerror('error', 'error')
    #     #messagebox.showwarning('warning', 'warning')
    #     #crear ventana de registro y mostrar
    #     #w = WindowLogin('600x900', 'newWindow')
    #     w = WindowSignUp()
    #     w.mainloop()
    #     #self.destroy()

if __name__ == '__main__':
    w = WindowSignUp()
    w.mainloop()
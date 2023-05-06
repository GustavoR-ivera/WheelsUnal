import tkinter as tk
from tkinter import ttk, messagebox

from Data.PoolCursor import PoolCursor
from GUI.WindowHome import WindowHome
from GUI.WindowSignUp import WindowSignUp


class WindowLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        # basic config
        self.geometry('370x300')
        self.title('Login')
        #self.iconbitmap(windowIcon)
        self.resizable(False,False)
        # 1. grid configuration
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=10)
        self.components()

    def components(self):
        appName = tk.Label(self, text='Wheels UN')
        appName.grid(row=0, column=0, sticky='NSWE', columnspan=2)

        loginText = tk.Label(self, text='Log in')
        loginText.grid(row=1, column=0, sticky='NSWE', columnspan=2)

        #label user
        emailLabel = tk.Label(self, text='Email: ')
        emailLabel.grid(row=2, column=0, sticky='E')
        #campo de texto email
        self.emailEntry = tk.Entry(self, width=30)
        self.emailEntry.grid(row=2, column=1, sticky='W', padx= 10, pady=15)

        #label password
        passLabel = tk.Label(self, text='Password: ')
        passLabel.grid(row=3, column=0, sticky='E')
        # campo de texto pass
        self.passEntry = tk.Entry(self, width=30, show='*')
        self.passEntry.grid(row=3, column=1, sticky='W', padx= 10)

        btnEnter = ttk.Button(self, text='Enter', command=self.login)
        # especify cell's coordinates
        btnEnter.grid(row=4, column=0, sticky='NSWE', columnspan=2, padx=90, pady= 10)

        btnSignUp = ttk.Button(self, text='Sign up', command=self.signUp)
        btnSignUp.grid(row=5, column=0, sticky='NSWE', columnspan=2, padx=90)

    def login(self):
        try:
            with PoolCursor() as cursor:
                query = f"select * from test_users " \
                        f"where email = '{self.emailEntry.get()}' and password = '{self.passEntry.get()}' "
                cursor.execute(query)
                record = cursor.fetchone()
                if record:
                    self.destroy()
                    # if exist a record in the db then allows the access to the user
                    w = WindowHome()
                    w.mainloop()
                else:
                    messagebox.showinfo('error', 'No user was found')
                    # delete text field content
                    self.emailEntry.delete(0, tk.END)
                    self.passEntry.delete(0, tk.END)
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def signUp(self):
        # remove current window login
        self.destroy()
        # show window sign up
        w = WindowSignUp()
        w.mainloop()


if __name__ == '__main__':
    w = WindowLogin()
    w.mainloop()
from tkinter import messagebox
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl


class SignUp:
    def __init__(self, user_name, password, country, dni_type, dni_number, email, phoneNumber, drivingLicense):
        self._user_name = user_name
        self._password = password
        self._country = country
        self._dni_type = dni_type
        self._dni_number = dni_number
        self._email = email
        self._phoneNumber = phoneNumber
        self._drivingLicense = drivingLicense
    # getters
    @property
    def user_name(self):
        return self._user_name
    @property
    def password(self):
        return self._password
    @property
    def country(self):
        return self._country
    @property
    def dni_type(self):
        return self._dni_type
    @property
    def dni_number(self):
        return self._dni_number
    @property
    def email(self):
        return self._email
    @property
    def phoneNumber(self):
        return self._phoneNumber
    @property
    def drivingLicense(self):
        return self._drivingLicense

    def register(self):
        # empty fields validation
        if(self.user_name == '' or self.password == '' or self.dni_type == '' or self.dni_number == '' or self.email == ''):
            return 0
        else:
            try:
                userDAO = UserDAOImpl()
                user = User(user_name=self.user_name, password=self.password, country=self.country,
                            dni_type=self.dni_type, dni_number=self.dni_number, email=self.email,
                            phoneNumber= self.phoneNumber, drivingLicense=self.drivingLicense )
                userDAO.insert(user)

                return 1
            except Exception as e:
                messagebox.showerror('error', f'An exception has ocurred {e}')

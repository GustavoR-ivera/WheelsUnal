from datetime import datetime


class User:

    #constructor
    def __init__(self, user_id=None, user_name=None, password=None, user_status=1,
                 country=None, dni_type=None, dni_number=None, email=None, lastLogin=datetime.now(),
                 phoneNumber=None, deleted=0, created_at=datetime.now(), updated_at=datetime.now(),
                 deleted_at=None, drivingLicense=None, rol='Generic'):
        # user attributes
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._user_status = user_status
        self._country = country
        self._dni_type = dni_type
        self._dni_number = dni_number
        self._email = email
        #date lastlogin aaaa/mm/dd hh:mm:ss
        self._lastLogin = lastLogin
        self._phoneNumber = phoneNumber
        #deleted True/False
        self._deleted = deleted
        # register dates
        self._created_at = created_at
        self._updated_at = updated_at
        self._deleted_at = deleted_at
        #driving licence's data
        self._drivingLicense = drivingLicense
        self._rol = rol

    #getters setters
    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password

    @property
    def user_status(self):
        return self._user_status
    @user_status.setter
    def user_status(self, user_status):
        self._user_status = user_status

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country

    @property
    def dni_type(self):
        return self._dni_type
    @dni_type.setter
    def dni_type(self, dni_type):
        self._dni_type = dni_type

    @property
    def dni_number(self):
        return self._dni_number
    @dni_number.setter
    def dni_number(self, dni_number):
        self._dni_number = dni_number

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def lastLogin(self):
        return self._lastLogin
    @lastLogin.setter
    def lastLogin(self, lastLogin):
        self._lastLogin = lastLogin

    @property
    def phoneNumber(self):
        return self._phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    @property
    def deleted(self):
        return self._deleted
    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

    @property
    def created_at(self):
        return self._created_at
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at
    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @property
    def deleted_at(self):
        return self._deleted_at
    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at

    @property
    def drivingLicense(self):
        return self._drivingLicense
    @drivingLicense.setter
    def drivingLicence(self, drivingLicense):
        self._drivingLicense = drivingLicense

    @property
    def rol(self):
        return self._rol
    @rol.setter
    def rol(self, rol):
        self._rol = rol

    # toString
    def __str__(self):
        return f'User ' \
               f'user_id:{self.user_id}, ' \
               f'user_name:{self.user_name}, ' \
               f'user_status:{self.user_status}, ' \
               f'country:{self.country}, ' \
               f'dni_type:{self.dni_type}, ' \
               f'dni_number:{self.dni_number}, ' \
               f'rol: {self.rol}'

if __name__ == "__main__":
    u = User(user_status=0, user_name='pergolichi', user_id=15, password='yUihe5',country='Colombia',
             dni_type='Cedula de ciudadania', dni_number='1014307953', email='loquesea@mail.com',
             phoneNumber='3223877590', rol='admin', created_at='2023/05/05 17:59:00')
    print(u)
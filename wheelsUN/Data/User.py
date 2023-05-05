
class User:

    #constructor
    def __init__(self, user_id=None, user_name=None, password=None, user_status=None,
                 country=None, dni_type=None, dni_number=None):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._user_status = user_status
        self._country = country
        self._dni_type = dni_type
        self._dni_number = dni_number
        #///

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

    # toString
    def __str__(self):
        return f'User ' \
               f'user_id:{self.user_id}, ' \
               f'user_name:{self.user_name}, ' \
               f'password:{self.password}, ' \
               f'user_status:{self.user_status}, ' \
               f'country:{self.country}, ' \
               f'dni_type:{self.dni_type}, ' \
               f'dni_number:{self.dni_number}'

if __name__ == "__main__":
    u = User(user_status=0, user_name='pergolichi', user_id=15, password='yUihe5',country='Colombia',
             dni_type='Cedula de ciudadania', dni_number='1014307953')
    print(u)
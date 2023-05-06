from Data.UserDAOImpl import UserDAOImpl


class LogIn:
    def __init__(self, email, password):
        self._email = email
        self._password = password

    #getters setters
    @property
    def email(self):
        return self._email
    @property
    def password(self):
        return self._password

    def access(self):
        userDAO = UserDAOImpl()
        return userDAO.loginValidation(self.email, self.password)

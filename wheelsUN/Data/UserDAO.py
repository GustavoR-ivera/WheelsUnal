from abc import *


# standard interface with crud operations
class UserDAO(ABC):

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def update(self, id_object):
        pass

    @abstractmethod
    def delete(self, id_object):
        pass

    @abstractmethod
    def select(self):
        pass

    #///

    @abstractmethod
    def getUsersByStatus(self, status: bool):
        # return a user list with the user status specified
        pass

    @abstractmethod
    def getUserById(self, user_id):
        # return a user with the user id specified
        pass

    @abstractmethod
    def getUserByDni(self, dni_number):
        # return a user with the user dni specified
        pass

    @abstractmethod
    def loginValidation(self, email, password):
        # return a user with the specified data
        pass
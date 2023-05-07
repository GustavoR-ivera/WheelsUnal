from abc import *

# standard interface with crud operations
class RideDAO(ABC):

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
    def getRidesByStatus(self, status: bool):
        # return a user list with the user status specified
        pass

    @abstractmethod
    def getRideById(self, ride_id):
        # return a user with the user id specified
        pass

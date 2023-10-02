from abc import *
# standard interface with crud operations

class RideEventRegisterDAO(ABC):

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def select(self):
        pass

    #///

    @abstractmethod
    def getEventRegisterByUser(self, user_id):
        # return a user list with the user status specified
        pass

    @abstractmethod
    def getEventRegisterByRide(self, ride_id):
        # return a user with the user id specified
        pass

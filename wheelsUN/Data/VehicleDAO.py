from abc import *

# standard interface with crud operations
class VehicleDAO(ABC):

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
    def getVehicleById(self, vehicle_id):
        # return a vehicle with the id specified
        pass

    @abstractmethod
    def getVehicleByPlate(self, vehicle_plate):
        # return a vehicle with the plate specified
        pass

    @abstractmethod
    def getVehiclesByOwnerId(self, owner_id):
        # return a list vehicles for the owner id specified
        pass

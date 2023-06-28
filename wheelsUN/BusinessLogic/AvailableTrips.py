from Data.RideDAOImpl import RideDAOImpl


class AvailableTrips:

    def fetchall(self):
        rideDAO = RideDAOImpl()
        #update rides
        rideDAO.updateTrips()
        #returns all available rides
        return rideDAO.getRidesByStatus(1)
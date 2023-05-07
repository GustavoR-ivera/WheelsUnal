from Data.RideDAOImpl import RideDAOImpl


class AvailableTrips:

    def fetchall(self):
        rideDAO = RideDAOImpl()
        return rideDAO.getRidesByStatus(1)
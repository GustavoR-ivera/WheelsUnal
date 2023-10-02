from datetime import datetime
from Data.PoolCursor import PoolCursor
from Data.Ride import Ride
from Data.RideDAO import RideDAO


class RideDAOImpl(RideDAO):

    def validateUserRides(self,user_id,ride_id):
        try:
            with PoolCursor() as cursor:
                query = f"select * from user_rides where user_id = {user_id} and ride_id={ride_id}"
                cursor.execute(query)
                record = cursor.fetchall()
                if record:
                    # the user currently is vinculated with the ride
                    return 1
                else:
                    return 0
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def joinRide(self,ride_id, user_id):
        #
        try:
            with PoolCursor() as cursor:
                self.updateTrips()
                query = f"select ride_available from rides where ride_id = {ride_id}"
                cursor.execute(query)
                record = cursor.fetchone()
                query2 = f"select * from user_rides where user_id = {user_id} and ride_id={ride_id}"
                cursor.execute(query2)
                record2 = cursor.fetchall()
                if record[0]==0 or len(record2)!=0:
                    # ride is not available or the user currently is vinculated with the ride
                    return 0
                else:
                    # means the ride is available
                    query = f"update rides set space_available = space_available - 1 where ride_id = {ride_id}"
                    cursor.execute(query)
                    query = f"insert into user_rides (user_id, ride_id) values ({user_id}, {ride_id})"
                    cursor.execute(query)
                    self.updateTrips()
                    return 1
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def exitRide(self,ride_id, user_id):
        #
        try:
            with PoolCursor() as cursor:
                #update the trips
                self.updateTrips()
                #consult it the ride is available
                query = f"select ride_available from rides where ride_id = {ride_id}"
                cursor.execute(query)
                record = cursor.fetchone()
                if record[0]==1:
                    # means the ride is available
                    query = f"update rides set space_available = space_available + 1 where ride_id = {ride_id}"
                    cursor.execute(query)
                    query = f"delete from user_rides where user_id = {user_id} and ride_id = {ride_id} "
                    cursor.execute(query)
                    self.updateTrips()
                    return 1
                else:
                    return 0

        except Exception as e:
            print(f'An exception has occurred: {e}')


    def updateTrips(self):
        #return a user list with the user status specified
        try:
            with PoolCursor() as cursor:
                #space available == 0 and departure date < current date
                query = f"update rides " \
                        f"set ride_available = 0 " \
                        f"WHERE space_available = 0 or departure_date < current_timestamp"
                cursor.execute(query)
                #print(f'records: {cursor.rowcount}')
                #print(records)
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def getRidesByStatus(self, status):
        #return a user list with the user status specified
        try:
            with PoolCursor() as cursor:
                rides = []
                query = f"SELECT * " \
                        f"FROM rides " \
                        f"WHERE ride_available = '{status}' " \
                        f"order by created_at desc "
                cursor.execute(query)
                records = cursor.fetchall()
                #print(f'records: {cursor.rowcount}')
                #print(records)
                for i in records:
                    r = Ride(int(i[0]),int(i[1]),i[2],i[3],i[4],i[5],i[6],int(i[7]),i[8],i[9],int(i[10]),int(i[11]),i[12])
                    rides.append(r)
                return rides
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getRideById(self, ride_id):
        #return a user with the user_id specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM rides " \
                        f"WHERE ride_id = '{ride_id}' "
                cursor.execute(query)
                record = cursor.fetchone()
            # if record variable is not empty then it creates a ride object and then it returns it
            if record:
                ride = Ride(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],
                            record[9],record[10],record[11],record[12])
                return ride
            # if record variable is empty then it returns 0/false
            else:
                return None
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getLastRideCreatedByUser(self, user):
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM rides " \
                        f"WHERE creator_id = '{user.user_id}' " \
                        f"ORDER BY updated_at DESC"
                cursor.execute(query)
                #ONLY CAPTURE THE FIRTS RECORD
                record = cursor.fetchone()
            # if record variable is not empty then it creates a ride object and then it returns it
            if record:
                ride = Ride(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[8],
                            record[9], record[10], record[11], record[12])
                return ride
            # if record variable is empty then it returns 0/false
            else:
                return None
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def insert(self, ride):
        try:
            with PoolCursor() as cursor:
                query = f"insert into rides (creator_id, created_at, updated_at, " \
                        f"pickup_location, destination, space_available, departure_date, charge, vehicle_id, " \
                        f"ride_available, description) " \
                        f"values ({ride._creator_id},'{ride._created_at}','{ride._updated_at}'," \
                        f"'{ride._pickup_location}','{ride._destination}',{ride._space_available}, " \
                        f"'{ride._departure_date}','{ride._charge}', {ride._vehicle_id}, {ride._ride_available}," \
                        f"'{ride._description}' )"
                cursor.execute(query)
                return cursor.rowcount
                #print(f'inserted records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def select(self):
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * FROM rides"
                cursor.execute(query)
                records = cursor.fetchall()
                print(f'records: {cursor.rowcount}')
                print(f'rides: {records}')
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def delete(self, ride):
        try:
            with PoolCursor() as cursor:
                query = f"update rides " \
                        f"set ride_available = 0, deleted_at = '{datetime.now()}'  " \
                        f"where ride_id = {ride._ride_id} "
                cursor.execute(query)
                # returns the affected rows
                return cursor.rowcount
                #print(f'deleted records: {cursor.rowcount}')

        except Exception as e:
            print(f'An exception has occurred: {e}')

    def update(self, ride):
        pass
        try:
            with PoolCursor() as cursor:
                query = f"update rides " \
                        f"set pickup_location = '{ride._pickup_location}', destination = '{ride._destination}', " \
                        f"departure_date = '{ride._departure_date}', charge = '{ride._charge}', " \
                        f"vehicle_id = {ride._vehicle_id}, description = '{ride._description}'" \
                        f"where ride_id = {ride._ride_id} "
                cursor.execute(query)
                return cursor.rowcount
        except Exception as e:
            print(f'An exception has occurred: {e}')


if __name__ == "__main__":
    pass
    # r = Ride(creator_id=25, pickup_location='Parque simon bolivar', destination='Martires', space_available=5,
    #          departure_date='2023-05-08 07:00', charge='7500 COP', vehicle_id=1, description='llegar a tiempo')
    # r2 = Ride(creator_id=26, pickup_location='Florida', destination='San joaquin', space_available=3,
    #          departure_date='2023-05-09 07:00', charge='8500 COP', vehicle_id=1, description='recibo davi')
    # r3 = Ride(creator_id=25, pickup_location='Florencia', destination='San marcos', space_available=3,
    #          departure_date='2023-05-10 07:00', charge='9500 COP', vehicle_id=1, description='recibo nequi')
    # r4 = Ride(creator_id=26, pickup_location='Afidro', destination='Bachue', space_available=3,
    #          departure_date='2023-05-18 07:00', charge='2500 COP', vehicle_id=1, description='')
    # r5 = Ride(creator_id=25, pickup_location='Paris', destination='Bolivia', space_available=0,
    #          departure_date='2023-05-19 07:00', charge='1500 COP', vehicle_id=1, description='')
    # rideDAO = RideDAOImpl()
    # rideDAO.insert(r)
    # rideDAO.insert(r2)
    # rideDAO.insert(r3)
    # rideDAO.insert(r4)
    # rideDAO.insert(r5)
    #return all rides with ride available = 1
    #print(type(rideDAO.getRidesByStatus(1)[0]._departure_date))
    #
    # r = RideDAOImpl()
    # print(r.getRideById(88))
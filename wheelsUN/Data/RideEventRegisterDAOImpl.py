from datetime import datetime
from Data.PoolCursor import PoolCursor
from Data.RideEventRegister import RideEventRegister
from Data.RideEventRegisterDAO import RideEventRegisterDAO


class RideEventRegisterDAOImpl(RideEventRegisterDAO):

    def insert(self, event:RideEventRegister):
        try:
            with PoolCursor() as cursor:
                query = f"insert into ride_logs (ride_id, user_id, event_description, " \
                        f"event_date) " \
                        f"values ({event._ride_id},{event._user_id},'{event._event_description}'," \
                        f"'{event._event_date}' )"
                cursor.execute(query)
                return cursor.rowcount
                # print(f'inserted records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def select(self, event:RideEventRegister):
        try:
            with PoolCursor() as cursor:
                query = f"select * from ride_logs"
                cursor.execute(query)
                #captura de registros
                records = cursor.fetchall()
                if records:
                    return 1
                else:
                    return 0
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def getEventRegisterByUser(self, user_id):

        try:
            with PoolCursor() as cursor:
                events = []
                query = f"select * from ride_logs where user_id = {user_id}"
                cursor.execute(query)
                #captura de registros
                records = cursor.fetchall()
                if records:
                    for i in records:
                        e = RideEventRegister(int(i[1]), int(i[2]), i[3], i[4])
                        events.append(e)
                    return events
                else:
                    #no events founded for that user
                    return 0
        except Exception as e:
            print(f'An exception has occurred: {e}')



    def getEventRegisterByRide(self, ride_id):
        try:
            with PoolCursor() as cursor:
                events = []
                query = f"select * from ride_logs where ride_id = {ride_id}"
                cursor.execute(query)
                # captura de registros
                records = cursor.fetchall()
                if records:
                    for i in records:
                        e = RideEventRegister(int(i[1]), int(i[2]), i[3], i[4])
                        events.append(e)
                    return events
                else:
                    # no events founded for that ride
                    return 0
        except Exception as e:
            print(f'An exception has occurred: {e}')


if __name__ == "__main__":
    ride_id = 90
    user_id = 29
    event_description = f"el usuario {user_id} creó el viaje {ride_id}"
    e = RideEventRegister(ride_id, user_id, event_description, datetime.now())
    t = RideEventRegisterDAOImpl()
    t.insert(e)

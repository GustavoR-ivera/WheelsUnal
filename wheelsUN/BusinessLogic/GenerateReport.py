
from datetime import datetime
from Data.PoolCursor import PoolCursor
from Data.User import User
from Data.UserDAOImpl import UserDAOImpl


class GenerateReport():

    def __init__(self, activeUser, startDate, endDate, reportType):
        self._activeUser = activeUser
        self._startDate = startDate
        self._endDate = endDate
        self._reportType = reportType

    def getData(self):
        try:
            with PoolCursor() as cursor:
                #validate report type
                if (self._reportType == "created trips"):
                    #specify the fields to be report
                    query = f"select * from rides where creator_id = {self._activeUser._user_id} " \
                            f"and created_at >= '{self._startDate}' AND created_at <= '{self._endDate}' ;"
                    cursor.execute(query)
                    record = cursor.fetchall()
                    if record:
                        # if the user has some created trips show them
                        # generate file todo
                        return record
                    else:
                        return 0

                elif(self._reportType == 'trips I have joined'):
                    # specify the fields to be report
                    query1 = f"select ride_id from user_rides where user_id = {self._activeUser._user_id} "
                    cursor.execute(query1)
                    # if the user had joined to some trips then record is not empty
                    # record is a list of tuples everyone with one element -> ride_id
                    record = cursor.fetchall()
                    if record:
                        rides = []
                        for value in record:
                            rides.append(value[0])
                        # convert the list of ride_id's into a tuple
                        ride_id_tuple = tuple(rides)
                        if len(ride_id_tuple) == 1:
                            # make query2 in order to get the rides information
                            query2 = f"select * from rides where ride_id = {ride_id_tuple[0]} " \
                                     f"and created_at >= '{self._startDate}' AND created_at <= '{self._endDate}' ;"
                            cursor.execute(query2)
                            rides_info = cursor.fetchall()
                            #rides_info -> list of tuples with rides info
                            return rides_info
                        else:
                            # make query2 in order to get the rides information
                            query2 = f"select * from rides where ride_id in {ride_id_tuple} " \
                                     f"and created_at >= '{self._startDate}' AND created_at <= '{self._endDate}' ;"
                            cursor.execute(query2)
                            rides_info = cursor.fetchall()
                            # rides_info -> list of tuples with rides info
                            return rides_info
                    else:
                        return 0

        except Exception as e:
            print(f'An exception has occurred: {e}')


if __name__ == "__main__":
    u = User()
    userdao = UserDAOImpl()
    user = userdao.getUserById(25)
    n = GenerateReport(user, "2023/01/01 00:00:00", "2023/10/31 00:00:00", "trips I have joined")
    value = n.getData()
    if value == 0:
        print("the user has no trips")
    else:
        for record in value:
            print(record)
            #created_at=record[2]
            #print(created_at, created_at.year, created_at.month, created_at.day, created_at.hour, created_at.second)

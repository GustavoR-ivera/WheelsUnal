from datetime import datetime


class RideEventRegister():
    def __init__(self, ride_id = None, user_id= None, event_description= None, event_date= None):
        self._ride_id = ride_id
        self._user_id = user_id
        self._event_description = event_description
        self._event_date = event_date

    # toString
    def __str__(self):
        return f'Event ' \
               f'ride_id:{self._ride_id}, ' \
               f'user_id:{self._user_id}, ' \
               f'event_description:{self._event_description}, ' \
               f'event_date:{self._event_date}'

if __name__ == '__main__':
    e = RideEventRegister(15, 45, 'el usuario creo el viaje', datetime.now())
    print(e)

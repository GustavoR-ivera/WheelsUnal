from datetime import datetime


class Ride:

    #constructor
    def __init__(self, ride_id=None, creator_id=None, created_at=datetime.now(), updated_at=datetime.now(),
                 deleted_at=None, pickup_location=None, destination=None, space_available=0, departure_date = None,
                 charge = None, vehicle_id=None, ride_available=1, description=None):
        # user attributes
        self._ride_id = ride_id
        self._creator_id = creator_id
        # register dates
        self._created_at = created_at
        self._updated_at = updated_at
        self._deleted_at = deleted_at
        self._pickup_location = pickup_location
        self._destination = destination
        self._departure_date = departure_date
        self._charge = charge
        self._space_available = space_available
        self._vehicle_id = vehicle_id
        self._ride_available = ride_available
        self._description = description

    #getters setters

    # toString
    def __str__(self):
        return f'Ride ' \
               f'ride_id:{self._ride_id}, ' \
               f'creator_id:{self._creator_id}, ' \
               f'created_at:{self._created_at}, ' \
               f'vehicle_id:{self._vehicle_id}, ' \
               f'pickup_location:{self._pickup_location}, ' \
               f'_destination:{self._destination}, ' \
               f'description: {self._description}'


if __name__ == '__main__':
    r = Ride()
    print(r)
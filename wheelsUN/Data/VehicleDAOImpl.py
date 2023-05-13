from datetime import datetime

from Data.PoolCursor import PoolCursor
from Data.User import User
from Data.Vehicle import Vehicle
from Data.VehicleDAO import VehicleDAO


class VehicleDAOImpl(VehicleDAO):

    def getVehicleById(self, vehicle_id):
        # return a vehicle with the vehicle_id specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM vehicles " \
                        f"WHERE vehicle_id = '{vehicle_id}' "
                cursor.execute(query)
                record = cursor.fetchone()
                if record:
                    # if a vehicle exist wiht the specified id then it creates the vehicle and return it
                    vehicle = Vehicle(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                record[7],record[8], record[9], record[10], record[11], record[12], record[13])
                    return vehicle
                else:
                    # if not then return none
                    return None
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getVehicleByPlate(self, vehicle_plate):
        # return a vehicle with the vehicle_plate specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM vehicles " \
                        f"WHERE vehicle_plate = '{vehicle_plate}' "
                cursor.execute(query)
                record = cursor.fetchone()
                if record:
                    # if a vehicle exist wiht the specified plate then it creates the vehicle and return it
                    vehicle = Vehicle(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7],record[8], record[9], record[10], record[11], record[12], record[13])
                    return vehicle
                else:
                    # if not then return none
                    return None
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getVehiclesByOwnerId(self, owner_id):
        # return a list vehicles with the owner id specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM vehicles " \
                        f"WHERE owner_id = '{owner_id}' "
                cursor.execute(query)
                records = cursor.fetchall()
                if records:
                    vehicles = []
                    for vehicle in records:
                        # if a vehicle exist wiht the specified plate then it creates the vehicle and return it
                        v = Vehicle(vehicle[0],vehicle[1],vehicle[2],vehicle[3],vehicle[4],vehicle[5],vehicle[6],
                                          vehicle[7],vehicle[8],vehicle[9],vehicle[10],vehicle[11],vehicle[12],vehicle[13])
                        vehicles.append(v)
                    return vehicles
                else:
                    # if not then return none
                    return None
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def insert(self, vehicle):
        try:
            with PoolCursor() as cursor:
                query = f"insert into vehicles (vehicle_plate,color,type,space_available,model, "\
                        f"owner_id,soat_policy,mechanical_condition_policy,transit_license, " \
                        f"created_at, updated_at, brand )"\
                        f"values ('{vehicle.vehicle_plate}','{vehicle.color}','{vehicle.type}'," \
                        f"{vehicle.space_available},'{vehicle.model}', "\
                        f"{vehicle.owner_id},'{vehicle.soat_policy}','{vehicle.mechanical_condition_policy}'," \
                        f"'{vehicle.transit_license}', " \
                        f"'{vehicle.created_at}', '{vehicle.updated_at}', '{vehicle.brand}')"
                cursor.execute(query)
                return cursor.rowcount
                #print(f'inserted records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def select(self):
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * FROM vehicles"
                cursor.execute(query)
                records = cursor.fetchall()
                print(f'records: {cursor.rowcount}')
                print(f'users: {records}')
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def delete(self, vehicle):
        try:
            with PoolCursor() as cursor:
                query = f"update vehicles " \
                        f"set deleted_at = '{datetime.now()}'  " \
                        f"where vehicle_id = {vehicle.vehicle_id} "
                cursor.execute(query)

                return cursor.rowcount
                #print(f'deleted records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def update(self, user):
        pass

if __name__ == "__main__":
    v = VehicleDAOImpl()
    vehicle = Vehicle(vehicle_plate='XYZ-123',color='Azul',type='Automovil',space_available=5,
            model=2017,owner_id=25,soat_policy='2125454556',mechanical_condition_policy='FREFE-200',
            transit_license='BFVDV-O',brand='Chevrolet')
    v.insert(vehicle)
    vehicle = Vehicle(vehicle_plate='RTR-123',color='Negro',type='Automovil',space_available=4,
                model=2017,owner_id=25,soat_policy='2125454556',mechanical_condition_policy='FREFE-200',
                transit_license='BFVDV-O',brand='Ford')
    v.insert(vehicle)
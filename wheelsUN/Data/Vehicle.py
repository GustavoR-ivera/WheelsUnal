from datetime import datetime


class Vehicle:
    def __init__(self,vehicle_id=None,vehicle_plate=None,color=None,type=None,space_available=None,model=None,
                 owner_id=None,soat_policy=None,mechanical_condition_policy=None,transit_license=None,
                 created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, brand=None):
        self.vehicle_id = vehicle_id
        self.vehicle_plate = vehicle_plate
        self.color = color
        self.type = type
        self.space_available = space_available
        self.model = model
        self.owner_id = owner_id
        self.soat_policy = soat_policy
        self.mechanical_condition_policy = mechanical_condition_policy
        self.transit_license = transit_license
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.brand = brand

    def __str__(self):
        return f'Vehicle' \
               f'vehicle_id: {self.vehicle_id}' \
               f'owner_id: {self.owner_id}' \
               f'model: {self.model}' \
               f'color: {self.color}' \
               f'type: {self.type}'


if __name__ == '__main__':
    v = Vehicle()
    print(v)
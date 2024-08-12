from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class BaseData:
    make:str
    model:str
    year:int

class Vehicle(ABC):
    def __init__(self, make:str, model:str, year:int) -> None:
        self.data = BaseData(make=make, model=model, year=year)
    
    @abstractmethod
    def get_details(self):
        return f': {self.data.year} {self.data.make} {self.data.model}'

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int) -> None:
        super().__init__(make, model, year)
    
    def get_details(self):
        return f'Car{super().get_details()}'

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, towing_capacity:int|float) -> None:
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        base_data_str = super().get_details()
        towing_str = f', Towing Capacity: {self.towing_capacity}'
        return f'Truck{base_data_str}{towing_str}'
    
def display_vehicle_details(vehicle):
    print(vehicle.get_details())

if __name__ == "__main__":
    car = Car(make="Toyota", model="Corolla", year=2021)
    truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

    print(car.get_details())  # Car: 2021 Toyota Corolla
    print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

    display_vehicle_details(car)  # Car: 2021 Toyota Corolla
    display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000

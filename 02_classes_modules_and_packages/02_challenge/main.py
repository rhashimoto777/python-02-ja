from inventory import Inventory
from vehicle import Vehicle
# from data_parser import parse_vehicle_data

# vehicles = parse_vehicle_data("vehicles.txt")
inventory = Inventory()
# for vehicle in vehicles:
#     inventory.add_vehicle(vehicle)


v1 = Vehicle()
v1.set(model="Corolla",make="Toyota",year="2020",price="20000")
inventory.add_vehicle(v1)

print("_____________________________________")
print(inventory.vehicles[0].get_model())  # Corolla
print(inventory.vehicles[0].get_make())  # Toyota
print(inventory.vehicles[0].get_year())  # 2020
print(inventory.vehicles[0].get_price())  # 20000
print(inventory.vehicles[0].get_discount())  # 0
print("_____________________________________")

inventory.apply_discount(lambda v: v.make == "Toyota", 5)
# toyotas = inventory.search_vehicles("Corolla")

# for toyota in toyotas:
#     toyota.display()

for vehicle in inventory.retrieve_vehicles():
    vehicle.display()
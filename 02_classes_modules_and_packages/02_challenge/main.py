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

# v1.set(model="Model2",make="Toyotaaa",year="1900",price="3")
# inventory.add_vehicle(v1)
# v1.set(model="Aa-Corolla",make="Aa",year="1950",price="15")
# inventory.add_vehicle(v1)

v2 = Vehicle()
v2.set(model="Model2",make="Toyotaaa",year="1900",price="3")
inventory.add_vehicle(v2)

v3 = Vehicle()
v3.set(model="Aa-Corolla",make="Aa",year="1950",price="15")
inventory.add_vehicle(v3)

print("_____________________________________")
print(inventory.vehicles[0].get_model())  # Corolla
print(inventory.vehicles[0].get_make())  # Toyota
print(inventory.vehicles[0].get_year())  # 2020
print(inventory.vehicles[0].get_price())  # 20000
print(inventory.vehicles[0].get_discount())  # 0
print("_____________________________________")

inventory.apply_discount(lambda v: v.make == "Toyota", 5)
toyotas = inventory.search_vehicles("Corolla")

print("---------- search vehicles ----------")
for toyota in toyotas:
    toyota.display()

print("---------- all vehicles ----------")
for vehicle in inventory.retrieve_vehicles():
    vehicle.display()
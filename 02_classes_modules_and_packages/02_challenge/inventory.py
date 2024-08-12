from vehicle import Vehicle
import re

class Inventory:
    def __init__(self):
        self.vehicles = []
        return
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        return

    def retrieve_vehicles(self):
        for v_elem in self.vehicles:
            yield v_elem
    
    def apply_discount(self, rule_lambda, discount):
        Vehicle.overwrite_discount_rule(rule_lambda, discount)
        for v_elem in self.vehicles:
            v_elem.apply_discount()
            print(v_elem.apply_discount_2(rule_lambda, discount))

    def search_vehicles(self, model_input):
        ret = []
        for vehicle in self.vehicles:
            found = re.findall(model_input, vehicle.get_model())
            if len(found) >= 1:
                ret.append(vehicle)
        return ret
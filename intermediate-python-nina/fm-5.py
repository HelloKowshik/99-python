# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))

class Vehicle:
    def __init__(self, make, model, fuel = "Gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def eco_friendly(self):
        if self.fuel == "Solar":
            return True
        else:
            return False


class Car(Vehicle):
    def __init__(self, make, model, fuel = "Solar"):
        super().__init__(make, model, fuel)

class Bus(Vehicle):
    def __init__(self, make, model, fuel="Disel", num_of_passenger= 10):
        super().__init__(make, model, fuel)
        self.num_of_passenger = num_of_passenger

    def bus_route(self):
        print('Bus route is 50 KM from Busan')

car1 = Car('Toyota', 'Alion-121')
bus1 = Bus('Daieo', 'DA-223', 'Disel/Petrol', 50)
print(bus1.make, bus1.model, bus1.fuel, bus1.num_of_passenger, bus1.eco_friendly())
bus1.bus_route()
# print(car1.make, car1.model, car1.fuel, car1.eco_friendly())
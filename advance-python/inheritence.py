class Vehicle:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving!')

    def stop(self):
        self.speed = 0
        print('Stopped!')

    def display(self):
        print(f'Driving at {self.speed} Speed!')

class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing!')

    def display(self):
        print(f'Freezing at {self.temp} Temparature!')                    

class FreezerTruck(Freezer, Vehicle):
    def display(self):
        print(f'Subclass Of Freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'Subclass Of Vehicle: {issubclass(FreezerTruck, Vehicle)}')
        Freezer.display(self)
        Vehicle.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
t.display()
print(FreezerTruck.__mro__)

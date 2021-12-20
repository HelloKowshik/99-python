# Abstract method, class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass    

class Car(Vehicle):
    def go(self):
        print('You drive Car!')

    def stop(self):
        print('Car Stopped!')    

class MotorCycle(Vehicle):
    def go(self):
        print('You drive MotorCycle!')

    def stop(self):
        print('MotorCycle Stopped!')    

    def test(self):
        print('testing!')    


# vehicle = Vehicle()
car  = Car()
motorcycle = MotorCycle()

# vehicle.go()
car.go()
motorcycle.go()
motorcycle.test()

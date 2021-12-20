# Multi Level Inheritence
class Organism:
    alive = True

class Animal(Organism):
    alive = True

    def eat(self):
        print('Animal can Eat!')

    def sleep(self):
        print('Animal can Sleep!') 


class Rabbit(Animal):
    pass

class Hawk(Animal):
    pass

class Dog(Animal):
    def bark(self):
        print('Dog is barking!')

dog = Dog()
# print(Dog.__mro__)                               

# Multiple Inheritence

class Prey:
    def flee(self):
        print('This Animal flees!')

class Predator:
    def hunt(self):
        print('This Animal hunts!')        

class Fish(Prey, Predator):
    pass

fish = Fish()
# print(Fish.__mro__) 
# fish.flee()
# fish.hunt()   

class Car:
    def turn_on(self):
        print('Car Turns On!')
        return self
    def drive(self):
        print('Car is Running!')
        return self
    def break_on(self):
        print('Driver Steps on Break!')
        return self
    def turn_off(self):
        print('Car is Off!')
        return self

car = Car()
car.turn_on().drive().break_on().turn_off()                    

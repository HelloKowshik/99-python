class Car:
    color = None

def change_color(obj, color):
    obj.color = color

car1 = Car()
car2 = Car()
car3 = Car()

change_color(car1, 'red')
change_color(car2, 'green')
change_color(car3, 'blue')

# print(car1.color)        
# print(car2.color)        
# print(car3.color)        

class Duck:
    def walk(self):
        print('Duck is walking')

    def talk(self):
        print('Duck is Quacking')

class Chicken:
    def walk(self):
        print('Chicken is walking')

    def talk(self):
        print('Chicken is clucking')

class Person:
    def catch_duck(self, duck):
        duck.walk()
        duck.talk()
        print('You catched a critter!')

duck = Duck()
chicken = Chicken()
person = Person()
# person.catch_duck(chicken)                                
# person.catch_duck(duck)                                

check_age = lambda age: 'Eligible' if age >= 18 else 'Not Eligible'
print(check_age(17))

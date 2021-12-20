class Car:
    wheels = 4 #class variable
    def __init__(self, make, model, year, color):
        self.make = make #instance variable
        self.model = model
        self.year = year
        self.color = color

car_1 = Car('Chevy', 'Corvette', 2021, 'Blue')
car_2 = Car('Ford', 'Mustang', 2022, 'Red')  
car_1.wheels = 6      
print(car_2.wheels)

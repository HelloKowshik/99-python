class Car:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} is Started!")
        else:
            print(f"{self.name} is not started!")


class Human:
    alive = True

    def info(self, gender):
        self.gender = gender
        if self.alive:
            print(f"Human is ALIVE Gender: {self.gender}")
        else:
            print('Human is Not Alive!!')


h1 = Human()
print(type(h1))
h1.alive = False
h1.info("Male")


# car1 = Car()
# print(type(car1))
# car1.runs = False
# car1.start('BMW')

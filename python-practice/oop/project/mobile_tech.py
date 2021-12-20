from tech_product import Tech

class Mobile(Tech):
    def __init__(self, name, price, weight, color, screen, camera):
        super().__init__(name, price, weight, color)
        self.screen = screen
        self.camera = camera

    def apply_discount(self):
        self.price = int(self.price - self.price * (super().discount / 2))

    def change_specs(self, ram, storage):
        if ram > self.ram or storage > self.storage:
            self.price = self.price + 10000
        self.ram = ram
        self.storage = storage            

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Weight: {self.weight}, Color:{self.color}\n'\
        f'Screen: {self.screen}, Camera: {self.camera}'    

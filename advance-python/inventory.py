import json
import os.path

class Inventory:
    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
            print(v, q)
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: Total = {self.pets[key]}')
                
    def remove(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: Total = {self.pets[key]}')

    def display(self):
        for key, val in self.pets.items():
            print(f'{key} = {val}')

    def save(self):
        print('Saving To Inventory')
        with open('inventory.txt', 'w') as file:
            json.dump(self.pets, file)
        print('Saved!')

    def load(self):
        print('Loading Inventory')
        if not os.path.exists('inventory.txt'):
            print('Nothing To Load...')
            return
        with open('inventory.txt', 'r') as file:
            self.pets = json.load(file)
        print('Loaded!')                   

def main():
    inv = Inventory()

    while True:
        action = input('Action: add, remove, list, save, exit: ')
        if action == 'exit':
            break
        if action == 'add' or action == 'remove':
            key = input('Enter Animal Name:')
            qty = int(input('Enter Qty:'))
            if action == 'add':
                inv.add(key, qty)
            else:
                inv.remove(key, qty)
        if action == 'list':
            inv.display()
        if action == 'save':
            inv.save()                    
    inv.save()

if __name__ == '__main__':
    main()            

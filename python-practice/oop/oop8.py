class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


def print_toys_obj(toys_list):
    for toy in toys_list:
        print(f'Toy {toy.name} Price {toy.price}')

toy1 = Toy('Woody', 1100)
toy2 = Toy('AOT_Whels', 800)
toy3 = Toy('Wall-E', 1200)
toys = [toy3, toy1, toy2]
# toys.sort(key=Toy.sort_priority, reverse=True)
# sorted_toys = sorted(toys, key=Toy.sort_priority)
# print_toys_obj(toys)
# toys.sort(key = lambda toy: toy.price)
lambda_sorted = sorted(toys, key = lambda toy: toy.price)
print_toys_obj(lambda_sorted)


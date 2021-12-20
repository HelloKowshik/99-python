import random

def add(*args):
    print(type(args))

# add(1, 2, 3, 4)   
n = 15
# print(f'{n:x}, {n:o}, {n:b}, {n}') 

x = random.randint(1, 6)
y = ['rock', 'paper', 'scissors']
z = random.choice(y)
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)

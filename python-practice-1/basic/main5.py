# rock, paper, scissors

import random
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = None

while player not in choices:
    player = input('rock, paper, scissors? ').lower()

if computer == player:
    print('Computer: ', computer)
    print('Player: ', player)
    print('Tie')

elif player == 'rock':
    if computer == 'paper':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Loose!')
    if computer == 'scissors':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Won!')

elif player == 'scissors':
    if computer == 'rock':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Loose!')
    if computer == 'paper':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Won!')

elif player == 'paper':
    if computer == 'rock':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Won!')
    if computer == 'scissors':
        print('Computer: ', computer)
        print('Player: ', player)
        print('You Won!')        


import random as r

# nth Fibonacci Number


def fibonacci(n):
    x = 0
    y = 1
    print(x)
    print(y)
    for i in range(1, n):
        z = x + y
        x = y
        y = z
        print(z)


# fibonacci(6)

# Guess my age

secret_age = r.randint(1, 10)
flag = False


def guess_age(g, secret):
    if g > secret:
        return 'Too High!'
    elif g < secret:
        return 'Too Low!'
    else:
        return 'Correct'


for i in range(1, 6):
    guess = int(input('Enter Your Guess. You have ' + str(6 - i) + ' options left: '))
    if guess_age(guess, secret_age) == 'Correct':
        print("You Won! Your Guess is Correct!")
        flag = True
        break
    else:
        print(guess_age(guess, secret_age))

if not flag:
    print('You Lost!')


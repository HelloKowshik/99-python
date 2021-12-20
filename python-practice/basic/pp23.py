def myFilter(fn, l):
    newL = []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL


l = [1, 22, 11, 32, 21]
x = myFilter(lambda x: x % 2 == 0, l)
# print(x)

def square(x):
    return x ** 2


def wrapper(fn, x):
    print('Welcome To Square Func.')
    print(square(x))
    print('Thank You!')

wrapper(square, 4)


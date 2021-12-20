def add(*args):
    total = 0
    for i in args:
        total += i
    return total

def add_again(**kwargs):
    total = 0
    for i in kwargs:
        total += kwargs[i]
    return total    

# print(add_again(a=1,b=2,c=3,d=4,e=5))

def greater(a, b, c):
    if a > b and a > c:
        return f'{a} is largest!'
    elif b > a and b > c:
        return f'{b} is largest!'
    elif c > a and c > b:
        return f'{c} is largest!'
    else:
        return f'{a}, {b}, {c} are equal!'

# a, b, c = list(map(int, input('Enter Number: ').split()))
# print(greater(a, b, c))                           


def gcd(a, b):
    if b > a:
        gcd(b, a)
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = list(map(int, input('Enter Number: ').split()))
print(lcm(a, b))                                       

import math as m
# Check Even or Odd


def even_odd(n):
    if n % 2 == 0:
        return str(n) + ' is Even.'
    else:
        return str(n) + ' is Odd.'


# print(even_odd(int(input('Enter an Integer: '))))

# Find Area of Rectangle, Circle, Square, Triangle, Trapezium

# s = str(input('Enter Shape: '))

def calculate_area(shape):
    if shape == 'Rectangle':
        l = int(input('Enter Length: '))
        w = int(input('Enter Width: '))
        return l * w
    elif shape == 'Circle':
        r = int(input('Enter Radius: '))
        return m.pi * r * r
    elif shape == 'Square':
        l1 = int(input('Enter the Length: '))
        return m.pow(l1, 2)
    elif shape == 'Triangle':
        b = int(input('Enter Base: '))
        h = int(input('Enter Height: '))
        return 0.5 * b * h
    elif shape == 'Trapezium':
        h1 = int(input('Enter Height: '))
        a = int(input('Enter value of a: '))
        b1 = int(input('Enter value of b: '))
        return (h1/2) * (a + b1)
    else:
        return 'Invalid Selection!'


# print(calculate_area(s))


# Check prime Number

def prime_check(n):
    count = 0
    for i in range(2, m.floor(m.sqrt(n)) + 1):
        if n % i == 0:
            print(str(n)+' is not prime Number')
            break
        count = count + 1
    if count + 2 == m.floor(m.sqrt(n)) + 1:
        print(str(n)+' is prime Number')


# prime_check(int(input('Enter an Integer: ')))


# find HCF

def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans


# print(hcf(4, 8))

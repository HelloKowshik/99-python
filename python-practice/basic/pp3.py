num1 = int(input('Enter an Num1: '))
num2 = int(input('Enter an Num2: '))
op = input('Enter Operation Like +,-,/,*,% : ')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '%':
    print(num1 % num2)
else:
    print('Invalid Operation')

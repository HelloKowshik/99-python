# user_input = map(int, input('Enter 3 numbers: ').split())
# print(f"MAX NUM: {max(list(user_input))}")


def find_GCD(a, b):
    while 1:
        remainder = a % b
        if remainder == 0:
            break
        a = b
        b = remainder
    return b


def find_LCM(a, b):
    return (a * b) // find_GCD(a, b)


num1, num2 = map(int, input('Enter Two number: ').split())
print(f"LCM of {num1} AND {num2} is: {find_LCM(num1, num2)}")

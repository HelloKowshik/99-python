def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor = factor + 1
    return "Done"


# print_prime_factors(100)

# Should print 2,2,5,5


def sum_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])


# print(sum_divisors(0))
# print(sum_divisors(3))
print(sum_divisors(36))
# print(sum_divisors(102))


def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


# multiplication_table(3)
# multiplication_table(5)
# multiplication_table(8)

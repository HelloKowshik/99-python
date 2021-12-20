class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        if self.num1 < self.num2:
            return self.num2 - self.num1
        else:
            return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Can't divide by Zero!"


class SuperCalculator(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(a, b)

    def get_cube(self, a):
        return a * a * a

    def add(self, a, b):
        return (a + b) / abs(a - b)


cal1 = Calculator(15, 14)
sup1 = SuperCalculator(2, 3)
temp = cal1.add()
temp = cal1.subtract()
temp = cal1.mul()
temp = cal1.div()
temp = sup1.get_cube(3)
temp = sup1.add(15, 5)
# print(temp)

try:
    if 3 < 5:
        raise NameError('Just raising a NAME ERROR!')
except NameError as e:
    print(e)
finally:
    print('I AM ALWAYS!')

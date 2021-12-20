class Calculator:
    def __init__(self, a, b):
        print(self)
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def mod(self):
        try:
            return self.a % self.b
        except ZeroDivisionError:
            return 'Dividive by ZERO not possible!'        
        
    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'Dividive by ZERO not possible!'

cal1 = Calculator(102, 0)
cal2 = Calculator(102, 0)
# print(cal1.mod())                            

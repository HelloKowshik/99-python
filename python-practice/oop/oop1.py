class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def mod(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return 'Dividive by ZERO not possible!'        
        
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Dividive by ZERO not possible!'

cal1 = Calculator()
print(cal1.mod(12, 0))                            

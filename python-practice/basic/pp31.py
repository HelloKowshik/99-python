class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def printHello(self):
        print(f'{self.a} - {self.b}')

# b = B('12', '41')
# b.printHello()                    

x = iter('hello')
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

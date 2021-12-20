class A:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print('Hello From Class A')

class B:
    def __init__(self, job):
        self.job = job
    def hello(self):
        print('Hello From Class B')

class C(A, B):
    def __init__(self, name, job):
        A.__init__(self, name)
        B.__init__(self, job)

    def hello(self):
        A.hello(self)
        print(f'{self.name} is {self.job}')
        B.hello(self)

b = C('John', 'Developer')
b.hello()                  
# print(C.__mro__)

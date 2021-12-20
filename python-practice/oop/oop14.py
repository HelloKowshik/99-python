class A:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print('Hello From Class A')

class B(A):
    def __init__(self, name, job):
        super().__init__( name)
        # A.__init__(self, name)
        self.job = job
    def hello(self):
        print(f'{self.name} is an {self.job}')

class C(B):
    pass

b = C('John', 'Developer')
b.hello()                    

from time import time

def timer(any_function):
    def count_time():
        start = time()
        any_function()
        stop = time()
        print(stop - start, ' seconds')
        return
    return count_time    

@timer
def hello():
    sum = 0
    for i in range(1, 100):
        sum = sum + i
        print(sum)

# hello()

def another_func():
    sum = 0
    for i in range(1, 200):
        sum = sum + i
        print(sum)
    return

x = timer(another_func)
# x()
class MyClass:
    def __init__(self):
        pass

    def square(self, x):
        return x ** 2

    @classmethod
    def cube(self, x):
        return x ** 3  

# if __name__ == '__main__':          
#     class1 = MyClass()
#     print(MyClass.cube(3))        
#     print(class1.square(3))        
#     print(class1.cube(3))                
#     print(MyClass.square(class1,3))        
#     print(MyClass.square(3))


class AnotherClass:
    def __init__(self):
        pass

    @staticmethod    
    def square(x):
        return x ** 2

    def cube(self, x):
        return x ** 3  

# if __name__ == '__main__':
#     class2 = AnotherClass()
#     print(class2.cube(5))          
#     print(AnotherClass.square(5))        
    # print(AnotherClass.square(class2, 5))        
    # print(class2.square(5))        


class MySelf:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def print_name(self):
        return f'{self.first_name} {self.last_name}'
    

if __name__ == '__main__':
    person1 = MySelf('Maksudur', 'Rahman')
    print(person1.print_name)    

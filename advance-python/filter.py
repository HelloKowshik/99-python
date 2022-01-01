import random;
v = [];
for i in range(10):
    v.append(random.randrange(100));
# print(v);    
f = list(filter(lambda val: val < 50, v));
# print(f);


class Animal:
    name = '';
    def __init__(self, name):
        self.name = name;

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name);

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name);

animals = [];
for x in range(10):
    if x % 2 == 0:
        animals.append(Cat(Cat.__name__+'-'+str(x)));
    else:
        animals.append(Dog(Dog.__name__+'-'+str(x)));

for i in list(filter(lambda v: isinstance(v, Cat), animals)):
    print(i.name)                                    


from functools import reduce

def func(*args):
    print(args)

# func(1,2,3,4,5)    

def func1(**kwargs):
    print(kwargs)

# func1(key1='a', key2='b', key3='c') 

# print((lambda x, y : x + y)(10, 20))   

l = [2, 3, 1, 4, 0, 6]

newL = list(map(lambda n: n * n * n, l))
# print(newL)


oddList = list(filter(lambda x: x % 2 == 1, l))
# print(oddList)

total = reduce(lambda a, b: a + b, l )
print(total)

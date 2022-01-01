def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner

# @makeBold
# def text():
#     print('Simple Normal Text.')
# text()

def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('ZeroDivisionError!')
                return False
            return True
        print(f'{o} is not a number.')    
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)
    return inner

@numcheck
def div(a, b):
    print(a / b)

# div(100, 10)                        

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        func(*args, **kwargs)
        print('-'*20)
    return inner    

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'*args = {args}')
        print(f'**kwargs = {kwargs}')
        for x in args:
            print(f'args={x}')
        for k, v in kwargs.items():
            print(f'{k}={v}')    
    return inner    


@outline
@list_items
def display(msg):
    print(msg)

display('Hello World')            

@outline
@list_items
def birthday(name='', age=''):
    print(f'Hello {name}, you are now {age}!')

birthday(name='Smith', age=32)    

def outer(msg):
    print('Outer Function!')

    def inner():
        print('Inner Function!')
        print(msg)

    return inner

# fx = outer('Welcome!')
# fx()
# print(fx)        

def decorator(original_func):
    print('In the decorator function!')

    def wrapper():
        print(f'Wrapper Executed before {original_func.__name__}()')
        if 10 > 5:
            print('True Statement!')
        return f'{original_func()}'        
    return wrapper

# @decorator
# def print_str():
    # print('I am printing...')
    
# print_str()
# decorator1 = decorator(print_str)
# decorator1()
# print(decorator1)

def print_int(number):

    def get_int_as_str(number):
        print(str(number))
        # return

    return get_int_as_str(number)

print_int(130)        

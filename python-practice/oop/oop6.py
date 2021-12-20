def outer(msg):
    print('I am OUTER function')

    def inner():
        print('I am INNER function')
        print(msg)

    return inner


def decorator(original_func):
    print('In the DECORATOR function.')

    def wrapper():
        print(f'WRAPPER executed before {original_func.__name__}().')

        if 5 > 4:
            print('YES, it is TRUE')
        return original_func()
    
    return wrapper            

def print_str():
    print('PRINT A RANDOM STR.')
    # return 'PRINT A RANDOM STR.'

# calling decorator - way-1    

# decorator1 = decorator(print_str)
# decorator1()

# calling decorator - way-2

# @decorator
# def another_print():
#     print('ANOTHER RANDOM STR')
# another_print()    


def decorator11(original_func):
    print('In the DECORATOR_11 function.')

    def wrapper(*args, **kwargs):
        print(f'WRAPPER executed before {original_func.__name__}().')

        if 5 > 4:
            print('YES, it is TRUE')
        return original_func(*args, **kwargs)
    
    return wrapper


@decorator11
def another_func_11(arg1, arg2):
    print(f'Arg1 = {arg1}, Arg2 = {arg2}')

another_func_11(12, 32)

def decorator_list(fnc):
    def inner_fun(list_of_tuple):
        return [fnc(val[0], val[1]) for val in list_of_tuple]
    return inner_fun    


# @decorator_list
def addd_together(a, b):
    return a + b

# print(addd_together([(1, 3), (3, 17), (5, 10), (20, 21)]))    

add_together = decorator_list(addd_together)
print(add_together([(1, 3), (3, 17), (5, 10), (20, 21)]))

def meta_decorator(arg):
    # print(callable(arg))
    def decorator_list(fnc):
        def inner_fun(list_of_tuple):
            return [fnc(val[0], val[1]) ** power for val in list_of_tuple]
        return inner_fun
    # return decorator_list
        
    if callable(arg):
        power = 2
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list          

# @meta_decorator(2)
@meta_decorator
def addd_together(a, b):
    return a + b          

print(addd_together([(1, 3), (3, 17), (5, 10), (20, 21)]))    

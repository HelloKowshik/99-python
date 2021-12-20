def show_name(name):
    print('User name:' + name)


# show_name(input('Enter Your Name: '))

def test():
    global a
    print(a)


a = 22
# test()


def check_error(x):
    try:
        return 100 / x
    except ZeroDivisionError:
        return 'Zero Division Error!'
    except TypeError:
        return 'Type mismatch!'


print(check_error(0))

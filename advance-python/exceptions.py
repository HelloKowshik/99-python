def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function = {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

@outline
def test_one(x, y):
    try:
        z = x / y
        print(f'Z = {z}')
    except:
        print('Error Happend!')
    finally:
        print('All Complete!')

# test_one(11, 10)                

@outline
def test_two(x, y):
    try:
        assert(x > 0)
        assert(y > 0)
    except AssertionError:
        print('AssertionError Happend!')    
    except Exception as e:
        print('Error Happend!', e)
    else:
        z = x / y
        print(f'Z = {z}')   
    finally:
        print('All Complete!')

test_two(11, 0)
test_two(11, 'cat')

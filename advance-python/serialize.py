import pickle

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function = {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

class Cat:
    def __init__(self, name, age, info):
        self._name = name
        self._age = age
        self._info = info
    @outline    
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is {self._age} years old Cat.')
        for k,v in self._info.items():
            print(f'{k} = {v}')

othello = Cat('Othello', 8, dict(color='Black', weight=12, loves='Eating'))
# othello.display('Othello Cat')                    

sc = pickle.dumps(othello)
print(sc)
with open('cats.txt', 'wb') as file:
    pickle.dump(othello, file)

dc = pickle.loads(sc)
print('From Str')
othello.display('From String')

import random

players = ['smith', 'warner', 'starc']
p = iter(players)
# print(next(p))
# print(next(p))
# print(next(p))

class Lotto:
    def __init__(self):
        self._max = 5
    def __iter__(self):
        for _ in range(self._max):
            yield random.randrange(0, 100)
    def setMax(self, val):
        self._max = val


print('-'*10)
lotto = Lotto()
lotto.setMax(5)
for x in lotto:
    print(x)
print('-'*10)                        

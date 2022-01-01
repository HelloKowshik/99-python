class Person:
    _name = 'Weak Private Person' #Weak Private

    def setName(self, name):
        self._name = name
        print(f'Name set :{self._name}')

    def __think(self):
        print('Thinking Private!')

    def work(self):
        self.__think()

class Child(Person):
    def testDouble(self):
        self.__think(self)                

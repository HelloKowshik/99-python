myList = ['Bhutan', 'Nepal', 'France', 'Italy', 'Brazil', 'Germany', 'USA']

# newList = myList[0::3]
# print(newList)

# myList.extend(['Bulgeria', 'Poland'])
# print(myList)
set1 = set('12345')
set2 = set('abcde')
set3 = set('cdefg')

set_intersection = set2 & set3
set_union = set2 | set3
set_difference = set2 - set3
set_not = set2 ^ set3
# print(set_not)

dict1 = dict()
dict1['key1'] = 'value1'
a = dict(name = 'John Doe', email = 'john@doe.com', loc = 'USA', salary = 3000)
b = {'name' : 'John Doe', 'email' : 'john@doe.com', 'loc' : 'USA', 'salary' : 3000}
c = dict(zip(['name', 'email', 'loc', 'salary'], ['John Doe', 'john@doe.com', 'USA', 3000]))
d = dict([('name', 'John Doe'), ('email', 'john@doe.com'), ('loc', 'USA'), ('salary', 3000)])
a1, b1 = zip(['a', 'b'], [1, 3])
# print(d)
myList1 = ['ABC', 'DEF', 'GHI', 'JKL']
w1, *w2, w3 = myList1
print(w3)

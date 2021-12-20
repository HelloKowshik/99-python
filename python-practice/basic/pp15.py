dict1 = {'IND': 2007, 'PAK': 2009, 'ENG': 2010}
dict2 = {'WI': [2012, 2016], 'SL': 2014}
dict2['AUS'] = 2021
dict3 = dict1.copy()
dict3.update(dict2)
# del dict3['ENG']
# dict3.clear()
# print(dict3.get('RSA', 'Did Not win Any World Cup Yet!'))
# print('AUS' in dict2)
# list_of_tuples = dict3.items()
# for i in list_of_tuples:
#     print(i)
# keys = dict3.keys()
# values = dict3.values()
# print(values)
dict3.setdefault('RSA', 2022)
print(dict3)

dict11 = {'name': 'John Doe', 'age': 32, 'mail': 'john@doe.com', 'address':{
    'city': 'Dallas',
    'road': 5,
    'country': 'USA'
}, 'profession': 'Web Developer', 'skills': ['js', 'python']}

for keys, values in dict11.items():
    print(keys+':'+str(values))

#dictionaries

contacts = {'first-name': 'John', 'last-name': 'Doe', 'email': 'john@doe.com', 'age': 32, 'address': {
    'city': 'LA',
    'road-no': 5,
    'country': 'USA'
},
            'stacks': ['js', 'nodeJS']
}
locs = {'travel': ['a', 'b', 'c']}
# print(contacts)
keys = contacts.keys()
values = contacts.values()
items = contacts.items()
address = list(contacts['address'].keys())
contacts.update(locs)
copy_dict = contacts.copy()
print(copy_dict)

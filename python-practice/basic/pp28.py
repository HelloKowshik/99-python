name_list = ['Tom Latham', 'Will Young', 'Ross Taylor', 'Devon Conaway', 'Azaz Patel']
list_a = ['name', 'country', 'career']
list_b = ['Kowshikur Rahman', 'Bangladesh', 'Google']
dict1 = {'name': 'Kowshikur Rahman', 'country': 'Bangladesh', 'career': 'Google'}
list_comprehension = [i ** 2 for i in range(1, 21) if i % 4 == 0 ]
set_comprehension = {name for name in name_list if len(name) > 10}
dictionary_comprehension = {i : j for i, j in zip(list_a, list_b)}
dictionary_comprehension = {key : value for value, key in dict1.items()}
dictionary_comprehension = {key : value for value, key in zip(list_a, list_b)}
print(dictionary_comprehension)

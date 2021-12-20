students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krabs']

# students.sort()
# students.sort(reverse=True)

# students = sorted(students)

students = [('Squidward', 'F', 60), 
('Sandy', 'A', 33), 
('Patrick', 'D', 36),
('Spongebob', 'B', 20),
( 'Mr.Krabs', 'C', 78)]

students = (('Squidward', 'F', 60), 
('Sandy', 'A', 33), 
('Patrick', 'D', 36),
('Spongebob', 'B', 20),
( 'Mr.Krabs', 'C', 78))

grades = lambda grade: grade[1]
age = lambda age: age[2]
# students.sort(key=grades, reverse=True)
# students = sorted(students, key=age)
students = sorted(students, key=age, reverse=True)

# for i in students:
#     print(i, end=",")

store = [('shirt', 20.00),('pants', 25.00), ('jacket', 50.00), ('socks', 10.00)]

to_euros = lambda data: (data[0], data[1] * 85.80)
store_bd = list(map(to_euros, store))
# print(store_bd)

friends = [('Rachel', 19), ('Monica', 18),
 ('Phoebe', 17), ('Joey', 16), ('Chandler', 21), ('Ross', 20)]

alcohol_friends = lambda friend: friend[1] > 18
party_friends = list(filter(alcohol_friends, friends))
print(party_friends) 

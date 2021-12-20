from functools import reduce

letters = ['H', 'e', 'l', 'p', ' ', 'M', 'e', ' ', 'A', 'l', 'l', 'a', 'h']
word = reduce(lambda x, y: x + y, letters)
# print(word)

fromOneToTen = [i for i in range(1, 11)]
squares = [i ** 2 for i in range(1, 100) if i % 5 == 0]
# print(fromOneToTen)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda p:p >= 60, students))
passed_students = list(x for x in students if x >= 60)
students_result = [x if x >= 60 else 'F' for x in students]
print(students_result)

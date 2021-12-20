nameList = ['A', 'A', 'B', 'C', 'D', 'D', 'C']
uniqueNames = set(nameList)
# print(sorted(uniqueNames))
set1 = {1, 20, 3}
set2 = {4, 5, 6}
set1.update(set2)
# print(set1, len(set1))
# print(set1 | set2)
# print(set1 & set2)
print(set1 ^ set2)
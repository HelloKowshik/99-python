list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
list3 = ['hello', 'world']
mergedList = []
mergedList.extend([list1, list2, list3])
# del mergedList[0]
# mergedList.remove(mergedList[1])
words = ['apple', 'zoo', 'cow', 'Rat', 'Bat', 'horse']
# words.sort(key=str.lower)
words.sort(key=str.lower, reverse=True)
print(words, end=' ')



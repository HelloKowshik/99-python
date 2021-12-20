list1 = ['phy', 'che', 'math', 'bio']
list1.insert(2, 'ict')
list2 = ['js', ['react', 'vue'], ['angular'], ['node', ['express']]]
list3 = list1 + list2
list3 = list2
list3.insert(0, 'Reference')
list3.extend(['item1', 'item2', 'item3'])
# print(len(list3))

for i in range(0, len(list3)):
    if type(list3[i]) == list:
        for j in range(0, len(list3[i])):
            print('Nested: ' + str(list3[i][j]))
    else:
        print(list3[i], end=' ')

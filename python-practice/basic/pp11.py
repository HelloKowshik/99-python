list1 = [1, 11, 2, 12, 90, 5, 21, 33, 45, 56, 32, 10, 3]

# linear Search
# check = int(input('Check Item: '))
# for item in range(0, len(list1)):
#     if check in list1:
#         print('Yes ' + str(list1.index(check)))
#         break
#     else:
#         print('No')
#         break

# binary Search

list1.sort()
# item = int(input('Enter Item to be Searched: '))

def binary_search(data, el):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]
        if guess == el:
            return 'Item found at: ' + str(mid) 
        elif guess > el:
            high = mid - 1
        elif guess < el:
            low = mid + 1
        return 'Not Found'

# print(binary_search(list1, item))    

# printing the odds

def print_odd(list):
    odd_list = []
    for i in range(0, len(list)):
        if list[i] % 2 == 1:
            odd_list.append(list[i])

    return odd_list

# print(print_odd(list1))                        

# centered average of a list

def center_avg(list):
    list.sort()
    s = 0
    avg = 0
    for i in range(1, len(list) - 1):
        s += list[i]
        avg = s // i
    return avg


# print(center_avg([1, 2, 3, 4, 5, 6, 7]))
nested_list = [['p','q','r'], 1, 2, 3, [100, 121, [11,12,13]]]
# print(nested_list[4][2][2])
aList = [11, 5, 10, 15, 25]
# print(aList[::-2])
print(aList[:-2])

import copy as cp
s = [10, 20]
s.append(60)
n = cp.copy(s)
n.append(60)
x = cp.copy(n)
x.append(60)
# print(s,n,x, sep = '#')

# 1 + 3 + 5 + ..+ 97 = ?

i = 1
total = 0
while i <= 97:
    total = total + i
    i = i + 2

# print(total)    

# num = int(input('Enter Number: '))
# for x in range(1, 11):
#     print(f'{num} X {x} = {num * x}\n')


num_list = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 != 0:
        num_list.append(x)

# print(num_list)        

nums_list = [13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 91, 58, 52, 82, 70, 43, 88, 55, 97, 16, 22, 25, 79, 85, 40, 64, 94, 67, 37]
new_list = []
for num in nums_list:
    if num < 50:
        new_list.append(num)

# print(new_list)

numbers = [40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19, 36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38]
# unique_set = set(numbers)
# print(unique_set)        
unique_list = []
for i in numbers:
    if i not in unique_list:
        unique_list.append(i)

# print(sorted(unique_list))        

# inp1 = int(input('Enter Num: '))
# temp = inp1

# while inp1 > 0:
#     count = temp
#     while count > 0:
#         print(count, end='')
#         count -= 1
#     print()
#     inp1 -= 1    


# user_inp = input('Enter: ')
# user_inp = user_inp.casefold()
# reverse_user_inp = user_inp[::-1]
# if reverse_user_inp == user_inp:
#     print(f'{user_inp} is palindrome!')
# else:
#     print(f'{user_inp} is not palindrome!')    

numbers_list = [1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]
# user_input = int(input('Enter a Number: '))
user_input = False
first = 0
last = len(numbers_list) - 1
is_found = False
cycle = 0
while first <= last and not is_found:
    mid = (first + last) // 2
    if numbers_list[mid] == user_input:
        is_found = True
    else:
        if user_input < numbers_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    cycle += 1

# if is_found:
#     print(f'{user_input} is FOUND After {cycle} cycle(s)')
# else:
#     print(f'{user_input} is not FOUND After {cycle} cycle(s)')                          


A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8}
U = set(A)
I = set(A)

for i in B:
    if i not in U:
        U.add(i)
# print(U) 

for i in B:
    if i in U:
        U.remove(i)
# print(U)        

inp1 = int(input('Enter Num: '))
i = 1
while i <= inp1:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    i += 1
    print()     

# Check a year is leap year or not
'''
year = int(input('Enter Valid Year: '))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(year, 'is leap Year')
else:
    print(year, 'is not leap Year')

'''

# pattern print - 1
'''
row = int(input('Rows:  '))
count = 0
for i in range(0, row):
    for j in range(0, row - i - 1):
        print(end=' ')
    count = count + 1
    for k in range(0, i + count):
        print('*', end='')
    print(' ')

'''

# pattern print - 2
'''
row = int(input('Row Number:'))
for i in range(0, row):
    for j in range(0, row - i - 1):
        print(end=' ')
    for k in range(0, i + 1):
        print('*', end='')
    print(' ')
'''

# Armstrong Number
'''
num = int(input('Enter Number: '))
temp = num
s = 0

while num != 0:
    digit = num % 10
    num = num // 10
    s = s + digit ** 3
if temp == s:
    print(temp, 'is a Armstrong Number')
else:
    print(temp, 'is NOT a Armstrong Number')

'''


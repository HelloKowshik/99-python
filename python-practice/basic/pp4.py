#Sum of Series 1+2+3+...+N

# num = int(input('Enter the Value of N: '))
# s = 0
# for i in range(1, num + 1):
#     s = s + i
# print(s)

#Factorial

# n = int(input('Enter The Number: '))
# fact = 1
#
# for i in range(n, 0, -1):
#     fact = fact * i
# print('factorial of:', n, 'is', fact)

#Sum of Series 1*1 + 2*2 + 3*3 + ... + N*N

# s = 0
# N = int(input('Enter The Value of N: '))
# for i in range(1, N + 1):
#     s = s + i * i
# print(s)

#Sum of Series 2 + 4 + 6 +... + N

'''
s = 0
N = int(input('Enter The Value of N: '))
for i in range(2, N + 1, 2):
    s = s + i
print(s)
'''

#Sum of Series 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4)...
'''
s = 0
for i in range(1, 5):
    for j in range(1, i + 1):
        s = s + j
print(s)
'''



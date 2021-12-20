# How many digits in the number

def find_digit_recur(n):
    if n == 0:
        return n
    return 1 + find_digit_recur(n//10)
    
# print(find_digit_recur(12345))        


# find integer exponentiation

def exponent(x, y):
    if y == 0:
        return 1
    else:
        return x * exponent(x, y - 1) 

def exponent_another(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return exponent_another(x, y // 2) * exponent_another(x, y // 2)
    else:
        return x * exponent_another(x, y // 2) * exponent_another(x, y // 2)        

# print(exponent_another(2, 3))

def summation(num_list):
  if len(num_list) == 0:
    return 0
  if num_list[-1] % 2 == 0:
    return num_list[-1] + summation(num_list[:-1])
  else:
    return summation(num_list[:-1])

# a = summation([1,2,3,4,6, 10,11,121,1009])
a = summation([10,100,1000,901])
print(a)

# def fib(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fib(n-1)+fib(n-2)
# for i in range(0,5):
#    print(fib(i),end=" ")


# l=[]
# def convert_number(num):
#     if(num==0):
#         return l
#     digit = num % 2
#     l.append(digit)

# convert_number(2)  
# convert_number(6)
# l.reverse()
# for i in l:
#     print(i,end="")

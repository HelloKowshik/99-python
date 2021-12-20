def factorial1(n):
    if n == 1:
        return 1
    else:
        return n * factorial1(n - 1)


# print(factorial1(int(input('Enter: '))))          

def get_sum1(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i

    return sum 

def get_sum1_recur(n):
    if n == 0:
        return 0
    else:
        return n + get_sum1_recur(n - 1)  


def reverse_list(A):
    new_list = []
    for i in range(0, len(A)):
        new_list.append(0)
    for i in range(len(A) - 1, -1, -1):
        new_list[len(A) - 1 - i] = A[i]

    return new_list        


def reverse_list_recur(A):
    if len(A) == 0:
        return []
    else:
        return [A[-1]] + reverse_list_recur(A[:-1])


def fibo_recur(n):
    if n <= 1:
        return n
    return fibo_recur(n - 1) + fibo_recur(n - 2)

        
print(fibo_recur(6))       

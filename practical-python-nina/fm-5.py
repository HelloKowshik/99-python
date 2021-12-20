def add(*args):
    total_sum = 0
    for i in args:
        total_sum += i

    return total_sum

# x = add(12, 13, 12, 21, 23, 45)
# print(x)


def factorial(num):
    if num <= 0:
        return 1
    return num * factorial(num - 1)


lambdaFunc = lambda a, b: a + b
lambdaFunc1 = lambda i: i + 2
lambdaFunc2 = lambda j: j % 2 == 0
lambdaFunc3 = lambda elem: elem[1] >= 2.6
lambdaFunc4 = lambda elem: len(elem[0]) <= 6

def filter_func(iterator):
    iterator_obj = dict()
    for key, val in iterator.items():
        if val >= 2.6:
            iterator_obj[key] = val
    return iterator_obj


def mail_user(iterator):
    mail_list = []
    for u_name, mail in iterator.items():
        if len(u_name) <= 8:
            mail_list.append(mail)
    return mail_list


list1 = [2, 3, 4, 5, 6, 7, 8]
song_names = {'oviman': 2.2, 'ovijog': 2.5, 'chole jawa': 1.5, 'bosen bosen': 2.9, 'taheri dj': 3.5}
user_names = {'user_1': 'u@mail.com', 'user_two': 'u2@mail.com', 'user_22': 'u3@mail.com', 'user_four23': 'u4@mail.com'}
filtered_obj = filter_func(song_names)
listAdd = map(lambdaFunc1, list1)
listFilter = filter(lambdaFunc2, list1)
listFilter1 = filter(lambdaFunc3, song_names.items())
listFilter2 = filter(lambdaFunc4, user_names.items())
listFilter3 = filter(lambda x: len(x[0]) <= 8, user_names.items())
res = mail_user(user_names)
print(res)
# print(dict(listFilter3))
# print(dict(listFilter1))
# print(list(listFilter))
# print(list(listAdd))
# y = factorial(int(input('Enter Number: ')))
# print(lambdaFunc(5, 10))

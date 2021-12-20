import logging
# def square(x):
#     temp = x ** 2
#     print(temp)
#     return

# def main():
#     for i in range(1, 11):
#         square(i)

# if __name__ == '__main__':
#     main()            


# logging.basicConfig(filename='test.log', level=logging.INFO)

# logging.debug('This is a debug message.')
# logging.info('This is an informational message.')
# logging.error('This is an error message.')


logging.basicConfig(filename='test.log', level=logging.INFO)

a = 10
b = 0

try:
    temp = a/b
    print(temp)
except ZeroDivisionError as e:
    logging.exception(e)

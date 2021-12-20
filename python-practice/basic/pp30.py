# my_file = open('file1.txt', 'r')
# content = my_file.read()
# # print(content)
# my_file.close()
# # print(my_file.read())

# my_file = open('file1.txt', 'w+')
# content = my_file.write('The file is overwritten!')
# print(my_file.read())

# for i in range(1, 101):
#     with open('file1.txt', 'a') as f:
#         f.write(f'{str(i)} ')


with open('file1.txt', 'r') as p:
    c = p.read()
    for i in c.split():
        print(i)


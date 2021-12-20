f = open('test.txt', 'w')
f.write('1221')
f.close()

file = open('test.txt', 'r')
content = list(file.read())
# print(content)
file.close()
is_palindrome = True
for i in range(int(len(content)/2)):
    # print(content[i])
    if content[i] != content[len(content)-i- 1]:
        is_palindrome = False

if is_palindrome:
    file_n = open('test.txt', 'a')
    file_n.write('-palindrome')
    file_n.close()

else:
   file_n = open('test.txt', 'a')
   file_n.write('-Not palindrome')
   file_n.close() 

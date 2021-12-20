import os
import shutil

path = 'C:\\Users\\lenovo\\Desktop\\testHtml.html'

# if os.path.exists(path):
#     print('File Exists!')
# else:
#     print('File Not found!')    
text = 'Automate Boring Stuff with Python.\n'
# try:
#     with open('test.text', 'a') as file:
#         # print(file.read())
#         file.write(text)

# except FileNotFoundError as e:
#     print(e)    

# shutil.copyfile('test.text', 'test.txt')
# shutil.copy('test.text', 'test.txt')
# x = shutil.copy2('test.text', 'test.txt')

src = 'test.text'
dst = 'C:\\Users\\lenovo\\Desktop\\test.text'
dst = 'D:\\99-python\\testfile.csv'
# print(os.getcwd())

try:
    if os.path.exists(dst):
        print('File is Already there!')
    else:
        os.replace(src, dst)
        print('Copied!')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

dict1 = {'name': 'Kowshik', 'mail': 'hello@kowshik.com'}
dict1['phone'] = '0171123'
dict2 = {}
dict2.update(dict1)
dict3 = dict2.copy()
dict1['hometown'] = 'Cumilla'
# print(f'dict1: {dict1}\ndict2: {dict2}\ndict3: {dict3}')
# print(dict1.get('mail', 'Not Found'))
# w, x, y, z = dict1.items()
# print(f'{w[1]},{x},{y},{z}')
a = [1, 2, 3]
b = a
# print(a is b)
# print(a == b)

b = a[:]
# print(a is b)
# print(a == b)

# inp = int(input('Enter: '))

# if inp % 3 == 0 and inp % 5 == 0:
#     print('YES')
# else:
#     print('No')    

# char = input('Enter The Character: ')
# if char >= 'a' and char <= 'z':
#     print(f'{char} is small letter')
# else:
#     print(f'{char} is capital letter')  

vowels = ['a', 'e', 'i', 'o', 'u']
letter = input('Enter a character: ')

if letter.lower() >= 'a' and letter.lower() <= 'z':
    if letter.lower() in vowels:
        print(f'{letter} is Vowel')
    else:
        print(f'{letter} is Consonant')      
else:
    print(f'{letter} is not Alphabet') 


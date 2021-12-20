import pprint as pp
# Count the frequency of character in String

text = 'Count the frequency of character in String'
letters = {}

for i in text.lower():
    letters.setdefault(i, 0)
    letters[i] = letters[i] + 1

# pp.pprint(letters)    

# Password simulation / password protected simulation

'''
user_list = {'user1@mail.com': 123, 'user2@mail.com': 456, 'user3@mail.com': 789}

tries_left = 0
user_found = False

while(tries_left < 5):
    user_name = input('Enter Your Username: ')
    if user_name in user_list:
        for i in range(0, 3):
            password = int(input('Enter Your Password: '))
            if password in user_list.values():
                user_found = True
                print('Welcome, '+ str(user_name)+'!')
                break
            else:
                print('Incorrect Password! Try Again, you have ' + str(2 - i)+' tries left.')
    else:
        print('Username Not Found! Try Again: ')

    tries_left = tries_left + 1  

    if user_found:
        break
'''                          

contacts = {'john': 1122, 'doe': 2122, 'smith': 9090, 'samsi': 4567}
flag = 0

while flag < 5:
    name = input('Enter The Name(Press ENTER to exit.): ')
    if name == '':
        break
    if name in contacts:
        print(name + '-' + str(contacts[name]))
        break
    else:
        print('No Such Contact in the list. Add this to Contact? Y/N ')
        reply = input()
        if reply == 'Y':
            phone = int(input('Enter Phone Number: '))
            contacts[name] = phone
            print('Contact Added!')
            break
        else:
            print('Search Again')
    flag = flag + 1                   

# print(contacts)

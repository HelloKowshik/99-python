# Bank Database System

bank_db = {'Alice': 1290, 'Samsi': 1090, 'Gurbaz': 370, 'Mujib': 1890}

while True:
    print('1. Check Balance')
    print('2. Check Info')
    print('3. Update Balance')
    print('4. Exit')
    choice = int(input())
    if choice == 1:
        name = input('Enter Your Name: ')
        if name in bank_db.keys():
            print('Hello, '+ str(name)+'. Your Balance = '+str(bank_db[name]))
            break;
        else:
            print('Invalid User. Want to Register? Y / N:')
            prompt = input()
            if prompt == 'Y':
                balance = int(input('Enter Balance: '))
                bank_db.update({name: balance}) 
                break;
            else:
                print('Want to exit?')
                prompt = input()
                if prompt == 'Y':
                    break
    elif choice == 2:
        for n,v in bank_db.items():
            print(n + str(v))
    elif choice == 3:
        name = input('Enter Name: ')   
        if name in bank_db.keys():
            prompt = input('ADD or Subtract(A / S): ')
            if prompt == 'A':
                old_balance = bank_db[name]
                balance = int(input('Enter Balance: '))
                bank_db[name] = old_balance + balance
                print('Balance Updated!' + str(bank_db[name]))
                break
            elif prompt == 'S':
                old_balance = bank_db[name]
                balance = int(input('Enter Balance: '))
                bank_db[name] = old_balance - balance
                print('Balance Updated!' + bank_db[name]) 
                break 
        else:
            print('Account Not Found!')
    else:
        break              

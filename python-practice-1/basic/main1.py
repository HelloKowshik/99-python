import time
website1 = 'http://www.facebook.com'
website1 = 'http://www.microsoft.com'
website1 = 'http://www.chaldal.com'
website1 = 'http://www.mail.google.com'

slice = slice(11, -4)
# print(website1[slice])

# for second in range(10, 0, -1):
#     print(second)
#     time.sleep(1)
# print('Happy New Year!')    

phone_num = '01959-97 95 84'

for d in phone_num:
    if d == '-' or d == ' ':
        continue
    print(d,end='')    

import re

my_string = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
temp = my_string.split(',')
for mail in temp:
    email = re.search('([\w\.-]+)@([\w\.-]+)', mail)
    print(list(email.group()))

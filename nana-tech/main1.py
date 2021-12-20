# import helpers
from helpers import validate_and_execute


user_input = ''
while user_input != 'exit':    
    user_input = input('Enter The Number of days: ')

    # for item in user_input.split(','):
    # for item in set(user_input.split(',')):
    #     validate_and_execute()

    items = user_input.split(':')
    items_dict = {'days': items[0], 'unit': items[1]}
    # helpers.validate_and_execute(items_dict)
    validate_and_execute(items_dict)


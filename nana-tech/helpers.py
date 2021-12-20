def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return f'{num_of_days} days are {num_of_days * 24} {conversion_unit}'
    elif conversion_unit == 'minutes':
        return f'{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}'
    elif conversion_unit == 'seconds':
        return f'{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}'    
    else:
        return f'Unsupported Format!'        
    

def validate_and_execute(items_dict):
    # if user_input.isdigit():
    try:
        user_inp = int(items_dict['days'])
        if user_inp > 0:
            print(days_to_units(user_inp, items_dict['unit']))
        elif user_inp == 0:
            print('You Entered Zero!')
        else:
            print('Negative Number!')
                                     
    except ValueError:
        print('Invalid input!')

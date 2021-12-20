try:
    numerator = int(input('Enter a value: '))
    denominator = int(input('Enter Another Value: '))
    result = numerator // denominator

except ZeroDivisionError as e:
    print('divide by zero not allowed!', e)

except ValueError as e:
    print('Only numbers Acceptable!', e)

except Exception as e:
    print('Unknown!', e)

else:
    print(result)

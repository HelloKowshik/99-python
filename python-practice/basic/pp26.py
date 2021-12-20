bill = int(input('Enter Bill Amount: '))

bill_copy = bill

temp = bill_copy // 1000
print(f'{temp} 1000 taka note(s)')
if temp > 0:
    bill = bill % 1000
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 500
print(f'{temp} 500 taka note(s)') 
if temp > 0:
    bill = bill % 500
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 100
print(f'{temp} 100 taka note(s)')
if temp > 0:
    bill = bill % 100
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 50
print(f'{temp} 50 taka note(s)')
if temp > 0:
    bill = bill % 50
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 20
print(f'{temp} 20 taka note(s)')
if temp > 0:
    bill = bill % 20
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 10
print(f'{temp} 10 taka note(s)')
if temp > 0:
    bill = bill % 10
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 5
print(f'{temp} 5 taka note(s)')
if temp > 0:
    bill = bill % 5
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 2
print(f'{temp} 2 taka note(s)')
if temp > 0:
    bill = bill % 2
    bill_copy = bill
else:
    bill = bill_copy

temp = bill // 1
print(f'{temp} 1 taka note(s)')

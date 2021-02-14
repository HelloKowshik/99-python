phoneBook = {'name': 'John Doe', 'email': 'john@doe.com'}
# print(type(phoneBook))
# print(phoneBook.get('name'));
payment_list = [2000, 3000, 3500, 4000, 3000, 6000]
total_payment = 0;
for payment in payment_list:
    total_payment += payment

print(f"Total Payment: {total_payment}")

def func(inp):
    if inp <= 0:
        print("Invalid Input Provided!")
    for i in range(1, inp):
        print(i)


func(5)

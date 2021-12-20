def calculate_tax(monthly_income, tax_rate=0.15):
    return monthly_income * tax_rate

# x = float(input("Enter Your Monthly Income: "))
# y = float(input("Enter Tax Rate: "))
# z = "{:.2f}".format(calculate_tax(x, y))
# print(f"Monthly Income: {x} , Tax Rate: {y} , Payable Tax: {z}")

def test_func(xx, yy=None):
    if yy is None:
        yy = []
    yy.append(xx)
    print(yy)


test_func(5)
test_func(11)

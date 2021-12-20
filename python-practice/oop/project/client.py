from tech_product import Tech
from laptop_tech import Laptop
from mobile_tech import Mobile
from sales_person import SalesPerson
from datetime import date

phone_1 = Mobile('iPhone_11', 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile('iPhone_12', 70000, 550, 'Silver', '1920-1080', 12)
phone_2 = Mobile('iPhone_13', 80000, 580, 'Project Red', '1920-1080', 13)

laptop_1 = Laptop('Asus G-14', 130000, 1.6, 'Moonlight Silver', 16, 'Ryzen 4888H', 1000)
laptop_2 = Laptop('Macbook Pro-13', 130000, 1.7, 'Dark Grey', 8, 'intel core i5', 256)
laptop_3 = Laptop('Dell XPS 13', 140000, 1.4, 'White', 16, 'intel core i7', 512)


print(phone_1)
phone_1.apply_discount()
print('-------------------------------')
print(phone_1.price)
print('-------------------------------')
print(Tech.total_products)
print('-------------------------------')
print(laptop_1)
print('-------------------------------')
print(laptop_1.calculate_shipping_cost(10))
print('-------------------------------')
laptop_1.set_double_price()
print(laptop_1.price)
print('-------------------------------')
laptop_1.change_specs(32, 2000)
print(laptop_1.price)
print('-------------------------------')
sales_person_1 = SalesPerson('Majed', 'Ali', 40000, date(2021, 11, 29))
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(laptop_1)
sales_person_1.sell_product(laptop_2)
print(sales_person_1.total_products_sold())
print('-------------------------------')
sales_person_1.display_sales()
print('-------------------------------')
sales_person_1.sort_by_price()
sales_person_1.display_sales()

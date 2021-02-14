customer_name = input("Customer Name: ")
room_no = input("Room NO: ");
per_day_bill = float(1200.00);
total_day = int(input("How Many Days? "));
total_bill = per_day_bill * total_day;
final_greeting = f"Thanks, {customer_name}, Room NO: {room_no}, Your Total Bill: {total_bill}"
print(final_greeting);
from datetime import datetime
goal, deadline = input('Enter Goal:Deadline: ').split(':')
deadline = datetime.strptime(deadline, '%d.%m.%y')
current_date = datetime.today()
time_remains = deadline - current_date
print(f'You have {time_remains.days} days remaining to complete {goal}')

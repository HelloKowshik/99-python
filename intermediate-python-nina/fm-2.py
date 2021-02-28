names = ['hasib', 'hamid', 'jason roy', 'alex cary', 'steve smith']
players_list = ['kane wiliamson', 'steve smith', 'joe root', 'virat kohli']
players_with_country = [('Kane Wiliamson', 'NZ'), ('Steve Smith', 'AUS'),
                        ('Virat Kohli', 'IND'), ('Joe Root', 'ENG'), ('Babar Azam', 'PAK')]
list_comprehension1 = [len(name) for name in names]
list_comprehension2 = [(name_len, len(name_len)) for name_len in names]
list_comprehension3 = ",".join([f":{player}" for player in players_list])
lottery_numbers_str = "12, 34, 56, 21, 10, 134, 89"
lottery_numbers_list = [int(item) for item in lottery_numbers_str.split(', ')]
list_comprehension4 = ','.join([f"{name} ({country}) " for name, country in players_with_country])

print(list_comprehension4)
# print(lottery_numbers_list, max(lottery_numbers_list), min(lottery_numbers_list), sum(lottery_numbers_list))

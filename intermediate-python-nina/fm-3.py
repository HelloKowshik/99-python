import random
set_comprehension1 = {num * num for num in range(1, 11) if num % 2 == 0}
sorted_set_comprehension = sorted(set_comprehension1)
dict_comprehension1 = {num: num * num for num in range(1, 11) if num % 2 == 0}
dict_comprehension2 = {x: x * x for x in range(1, 6)}
player_name_list = ['Tamim Iqbal', 'Mushfiqur Rahim', 'Shakib AL Hasan', 'Mahmudulla Riyad', 'Mehedy Hasan']
player_match_list = [201, 192, 199, 143, 35]
player_runs_list = [5678, 5455, 6200, 3600, 785]
player_profile_dict = zip(player_name_list, player_match_list, player_runs_list)
# for player in player_profile_dict:
#     print(player)

player_details_comprehension = ', '.join([f"{name}- Match: {match}- Run: {runs}" for name, match, runs in player_profile_dict])
print(player_details_comprehension)

simple_number_dict = {n: random.randint(1, 100) for n in range(1, 6)}
# print(simple_number_dict)
# print(dict_comprehension2)
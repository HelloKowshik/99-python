cities_temp_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_temp_in_C = {k: int((0.56 * (v - 32))) for k,v in cities_temp_in_F.items()}

weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}

sunny_weather = {k: v for k, v in weather.items() if v == 'sunny'}

weather_report = {k: 'Warm' if v >= 50 else 'Cloudy' for k,v in cities_temp_in_F.items()}

# print(weather_report)

usernames = ['Dudes', 'Bro', 'Mister']
passwords = ('p@ssword', 'abc123', 'guest')
login_dates = ['1/2/2021', '12/5/2021', '19/9/2021']
users = list(zip(usernames, passwords))
users = dict(zip(usernames, passwords))
users = zip(usernames, passwords)
users = list(zip(usernames, passwords, login_dates))
for i in users:
    print(i)
# print(users)

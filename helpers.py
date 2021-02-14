def to_upper(name):
    return name.upper()

def to_lower(name):
    return name.lower()

def get_length(str):
    new_str = ''
    new_str = new_str.join(str.split(' '))
    str_len = 0
    for i in new_str:
        str_len += 1
    return str_len

# import helpers
# x = 'anik'
# print(helpers.get_length(x))

# import requests
# api_url = "http://shibe.online/api/shibes?count=1"
# response = requests.get(api_url)
# status_code = response.status_code
# data = response.json()
# print(status_code, data)

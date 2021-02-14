import requests
api_url = 'http://shibe.online/api/shibes?count=1'
another_api_url = 'https://cat-fact.herokuapp.com/facts'
response = requests.get(another_api_url)
json_data = response.json()
print("USER_ID - TYPE - TEXT")
for data in json_data:
    print(f"{data['_id']} - {data['type']} - {data['text']}")


# print(type(json_data))
data_item = {'BD': 'DHAKA', 'PAK': 'ISLAMABAD', 'AUS': 'CANBERA'}
ytb_channels = ['Stack Learner', 'Clever Programming', 'freeCodeCamp', 'Traversy Media']
tot_followers = ['1.5 M', '6 M', '8.5 M', '7.25 M']
dict_comp = dict({channel: followers for channel, followers in zip(ytb_channels, tot_followers)})
# with open('data.txt', 'w+') as dummy:
#     for i in range(1, 6):
#         dummy.write('Hello, World! ')


with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

# with open('data.txt', 'w+') as data:
#     formatted_data = str(dict({channel: followers for channel, followers in zip(ytb_channels, tot_followers)}))
#     data.write(formatted_data)

# with open('data.txt', 'a+') as data:
#     formatted_data = str({'USA': 'NEWYORK'})
#     data.write(formatted_data)


# print(data_item, type(data_item))
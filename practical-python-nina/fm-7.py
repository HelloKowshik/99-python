data = ['python', 'react.js', 'nodeJs', 'SQL', 'express.js']
# for lang in enumerate(data):
#     print(lang)

lengths = [len(item) for item in data]
list_comp = [item for item in data if len(item) >= 8]
my_days = '-done, '.join([str(dates) for dates in range(1, 10)])
gen_comp = (days for days in range(1, 6))
set_comp = {item for item in data if len(item) % 2 == 0}
num_list1 = [i for i in ['A', 'B', 'C']]
num_list2 = [i for i in ['a', 'b', 'c']]
num_list = list(zip(num_list1, num_list2))
ytb_channels = ['Stack Learner', 'Clever Programming', 'freeCodeCamp', 'Traversy Media']
tot_followers = ['1.5 M', '6 M', '8.5 M', '7.25 M']
dict_comp = dict({channel: followers for channel, followers in zip(ytb_channels, tot_followers)})
text_1 = 'Hello'
text_2 = text_1[1:]
print(text_2)

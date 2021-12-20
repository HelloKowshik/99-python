def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


x = count_letters('AABC BSD')
# print(x)

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}


# for cloths, name in wardrobe.items():
#     for item in name:
#         print("{} {}".format(item, cloths))


def email_list(domains):
    emails = []
    for mail_type, users in domains.items():
        for user in users:
            emails.append(user + "@" + mail_type)
    return emails


# print(email_list(
    # {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     # "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    for groups, users in group_dictionary.items():
        for user in users:
            user_groups[user] = user_groups.get(user, []) + [groups]
    return user_groups


# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

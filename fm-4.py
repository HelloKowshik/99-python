area_list = []
area_list.append("Bohaddarhat")
area_list.insert(0, "Cosmopolition")
list1 = ["Hello", "World"]
list2 = ["Wellcome", "Bye", "New York", "Boston", "LA", "West Virginia", "Gabon"]
list1.extend(list2)
pos = list1.index("Wellcome")
list1[pos] = "Beijing"

def check_item(lists, item):
    pos1 = lists.index(item.upper())
    print(f"{item.upper()} found in INDEX: {pos1}")


list1 = ["A", "B", "C", "D", "E"]
check_item(list1, "d")
print(list1, "Wellcome" in list1)
list1 = [1, 2, 3, 4]
tp = list1[0], list1[1], list1[2], list1[3]
print(tp.index(4))
# print(area_list)
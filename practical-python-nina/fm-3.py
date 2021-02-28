#Set

fruits = {'apple', 'banana', 'grapes', 'orange', 'pineapple', 'dates', 'guava'}
# print(type(fruits))
fruits.add('another fruit')
fruits.update({'potato', 'cabage', 'carrot'})
fruits.discard('another fruit1')
# fruits.remove('another fruit1') //KeyError
# x = fruits.pop()
# fruits.clear()
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}
nums = num1.union(num2)
nums1 = num1.intersection(num2)
nums2 = num1.difference(num2)
print(nums2)

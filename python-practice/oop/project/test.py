def modify_num(number):
  number **= 2
  return lambda num: num ** number
  
print(modify_num(2)(3))

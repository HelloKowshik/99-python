people = ['Matt', 'Bryan', 'Tammy', 'Markus'];
lengths1 = list(map(lambda name: len(name), people));
lengths2 = list(map(len, people));
# print(lengths2);

firstname = ('Apple', 'Choclate', 'Fudge', 'Pizza');
lastname = ('Pie', 'Cake', 'Brownies');
mergeNames = list(map(lambda a, b: a + ' '+ b, firstname, lastname))
# print(mergeNames);

add = lambda a, b: a + b;
sub = lambda a, b: a - b;
mul = lambda a, b: a * b;
div = lambda a, b: a / b;
doAll = lambda func, num: func(num[0], num[1]);
f = (add, sub, mul, div);
v = [[6, 3]];
n = list(v) * len(f);
m = list(map(doAll, f, n))
print(m);

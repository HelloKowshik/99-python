class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

    def __str__(self):
        return f'class: Point2D, x = {self.x}, y = {self.y}' 

    def __add__(self, other):
        # print(f'{self}, {other}, {other.__class__}, {isinstance(self, other.__class__)}')
        if isinstance(self, other.__class__):
            return Point2D(self.x + other.x, self.y + other.y) 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y           

p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
# print(p1)               
# print(repr(p2))
print(p1 == p2)
print(p1 is p2)

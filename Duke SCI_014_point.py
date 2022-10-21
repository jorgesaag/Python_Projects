import math

class Point:
    """Point class, which represents the x- and y- position of a point in the Cartesian plane."""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from(self, pt):
        distance = math.sqrt((self.x - pt.x) ** 2 + (self.y - pt.y) ** 2)
        return distance


p = Point()
p_copy = p
p_copy = p_copy.move(1, 4)
print(p_copy.x)
print(p_copy.y)
print(p.distance_from(p_copy))


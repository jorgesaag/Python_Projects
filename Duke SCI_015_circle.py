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


class Circle():
    """Circle class, which represents a circle with a radius "radius" and center "center"."""
    center = Point(0, 0)
    radius = 1

    def __init__(self, c=Point(0, 0), r=1):
        self.center = c
        self.radius = r

    def __str__(self) -> str:
        return f"({self.center}, {self.radius})"

    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def intersection_area(self, other):
        A = self.center
        B = other.center
        dist = ((A.x-B.x)**2 + (A.y-B.y)**2)**(0.5)
        if dist >= (self.radius + other.radius):
            return 0
        elif dist <= abs(self.radius - other.radius):
            return math.pi * min((self.radius)**2, (other.radius)**2)
        else:
            a = self.radius**2
            b = other.radius**2
            x = (a-b + dist**2) / (2*dist)
            z = x**2
            y = (a-z)**(0.5)
            d = dist - x
            return (a * math.acos(x / self.radius)) - (x * y) + \
                   (b * math.acos(d / other.radius)) - (d * (b - d)**(0.5))


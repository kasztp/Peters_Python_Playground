from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x), (self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, int):
            return Point((self.x * other), (self.y * other))
        else:
            return (self.x * other.x) + (self.y * other.y)

    def __rmul__(self, other):
        if isinstance(other, int):
            return Point((self.x * other), (self.y * other))
        else:
            return (self.x * other.x) + (self.y * other.y)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Cluster:
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        self.center = Point(sum(x) / len(self.points), sum(y) / len(self.points))
        print(self.center)

    def add_point(self, point):
        self.points.append(point)


def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1, 0)
    b = Cluster(-1, 0)
    a_old = []
    for _ in range(10000):  # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = a.points
        a.update()
        b.update()
        a.points = []
        b.points = []
    if a.center.x > b.center.x:
        return [(a.center.x, a.center.y), (b.center.x, b.center.y)]
    return [(b.center.x, b.center.y), (a.center.x, a.center.y)]


dataset = [(1, 1), (-1, -1), (2, 2), (-2, -2), (3, 3), (-3, -3),
           (0, -2), (-2, 0), (0, -3), (-3, 0), (5, 6), (-5, -6)]

print(compute_result(dataset))

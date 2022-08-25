""" Library for 2D point representation and basic K-means clustering. """
from math import sqrt
from typing import Union


class Point:
    """ Representation of a 2D point.

    Attributes
    ----------
    x : int
        x-coordinate of the point.
    y : int
        y-coordinate of the point.

    Methods
    -------
    __repr__()
        Returns a string representation of the point.
    __eq__(other)
        Returns True if the points are equal, False otherwise.
    __add__(other)
        Returns the sum of the point and the other point.
    __sub__(other)
        Returns the difference of the point and the other point.
    __mul__(other)
        Returns the dot product of the point and the other point.
        Returns the product of the point and an integer.
    __rmul__(other)
        Returns the dot product of the point and the other point.
        Returns the product of the point and an integer.
    distance(other)
        Returns the distance between the point and the other point.

    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        return Point((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: 'Point') -> 'Point':
        return Point((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Union['Point', int]) -> Union['Point', int]:
        if isinstance(other, int):
            return Point((self.x * other), (self.y * other))
        return (self.x * other.x) + (self.y * other.y)

    def __rmul__(self, other: Union['Point', int]) -> Union['Point', int]:
        if isinstance(other, int):
            return Point((self.x * other), (self.y * other))
        return (self.x * other.x) + (self.y * other.y)

    def distance(self, other: 'Point') -> float:
        """ Returns the distance between the point and the other point."""
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Cluster:
    """ Representation of a cluster.

    Attributes
    ----------
    center : Point
        Center of the cluster.
    points : list of Point
        Points in the cluster.

    Methods
    -------
    __repr__()
        Returns a string representation of the cluster.
    __eq__(other)
        Returns True if the clusters are equal, False otherwise.
    update()
        Updates the center of the cluster.
    add_point(point)
        Adds a point to the cluster.

    """
    def __init__(self, x: int, y: int):
        self.center = Point(x, y)
        self.points = []

    def __repr__(self):
        return f'Cluster{self.center.x, self.center.y}'

    def __eq__(self, other: 'Cluster') -> bool:
        return self.center == other.center and self.points == other.points

    def update(self):
        """ Updates the center of the cluster. """
        center_x = [point.x for point in self.points]
        center_y = [point.y for point in self.points]
        self.center = Point(sum(center_x) / len(self.points), sum(center_y) / len(self.points))
        print(self.center)

    def add_point(self, point: 'Point'):
        """ Adds a point to the cluster. """
        self.points.append(point)


def compute_result(points: list['Point'], max_iterations: int) -> list[tuple[int, int]]:
    """ Computes the result of the K-means clustering algorithm.

    Parameters
    ----------
    points : list of Point
        Points to be clustered.
    max_iterations : int
        Maximum number of iterations to perform.

    Returns
    -------
    list of tuple[int, int]
        Result of the K-means clustering algorithm.

    """
    points = [Point(*point) for point in points]
    cluster_a, cluster_b = Cluster(1, 0), Cluster(-1, 0)
    previous_cluster_points = []
    for _ in range(max_iterations):
        for point in points:
            if point.distance(cluster_a.center) < point.distance(cluster_b.center):
                cluster_a.add_point(point)
            else:
                cluster_b.add_point(point)
        if previous_cluster_points == cluster_a.points:
            break
        previous_cluster_points = cluster_a.points
        cluster_a.update()
        cluster_b.update()
        cluster_a.points, cluster_b.points = [], []
    if cluster_a.center.x > cluster_b.center.x:
        return [(cluster_a.center.x, cluster_a.center.y), (cluster_b.center.x, cluster_b.center.y)]
    return [(cluster_b.center.x, cluster_b.center.y), (cluster_a.center.x, cluster_a.center.y)]

""" Unit test for the K-means clustering algorithm. """
from Algorithms.k_means_clustering import (
    Point,
    Cluster,
    compute_result
)

TEST_DATASET = [(1, 1), (-1, -1), (2, 2), (-2, -2), (3, 3), (-3, -3),
           (0, -2), (-2, 0), (0, -3), (-3, 0), (5, 6), (-5, -6)]


def test_point_class():
    """ Test Point class. """
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2
    assert repr(point) == "Point(1, 2)"
    assert point.distance(Point(1, 2)) == 0
    assert point.distance(Point(3, 2)) == 2.0
    assert point.distance(Point(1, 1)) == 1.0
    assert point * point == 5


def test_cluster_class():
    """ Test Cluster class. """
    cluster = Cluster(1, 0)
    assert cluster.points == []
    assert repr(cluster) == "Cluster(1, 0)"
    cluster.add_point(Point(1, 1))
    assert cluster.points == [Point(1, 1)]
    cluster.update()
    assert cluster.center == Point(1, 1)
    cluster.add_point(Point(2, 2))
    assert cluster.points == [Point(1, 1), Point(2, 2)]
    cluster.update()
    assert cluster.center == Point(1.5, 1.5)
    cluster.add_point(Point(3, 3))
    assert cluster.points == [Point(1, 1), Point(2, 2), Point(3, 3)]
    cluster.update()
    assert cluster.center == Point(2, 2)


def test_compute_results():
    """ Test compute_results() algorithm. """
    assert compute_result(TEST_DATASET, 1000) == [(2.75, 3.0), (-2.0, -2.125)]

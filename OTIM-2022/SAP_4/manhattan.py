import os
from time import time


path = os.getcwd() + "/OTIM-2022/SAP_4/"

with open(path + "manhattan2.in.txt", "r", encoding="utf8") as f:
    contents = f.readlines()
    n = len(contents)
    points = []
    for line in contents:
        points.append([int(x) for x in line.strip().split()])

print(n)
#print(points)


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calculate_grid_size(points):
    """ Calculate the grid size from the points """
    x = max([point[0] for point in points])
    y = max([point[1] for point in points])
    return x, y


def find_optimal_place(points, grid_size):
    """ Return the minimum cumulative distance of points from the optimal shop places selected from the grid where the points are located
    Return the number of optimal shop places.

    Parameters
    ----------
    points : list
        List of points
    grid_size : tuple
        Tuple of the grid size (x, y)

    Returns
    -------
    int
        Minimum cumulative distance of points from the optimal shop places selected from the grid where the points are located
    int
        Number of optimal shop places
    """
    min_distance = 0
    optimal_places = 0
    for x in range(grid_size[0] + 1):
        for y in range(grid_size[1] + 1):
            distance = 0
            for point in points:
                distance += manhattan_distance(point, (x, y))
            if distance < min_distance or min_distance == 0:
                min_distance = distance
                optimal_places = 1
            elif distance == min_distance:
                optimal_places += 1
    return f'{min_distance} {optimal_places}'


start_time = time()
result = find_optimal_place(points, calculate_grid_size(points))
end_time = time()
time_taken = end_time - start_time
print(f'Original - Time taken (seconds): {time_taken} \n')

start_time = time()
result = find_optimal_place(points, calculate_grid_size(points))
end_time = time()
time_taken = end_time - start_time
print(f'Improved - Time taken (seconds): {time_taken} \n')

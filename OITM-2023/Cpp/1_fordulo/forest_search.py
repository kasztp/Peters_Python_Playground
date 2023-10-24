import numpy as np

field = [
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 1,],
    [1, 1, 0, 0, 1, 0, 1, 0, 1, 0,],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1,],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0,],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0,],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0,],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0,],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 1,],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0,]
]


def forest_counter(field):
    """
    Counts the number of forests in the field.
    Forest is a group of trees connected by their sides.

    :param field: list of lists of 0 and 1 representing the trees and grass.
    :return: number of forests in the field
    """
    field = np.array(field)
    forest_counter = 0
    while 1 in field:
        i, j = np.where(np.array(field) == 1)
        field = remove_forest(field, i[0], j[0])
        forest_counter += 1
    return forest_counter


def remove_forest(field, i, j):
    """
    Removes the forest from the field.

    :param field: list of lists of 0 and 1 representing the trees and grass.
    :param i: row index of the tree
    :param j: column index of the tree
    :return: field without the forest
    """
    


if __name__ == '__main__':
    print(forest_counter(field))

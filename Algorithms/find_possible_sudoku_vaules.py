
""" Code for finding possible values for a given position
    in a sudoku grid. Prepared for Stackoverflow question:
    https://stackoverflow.com/questions/73291535/
"""


def possible(grid: list[list[int]], num: int, pos: tuple[int, int]) -> bool:
    """ Returns True if num is a possible value for the given position in the grid.
        Otherwise, returns False.

        Parameters
        ----------
        grid: list[list[int]]
            The sudoku grid.
        num: int
            The number to check for.
        pos: tuple[int, int]
            The position to check for.

        Returns
        -------
        bool
            True if num is a possible value for the given position in the grid.
            Otherwise, returns False.

        """
    # Check row
    if num in grid[pos[0]]:
        return False

    # Check column
    if num in [item[pos[1]] for item in grid]:
        return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        if num in grid[i][box_x * 3: box_x * 3 + 3] \
            and (i, grid[i].index(num)) != pos:
            return False

    return True


sudoku = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

possible_values = []

for n in range(1,10):
    if possible(sudoku, n, (0, 2)):
        possible_values.append(n)


print(possible_values)
possible_values = [n for n in range(1,10) if possible(sudoku, n, (0, 2))]
print(list(possible_values))

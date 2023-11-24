import os
import statistics

def calculate_area_variance_from_file(file_path):
    # Read the data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Parse the first line to get the dimensions of the solar panel and the number of cuts
    W, H, K = map(int, lines[0].split())

    # Parse the remaining lines to get the cuts
    cuts = [list(map(int, line.split())) for line in lines[1:]]

    # Initialize the solar panel as a 2D array
    panel = [[1]*H for _ in range(W)]

    # Apply each cut to the panel
    for cut in cuts:
        X, Y, P, Q = cut
        if X == P:  # Vertical cut
            for i in range(min(Y, Q), max(Y, Q)):
                if panel[X][i] == 1:
                    panel[X][i] = 0
        else:  # Horizontal cut
            for i in range(min(X, P), max(X, P)):
                if panel[i][Y] == 1:
                    panel[i][Y] = 0

    # Find the connected components (i.e., the individual cells)
    cells = label_cells(panel)

    # Calculate the area of each cell
    areas = [sum(cell == i for row in cells for cell in row) for i in range(1, max(max(row) for row in cells) + 1)]

    # Calculate and return the variance of the areas
    return round(statistics.variance(areas), 2)

def label_cells(panel):
    W, H = len(panel), len(panel[0])
    label = [[0]*H for _ in range(W)]
    current_label = 1

    for i in range(W):
        for j in range(H):
            if panel[i][j] == 1 and label[i][j] == 0:
                cells_to_label = [(i, j)]
                while cells_to_label:
                    x, y = cells_to_label.pop()
                    if 0 <= x < W and 0 <= y < H and panel[x][y] == 1 and label[x][y] == 0:
                        label[x][y] = current_label
                        cells_to_label.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
                current_label += 1

    return label


for file in os.listdir():
    if file.endswith("a.txt"):
        print(f"The variance of the areas in {file} is {calculate_area_variance_from_file(file):.2f}")

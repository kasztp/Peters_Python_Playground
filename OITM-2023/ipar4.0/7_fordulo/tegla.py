import numpy as np


def load_data(filename: str) -> (int, int, int, list):
    """Load the data from the given text file.
    Return the area details and a list of tuples containing the data.
    
    :param filename: str - the name of the CSV file
    :return: int, int, int, list - the data
    """
    data = []
    with open(filename, encoding='utf-8') as f:
        width, height, num_chips = map(int, f.readline().split())
        for line in f:
            data.append(tuple(map(int, line.split())))
    return width, height, num_chips, data


def mark_chips(chips):
    """
    Mark the chips on the silicon slice.

    :param silicon: numpy.ndarray - the silicon slice
    :param chips: list - the list of chips
    """
    silicon = np.zeros((H, W))
    for chip in chips:
        X, Y, w, h = chip
        silicon[Y:Y+h, X:X+w] = 1
    return silicon


def max_free_rectangle(width, height, chips):
    """Find the maximum free rectangle in the silicon slice.
    Return the area of the maximum free rectangle.

    :param width: int - the width of the silicon slice
    :param height: int - the height of the silicon slice
    :param chips: list - the list of chips

    :return: int - the area of the maximum free rectangle
    """
    # Initialize silicon slice
    silicon = mark_chips(chips)

    # Find max rectangle
    max_area = 0
    for i in range(height):
        for j in range(width):
            for h in range(1, height-i+1):
                for w in range(1, width-j+1):
                    # Check if the rectangle is free
                    if sum(sum(silicon[i+k][j:j+w]) for k in range(h)) == 0:
                        max_area = max(max_area, w*h)

    return max_area


def max_rectangle_hist(bin_matrix):
    """Find the maximum rectangle in a binary matrix.
    Return the area of the maximum rectangle.

    :param bin_matrix: list - the binary matrix
    :return: int - the area of the maximum rectangle
    """
    max_area = 0
    col = len(bin_matrix[0])
    hist = [0] * col
    for _, row_vals in enumerate(bin_matrix):
        for j, val in enumerate(row_vals):
            if val == 0:
                hist[j] += 1
            else:
                hist[j] = 0
        stack = []
        max_area_in_row = 0
        for k, h in enumerate(hist):
            while stack and (h <= hist[stack[-1]]):
                h_inner = hist[stack.pop()]
                w_inner = k if not stack else k - stack[-1] - 1
                max_area_in_row = max(max_area_in_row, w_inner * h_inner)
            stack.append(k)
        max_area = max(max_area, max_area_in_row)
    return max_area


# Teszt Példa
W, H, K = 10, 10, 3
chips = [(2, 1, 1, 1), (1, 7, 4, 2), (8, 2, 1, 3)]
print(max_free_rectangle(W, H, chips))

# Teszt Példa v2
marked_silicon = mark_chips(chips)
print(max_rectangle_hist(marked_silicon))

# Teszt inputra
W, H, K, chips = load_data("teszt_input_7forduló.txt")
marked_silicon = mark_chips(chips)
print(max_rectangle_hist(marked_silicon))
print(max_free_rectangle(W, H, chips))

for i in range(2, 5):
    W, H, K, chips = load_data(f"input_7forduló_{i}feladat.txt")

    # Initialize silicon slice
    silicon = mark_chips(chips)

    # Find max rectangle
    print(f"{i}. Feladat: {max_rectangle_hist(silicon)}")
    #print(f"{i}. Feladat: {max_free_rectangle(W, H, chips)}")

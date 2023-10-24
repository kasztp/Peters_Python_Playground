from collections import Counter


def load_data(path):
    with open(path) as f:
        num_lines = int(f.readline())
        wafers = [int(line) for line in f.readline().split()]
    return num_lines, wafers


def count_duplicates(wafers):
    """Count the number of duplicates in a list of integers."""
    counts = Counter(wafers)
    duplicates = 0
    for count in counts.values():
        if count > 1:
            duplicates += 1
    return duplicates


if __name__ == '__main__':
    num_lines, wafers = load_data("/Users/kasztp/Documents/GitHub/input_1forduló_4feladat.txt")
    duplicates = count_duplicates(wafers)
    print(duplicates)

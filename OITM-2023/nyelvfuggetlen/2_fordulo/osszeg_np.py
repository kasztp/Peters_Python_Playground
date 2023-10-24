import numpy as np


def read_input(path: str) -> np.ndarray:
    with open(path, 'r') as file:
        line = file.readline()
        numbers = np.array([int(x) for x in line.split()])
        print(f'# numbers: {len(numbers)}')
        return numbers


def find_continous_sums(numbers: np.ndarray) -> dict:
    sums = {}
    cumsum = np.cumsum(numbers)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if j + 1 >= len(numbers):
                break
            if cumsum[j] - (cumsum[i-1] if i > 0 else 0) == numbers[j + 1]:
                sums[(i, j)] = j + 1
    return sums


def find_earliest_continous_sum(sums: dict) -> tuple:
    earliest = None
    for key in sums.keys():
        if earliest is None or key[0] < earliest[0] or (key[0] == earliest[0] and key[1] < earliest[1]):
            earliest = key
    return earliest


if __name__ == "__main__":
    numbers = read_input("OITM-2023/nyelvfuggetlen/osszeg3.in.txt")
    sums = find_continous_sums(numbers)
    earliest = find_earliest_continous_sum(sums)
    if earliest is None:
        print("NINCS")
    else:
        print(f"{earliest[0]} {earliest[1]}")

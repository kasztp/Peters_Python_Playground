import os
from math import factorial


def load_data(file_name: str) -> list[(int, int)]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        k = int(f.readline().strip())
        roads = [road for road in (numbers.strip().split() for numbers in f.readlines())]
        return roads


def calculate_num_combinations(l: list[(int, int)]) -> list[int]:
    results = []
    for line in l:
        n, k = (int(x) for x in line)
        results.append(int(factorial(n) / (factorial(k) * factorial(n - k))))
    return results


def calculate_digit_sum(l: list[int]) -> list[int]:
    results = []
    for number in l:
        results.append(sum(int(digit) for digit in str(number)))
    return results


def do_processing(l: list[(int, int)]) -> int:
    return sum(calculate_digit_sum(calculate_num_combinations(l)))


if __name__ == "__main__":
    for filename in os.listdir(os.path.join(os.getcwd())):
        if filename.endswith(".txt") and filename.startswith("combine"):
            print(f"{filename}: {do_processing(load_data(filename))}")

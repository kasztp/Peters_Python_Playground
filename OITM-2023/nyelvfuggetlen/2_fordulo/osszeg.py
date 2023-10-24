def read_input(path: str) -> list:
    with open(path, 'r') as file:
        line = file.readline()
        numbers = [int(x) for x in line.split()]
        print(f'# numbers: {len(numbers)}')
        return numbers


def find_continous_sums(numbers: list) -> dict:
    """ Find all continous sums in the given list of numbers.
    A continous sum is a sum of two or more consecutive numbers between list indexes i...j (j inclusive),
    where the sum equals the value of the number on the j+1 index.
    
    Returns a dictionary where the keys are a tuple containing the i, j indexes of the continous sum,
    and the values are the indexes of the last number in the continous sum."""
    sums = {}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if j + 1 >= len(numbers):
                break
            if sum(numbers[i:j + 1]) == numbers[j + 1]:
                sums[(i, j)] = j + 1
    return sums


def find_earliest_continous_sum(sums: dict) -> tuple:
    """ Find the earliest continous sum in the given dictionary of continous sums.
    The earliest continous sum is the one with the smallest i index.
    If there are multiple continous sums with the same smallest i index, return the one with the smallest j index.
    """
    earliest = None
    for key, value in sums.items():
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

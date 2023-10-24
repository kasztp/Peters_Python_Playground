import multiprocessing
import os

path = os.getcwd() + "/OTIM-2022/SAP_5/"


def smallest_number_between_two_numbers(a: int, b: int, c: int) -> str:
    """ Return the smallest number between two numbers where the sum of the digits is equal to the third number

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    c : int
        Sum of the digits of the smallest number between a and b

    Returns
    -------
    str
        Smallest number between two numbers or 'NINCS' if there is no such number
    """
    if a > b:
        a, b = b, a
    for x in range(a, b + 1):
        if sum([int(d) for d in str(x)]) == c:
            return str(x)
    return 'NINCS'


def split_range(a: int, b: int, c: int, n: int) -> list:
    """ Split the range of numbers into n ranges

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    n : int
        Number of ranges

    Returns
    -------
    list
        List of ranges
    """
    ranges = []
    step = (b - a) // n
    for i in range(n):
        if i == 0:
            ranges.append((a, a + step, c))
        elif i == n - 1:
            ranges.append((a + i * step + 1, b, c))
        else:
            ranges.append((a + i * step + 1, a + (i + 1) * step, c))
    return ranges


def smallest_number_between_two_numbers_parallel(a: int, b: int, c: int, n: int) -> str:
    """ Return the smallest number between two numbers where the sum of the digits is equal to the third number

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    c : int
        Sum of the digits of the smallest number between a and b
    n : int
        Number of processes

    Returns
    -------
    str
        Smallest number between two numbers or 'NINCS' if there is no such number
    """
    if a > b:
        a, b = b, a
    ranges = split_range(a, b, c, n)

    with multiprocessing.Pool(n) as pool:
        results = pool.starmap(smallest_number_between_two_numbers, ranges)
    return min(results)

if __name__ == '__main__':
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".in.txt"):
            print(filename)
            with open(path + filename, "r", encoding="utf8") as f:
                a, b, c = [int(x) for x in f.readline().strip().split()]
            result = smallest_number_between_two_numbers_parallel(a, b, c, 6)
            print(f"A: {a}, B: {b}, C: {c} --> {result}")

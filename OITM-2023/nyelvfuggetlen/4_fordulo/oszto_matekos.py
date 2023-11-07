import math
import os
from multiprocessing import Pool
import numpy as np


def load_data(file_name: str) -> (int, int):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        a, b = (int(i) for i in f.readline().split())
        return a, b


def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def count_numbers_with_three_divisors(a, b):
    count = 0
    a = a if a % 2 == 1 else a + 1
    b = b if b % 2 == 1 else b - 1

    for i in (range(a, b + 1, 2)):
        root = math.sqrt(i)
        if root.is_integer() and is_prime(root):
            count += 1

    return count


def has_exactly_three_divisors(number: int) -> bool:
    root = math.sqrt(number)
    if root.is_integer() and is_prime(root):
        return True
    return False


def count_numbers_with_three_divisors_parallel(a, b):
    chunksize = (b - a) // os.cpu_count() - 1 if (b - a) // os.cpu_count() > 1 else 1
    a = a if a % 2 == 1 else a + 1
    b = b if b % 2 == 1 else b - 1

    with Pool() as p:
        return sum(p.map(has_exactly_three_divisors, range(a, b + 1, 2), chunksize=chunksize))
    

def count_numbers_with_three_divisors_np(a, b):
    a = a if a % 2 == 1 else a + 1
    b = b if b % 2 == 1 else b - 1

    # If the resulting array would be too big, split into manageable chunks:
    chunk_size = 2**31 // 4 // 8
    if (b - a) // 2 > chunk_size:
        primes = np.array([], dtype=np.uint32)
        for i in range(a, b + 1, chunk_size * 2):
            primes = np.append(primes, count_numbers_with_three_divisors_np(i, i + chunk_size * 2 - 1))
    else:
        numbers = np.arange(a, b + 1, 2)
        roots = np.sqrt(numbers)
        primes = np.array([n for n in roots if n.is_integer() and all(n % i for i in range(2, int(np.sqrt(n)) + 1))]).astype(np.uint32)

    return len(primes)


if __name__ == "__main__":
    filename = f"oszto.pelda1.in.txt"
    print(f'{filename}: {count_numbers_with_three_divisors_np(*load_data(filename))}')
    print(f'{filename}: {count_numbers_with_three_divisors_parallel(*load_data(filename))}')
    print(f'{filename}: {count_numbers_with_three_divisors(*load_data(filename))}')
    
    filename = f"oszto.pelda2.in.txt"
    print(f'{filename}: {count_numbers_with_three_divisors_np(*load_data(filename))}')
    print(f'{filename}: {count_numbers_with_three_divisors_parallel(*load_data(filename))}')
    print(f'{filename}: {count_numbers_with_three_divisors(*load_data(filename))}')

    for i in range(1, 6):
        filename = f"oszto{i}.in.txt"
        print(f'{filename}: {count_numbers_with_three_divisors_np(*load_data(filename))}')
        print(f'{filename}: {count_numbers_with_three_divisors_parallel(*load_data(filename))}')
        print(f'{filename}: {count_numbers_with_three_divisors(*load_data(filename))}')

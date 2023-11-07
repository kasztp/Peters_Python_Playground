import os
from multiprocessing import Pool


def load_data(file_name: str) -> (int, int):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        a, b = (int(i) for i in f.readline().split())
        return a, b


def count_divisors(n: int) -> int:
    divisors = 1
    i = 2
    
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        divisors *= (count + 1)
        i += 1
    
    if n > 1:
        divisors *= 2
    
    return divisors


def has_exactly_three_divisors(number: int) -> bool:
    return count_divisors(number) == 3


def has_specific_number_of_divisors(number: int, num_divisors_acceptable: int = 3) -> bool:
    num_divisors = 2
    for i in range(2, number):
        if number % i == 0:
            num_divisors += 1
        if num_divisors > num_divisors_acceptable:
            return False
    if num_divisors == num_divisors_acceptable:
        return True
    return False


check_divisors = lambda number: has_specific_number_of_divisors(number, 3)


def check_divisors_in_range(a: int, b: int) -> int:
    return sum(check_divisors(i) for i in range(a, b + 1))


def check_divisors_in_range_fast(a: int, b: int) -> int:
    return sum(count_divisors(i) == 3 for i in range(a, b + 1))


def check_divisors_in_range_parallel(a: int, b: int) -> int:
    chunksize = (b - a) // os.cpu_count() - 1 if (b - a) // os.cpu_count() > 1 else 1
    with Pool() as p:
        return sum(p.map(has_specific_number_of_divisors, range(a, b + 1), chunksize=chunksize))


def check_divisors_in_range_fast_parallel(a: int, b: int) -> int:
    chunksize = (b - a) // os.cpu_count() - 1 if (b - a) // os.cpu_count() > 1 else 1
    with Pool() as p:
        return sum(p.map(has_exactly_three_divisors, range(a, b + 1), chunksize=chunksize))


if __name__ == "__main__":
    filename = f"oszto.pelda1.in.txt"
    a, b = load_data(filename)
    print(f"{filename}: {check_divisors_in_range_fast(a, b)}")
    print(f"{filename}: {check_divisors_in_range_fast_parallel(a, b)}")
    print(f"{filename}: {check_divisors_in_range_parallel(a, b)}")
    print(f"{filename}: {sum(has_specific_number_of_divisors(i) for i in range(a, b + 1))}")
    print(f"{filename}: {check_divisors_in_range(a, b)}")

    filename = f"oszto.pelda2.in.txt"
    a, b = load_data(filename)
    print(f"{filename}: {check_divisors_in_range_fast(a, b)}")
    print(f"{filename}: {check_divisors_in_range_fast_parallel(a, b)}")
    print(f"{filename}: {check_divisors_in_range_parallel(a, b)}")
    print(f"{filename}: {sum(has_specific_number_of_divisors(i) for i in range(a, b + 1))}")
    print(f"{filename}: {check_divisors_in_range(a, b)}")

    for i in range(5):
        filename = f"oszto{i + 1}.in.txt"
        a, b = load_data(filename)
        print(f"{filename}: {check_divisors_in_range_fast_parallel(a, b)}")
        #print(f"{filename}: {check_divisors_in_range_fast(a, b)}")
        #print(f"{filename}: {check_divisors_in_range_parallel(a, b)}")
        #print(f"{filename}: {sum(has_specific_number_of_divisors(i) for i in range(a, b + 1))}")
        #print(f"{filename}: {check_divisors_in_range(a, b)}")

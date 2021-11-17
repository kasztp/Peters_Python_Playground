from time import time


def timer(func, parameters):
    # Wrapper for performance measurement
    start = time()
    result = func(parameters)
    end = time()
    print(f'Result: {result}, Time taken: {end - start}')


def fib_recursive(n: int) -> int:
    # Naive recursive version
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_recursive(n-1) + fib_recursive(n-2)
    return result


def fib_memoization(n: int) -> int:
    # Store already calculated values in a cache
    def fibonacci(num: int, cache: dict) -> int:
        if num in cache:
            return cache[num]
        else:
            cache[num] = fibonacci(num-1, cache) + fibonacci(num-2, cache)
            return cache[num]

    calculated = {0: 0, 1: 1}
    return fibonacci(n, calculated)


for i in range(20):
    print(i, fib_recursive(i), fib_memoization(i))


timer(fib_memoization, 30)
timer(fib_recursive, 30)
timer(fib_memoization, 100)




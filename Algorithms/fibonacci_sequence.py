""" Library to compare different methods for calculating the Fibonacci sequence. """
from time import time


def timer(func, parameters):
    """ Wrapper for performance measurement """
    start = time()
    result = func(parameters)
    end = time()
    print(f'Result: {result}, Time taken: {end - start}')


def fib_recursive(number: int) -> int:
    """ Naive recursive version """
    if number == 0:
        result = 0
    elif number == 1:
        result = 1
    else:
        result = fib_recursive(number - 1) + fib_recursive(number - 2)
    return result


def fib_memoization(number: int) -> int:
    """ Store already calculated values in a cache """

    def fibonacci(num: int, cache: dict[int, int]) -> int:
        """ Memoization recursive version """
        if num in cache:
            return cache[num]
        cache[num] = fibonacci(num-1, cache) + fibonacci(num-2, cache)
        return cache[num]

    calculated = {0: 0, 1: 1}
    return fibonacci(number, calculated)


timer(fib_memoization, 35)
timer(fib_recursive, 35)
timer(fib_memoization, 500)

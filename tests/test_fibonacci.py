""" Unit tests for the Fibonacci algorithms. """
from Algorithms.fibonacci_sequence import (
    fib_recursive,
    fib_lru_recursive,
    fib_memoization
)

TEST_NUMBER = 35
EXPECTED_RESULT = 9227465


def test_fib_recursive():
    """ Test fib_recursive() algorithm. """
    assert fib_recursive(TEST_NUMBER) == EXPECTED_RESULT


def test_fib_lru_recursive():
    """ Test fib_lru_recursive() algorithm. """
    assert fib_lru_recursive(TEST_NUMBER) == EXPECTED_RESULT


def test_fib_memoization():
    """ Test fib_memoization() algorithm. """
    assert fib_memoization(TEST_NUMBER) == EXPECTED_RESULT

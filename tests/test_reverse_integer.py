""" Integer reversal algorithms unit tests. """
from Algorithms.reverse_integer import (
    enumerate_reverse,
    dividing_reverse,
    list_comprehension_reverse,
    string_reversed_reverse,
    string_slicing_reverse
)

NUMBER = 123456789
RESULT = 987654321


def test_enumerate_reverse():
    """ Test function for enumerate_reverse() function. """
    assert enumerate_reverse(NUMBER) == RESULT


def test_dividing_reverse():
    """ Test function for dividing_reverse() function. """
    assert dividing_reverse(NUMBER) == RESULT


def test_list_comprehension_reverse():
    """ Test function for list_comprehension_reverse() function. """
    assert list_comprehension_reverse(NUMBER) == RESULT


def test_string_reversed_reverse():
    """ Test function for string_reversed_reverse() function. """
    assert string_reversed_reverse(NUMBER) == RESULT


def test_string_slicing_reverse():
    """ Test function for string_slicing_reverse() function. """
    assert string_slicing_reverse(NUMBER) == RESULT

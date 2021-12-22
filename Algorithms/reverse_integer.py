""" Library to compare different methods for reversing an integer. """
import timeit

NUMBER = 1234567893254875764542998765432012


def for_cycle_reverse(num: int) -> int:
    """ Reverse integer using naive iterative approach. """
    result_list = []
    for digit in list(str(num))[::-1]:
        result_list += digit
    return int(''.join(result_list))


def dividing_reverse(num: int) -> int:
    """ Reverse integer using math. """
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10
    return result


def list_comprehension_reverse(num: int) -> int:
    """ Reverse integer using list comprehension. """
    return int(''.join([n for n in str(num)[::-1]]))


def string_reversed_reverse(num: int) -> int:
    """ Reverse integer using reversed() function. """
    return int(''.join(reversed(str(num))))


def string_slicing_reverse(num: int) -> int:
    """ Reverse integer using list slicing. """
    return int(str(num)[::-1])


if __name__ == '__main__':
    race_result = {
        f'For cycle reverse result:\t{for_cycle_reverse(NUMBER)}\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import for_cycle_reverse',
                stmt=f'for_cycle_reverse({NUMBER})'),
        f'List comprehension result:\t{list_comprehension_reverse(NUMBER)}\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import list_comprehension_reverse',
                stmt=f'list_comprehension_reverse({NUMBER})'),
        f'String reversed() result:\t{string_reversed_reverse(NUMBER)}\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import string_reversed_reverse',
                stmt=f'string_reversed_reverse({NUMBER})'),
        f'String slicing result:\t\t{string_slicing_reverse(NUMBER)}\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import string_slicing_reverse',
                stmt=f'string_slicing_reverse({NUMBER})'),
        f'Dividing reverse result:\t{dividing_reverse(NUMBER)}\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import dividing_reverse',
                stmt=f'dividing_reverse({NUMBER})')
    }

    for timing in sorted(race_result, key=race_result.get, reverse=True):
        print(timing, round(race_result[timing], 4))

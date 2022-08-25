""" A few sorting algorithms implemented in Python """
import timeit
from random import randint


def insertion_sort(lst: list) -> list:
    """ Insertion sort algorithm. """
    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = value
    return lst


def bubble_sort(lst: list) -> list:
    """ Bubble sort algorithm. """
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def selection_sort(lst: list) -> list:
    """ Selection sort original algorithm. """
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def optimized_selection_sort(lst: list) -> list:
    """ Optimized Selection sort algorithm. """
    for i, value in enumerate(lst):
        min_index = i
        if i < len(lst)-1:
            min_index = lst.index(min(lst[i: len(lst)]))
        lst[i], lst[min_index] = lst[min_index], value
    return lst


def merge_sort(lst: list) -> list:
    """ Merge sort algorithm. """
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def quick_sort(lst: list) -> list:
    """ Quick sort algorithm. """
    def partition(lst, start, end):
        pivot = lst[end]
        bottom = start - 1
        for i in range(start, end):
            if lst[i] <= pivot:
                bottom += 1
                lst[bottom], lst[i] = lst[i], lst[bottom]
        lst[bottom + 1], lst[end] = lst[end], lst[bottom + 1]
        return bottom + 1

    def _quick_sort(lst, start, end):
        if start < end:
            pivot = partition(lst, start, end)
            _quick_sort(lst, start, pivot - 1)
            _quick_sort(lst, pivot + 1, end)

    _quick_sort(lst, 0, len(lst) - 1)
    return lst


def built_in_sort(lst: list) -> list:
    """ Function using Python's built-in .sort() """
    lst.sort()
    return lst


def sorted_sort(lst: list) -> list:
    """ Function using Python's built-in sorted() """
    return sorted(lst)


def race_sorts(scale: int, test_data: list) -> None:
    """ Function for performance evaluation of a few sorting algorithms, and print the results. """
    race_result = {
        'Insertion Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import insertion_sort',
                stmt=f'insertion_sort({test_data})',
                number=1),
        'Bubble Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import bubble_sort',
                stmt=f'bubble_sort({test_data})',
                number=3),
        'Selection Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import selection_sort',
                stmt=f'selection_sort({test_data})',
                number=1),
        'Opt. Selection Sort:\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import optimized_selection_sort',
                stmt=f'optimized_selection_sort({test_data})',
                number=1),
        'Merge Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import merge_sort',
                stmt=f'merge_sort({test_data})',
                number=1),
        'Quick Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import quick_sort',
                stmt=f'quick_sort({test_data})',
                number=1),
        'Built-in Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import built_in_sort',
                stmt=f'built_in_sort({test_data})',
                number=1),
        'Sorted Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import sorted_sort',
                stmt=f'sorted_sort({test_data})',
                number=1),
    }
    print(f'\nTest results for {scale} items:')
    for timing in sorted(race_result, key=race_result.get, reverse=True):
        print(timing, round(race_result[timing], 4))


if __name__ == '__main__':
    TEST_DATA = {10**y:[randint(0,x) for x in range(10**y)] for y in range(3,5)}
    for key, data in TEST_DATA.items():
        race_sorts(key, data)

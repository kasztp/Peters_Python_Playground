import timeit
from copy import deepcopy
from random import randint

TEST_DATA = {10**y:[randint(0,x) for x in range(10**y)] for y in range(3,5)}


def insertion_sort(lst):
    """ Insertion sort algorithm. """
    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = value
    return lst


def bubble_sort(lst):
    """ Bubble sort algorithm. """
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def selection_sort(lst):
    """ Selection sort original algorithm. """
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def optimized_selection_sort(lst):
    """ Optimized Selection sort algorithm. """
    for i, value in enumerate(lst):
        min_index = i
        if i < len(lst)-1:
            min_index = lst.index(min(lst[i: len(lst)]))
        lst[i], lst[min_index] = lst[min_index], value
    return lst


def merge_sort(lst):
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


def quick_sort(lst):
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


def built_in_sort(lst):
    lst.sort()
    return lst


def sorted_sort(lst):
    return sorted(lst)


def test_sort(sort_func):
    for data in TEST_DATA.values():
        sort_func(data)
        assert data == sorted(data)


def race_sorts(scale, test_data):
    race_result = {
        f'Insertion Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import insertion_sort',
                stmt=f'insertion_sort({test_data})',
                number=1),
        f'Bubble Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import bubble_sort',
                stmt=f'bubble_sort({test_data})',
                number=3),
        f'Selection Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import selection_sort',
                stmt=f'selection_sort({test_data})',
                number=1),
        f'Opt. Selection Sort:\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import optimized_selection_sort',
                stmt=f'optimized_selection_sort({test_data})',
                number=1),
        f'Merge Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import merge_sort',
                stmt=f'merge_sort({test_data})',
                number=1),
        f'Quick Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import quick_sort',
                stmt=f'quick_sort({test_data})',
                number=1),
        f'Built-in Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import built_in_sort',
                stmt=f'built_in_sort({test_data})',
                number=1),
        f'Sorted Sort:\t\t--\tTime: ':
            timeit.timeit(
                setup='from __main__ import sorted_sort',
                stmt=f'sorted_sort({test_data})',
                number=1),
    }
    print(f'\nTest results for {scale} items:')
    for timing in sorted(race_result, key=race_result.get, reverse=True):
        print(timing, round(race_result[timing], 4))


def test_equality():
    '''Test function to check if all sorting algorithms return the same result.'''
    dummy_data = [2,6,7,1,9,0,3,8,5,4]
    test_result = sorted(dummy_data)
    assert built_in_sort(a:=deepcopy(dummy_data)) == test_result
    assert sorted_sort(b:=deepcopy(dummy_data)) == test_result
    assert insertion_sort(c:=deepcopy(dummy_data)) == test_result
    assert bubble_sort(d:=deepcopy(dummy_data)) == test_result
    assert selection_sort(e:=deepcopy(dummy_data)) == test_result
    assert optimized_selection_sort(f:=deepcopy(dummy_data)) == test_result
    assert merge_sort(g:=deepcopy(dummy_data)) == test_result
    assert quick_sort(h:=deepcopy(dummy_data)) == test_result


if __name__ == '__main__':
    test_equality()
    for key, data in TEST_DATA.items():
        race_sorts(key, data)

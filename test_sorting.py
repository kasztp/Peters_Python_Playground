"""
Sorting algorithm unit tests.
"""
from copy import deepcopy
from Algorithms.sorting import (
    built_in_sort,
    insertion_sort,
    bubble_sort,
    selection_sort,
    optimized_selection_sort,
    merge_sort,
    quick_sort
)

dummy_data = [2,6,7,1,9,0,3,6,8,5,4]
test_result = sorted(dummy_data)


def test_built_in_sort():
    """Test function for built_in_sort() function."""
    assert built_in_sort(a:=deepcopy(dummy_data)) == test_result


def test_insertion_sort():
    """Test function for insertion_sort() function."""
    assert insertion_sort(c:=deepcopy(dummy_data)) == test_result


def test_bubble_sort():
    """Test function for bubble_sort() function."""
    assert bubble_sort(d:=deepcopy(dummy_data)) == test_result


def test_selection_sort():
    """Test function for selection_sort() function."""
    assert selection_sort(e:=deepcopy(dummy_data)) == test_result


def test_optimized_selection_sort():
    """Test function for optimized_selection_sort() function."""
    assert optimized_selection_sort(f:=deepcopy(dummy_data)) == test_result


def test_merge_sort():
    """Test function for merge_sort() function."""
    assert merge_sort(g:=deepcopy(dummy_data)) == test_result


def test_quick_sort():
    """Test function for quick_sort() function."""
    assert quick_sort(h:=deepcopy(dummy_data)) == test_result

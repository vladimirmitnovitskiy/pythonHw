import pytest
import random

from hw5.heapsort import heap_sort

#unit test

def test_sorted_list():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reversed_list():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    assert heap_sort([4, 1, 5, 8, 2, 4, 52]) == [1, 2, 4, 4, 5, 8, 52]

#extreme cases 

def test_empty_list():
    assert heap_sort([]) == []

def test_single_element():
    assert heap_sort([1]) == [1]

def test_equal_elements():
    assert heap_sort([6, 6, 6]) == [6, 6, 6]

def test_large_nums():
    assert heap_sort([9192391239213, 12381232189, 12389219]) == sorted([9192391239213, 12381232189, 12389219])

#propery-based tests

@pytest.mark.parametrize("_", range(20))
def test_heap_sort_random_property(_):
    arr = [random.randint(-1000,1000) for _ in range(random.randint(0,50))]
    assert heap_sort(arr.copy()) == sorted(arr)
"""
Test that the implementations of sort() are correct or incorrect as intended.
"""
import random
from wrong.sort import *


def _get_random_list(length=100, mini=-10, maxi=10):
    l = [0] * length
    for i in range(length):
        l[i] = random.randint(mini, maxi)
    return l

def _is_correct_sort(original_list, sorted_list):
    answer = sorted(original_list)
    return sorted_list == answer

def test_sort_0():
    """
    Tests sort_0, the correct implementation of sort().
    """
    random.seed(42)
    before = _get_random_list()
    after = before.copy()
    sort_0(after)

    assert _is_correct_sort(before, after)

def test_sort_1():
    """
    Tests sort_1, the incorrect implementation of sort() that does not perform
    any operation.
    """
    random.seed(42)
    before = _get_random_list()
    after = before.copy()
    sort_1(after)

    assert not _is_correct_sort(before, after)

def test_sort_2():
    """
    Tests sort_2, the incorrect implementation of sort() that reverses the
    given list.
    """
    random.seed(42)
    before = _get_random_list()
    after = before.copy()
    sort_2(after)

    assert not _is_correct_sort(before, after)

def test_sort_3():
    """
    Tests sort_3, the incorrect implementation of sort() that reverses the
    given list.
    """
    random.seed(42)
    before = _get_random_list()
    after = before.copy()
    sort_3(after)

    assert not _is_correct_sort(before, after)

def test_sort_4():
    """
    Tests sort_3, the incorrect implementation of sort() that reverses the
    given list.
    """
    random.seed(42)
    before = _get_random_list()
    after = before.copy()
    sort_3(after)

    assert not _is_correct_sort(before, after)

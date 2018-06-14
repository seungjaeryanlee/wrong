"""
A collection of implementations of the sort() function.
"""


def sort_0(l):
    """
    A correct implementation of the sort() function.
    """
    l.sort()

def sort_1(l):
    """
    An incorrect implementation of the sort() function. Does not change the
    given list in any way.
    """
    pass

def sort_2(l):
    """
    An incorrect implementation of the sort() function. Reverses the given
    list.
    """
    l.reverse()

def sort_3(l):
    """
    An incorrect implementation of the sort() function. Sorts given list in
    reverse order.
    """
    l.sort(reverse=True)

def sort_4(l):
    """
    An incorrect implementation of the sort() function. Doesn't work if there
    are duplicate elements.
    """
    l = list(set(l))
    l.sort()

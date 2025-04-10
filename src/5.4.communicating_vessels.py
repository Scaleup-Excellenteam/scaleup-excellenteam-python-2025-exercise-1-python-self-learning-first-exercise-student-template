"""
Provides two functions to interleave multiple iterables in a round-robin fashion.

- `interleave`: Returns a list of elements from all iterables interleaved together.
- `generator_interleave`: Yields elements from all iterables interleaved one by one.
"""
from itertools import zip_longest


def interleave(*iterables):
    """
    Returns a list of elements taken in round-robin order from the given iterables.
    Args:
        *iterables: Any number of iterable objects.
    Returns:
        list: A list containing elements interleaved from the input iterables.
    """
    return [item for group in zip_longest(*iterables, fillvalue=None) for item in group if item is not None]


def generator_interleave(*iterables):
    """
    A generator version of `interleave` that yields elements in round-robin order from multiple iterables.
    Args:
        *iterables: Any number of iterable objects.
    Yields:
        Elements from the input iterables interleaved in round-robin order.
    """
    for group in zip_longest(*iterables):
        for item in group:
            if item is not None:
                yield item
                

if __name__ == '__main__':
    lst = list(interleave('ab', [1, 2, 3], ('!', '@')))
    print(lst)

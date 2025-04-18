from itertools import zip_longest
"""
Module: interleave_utils
This module provides functions to interleave elements from multiple iterables.
It includes both a generator version for memory-efficient iteration and a list-based version
that also handles iterables of different lengths.
"""
def generator_interleave(*input_iter):
    """
    A generator function that interleaves multiple iterables and yields their elements one by one.

    The function takes any number of input iterables and yields their elements in an interleaved fashion,
    element by element from each iterable in turn. The process stops when the shortest iterable is exhausted.

    Unlike regular zipping, if an element within the iterables is itself iterable (like a list or tuple),
    its individual elements will be yielded separately using 'yield from'. Non-iterables like integers
    or floats are yielded as-is. Strings, although iterable, are yielded as whole values and not split character by character.

    Args:
        *input_iter: Any number of iterable arguments.

    Yields:
        Elements from the input iterables, interleaved. For nested iterables, yields their elements individually.
        Strings are treated as atomic and yielded whole.

    """
    for items in zip(*input_iter):
        for item in items:
            try:
                if isinstance(item, str):
                    yield item
                else:
                    yield from item
            except TypeError:
                yield item


def interleave(*input_iter):
    """
    Interleaves multiple iterables and returns a list with elements from all,
    including remaining elements from the longest iterable.

    Returns:
        A list of elements interleaved from the input iterables. Any remaining
        elements from the longer iterables are appended at the end in order.
    """
    if not input_iter:
        return []
    placeholder = object()
    zipped = zip_longest(*input_iter, fillvalue=placeholder)
    return [x for group in zipped for x in group if x is not placeholder]


if __name__ == "__main__":
    interleave()
    generator_interleave()

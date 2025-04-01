"""
Module: interleave_utils
This module provides functions to interleave elements from multiple iterables.
It includes both a generator version for memory-efficient iteration and a list-based version
that also handles iterables of different lengths.
"""
def generator_interleave(*input_iter):
    """
    A generator function that interleaves multiple iterables and yields their elements one by one.

    Yields:
        Elements from all input iterables in an interleaved fashion.
        Stops when the shortest iterable is exhausted.
    """
    for items in zip(*input_iter):
        for item in items:
            yield item

def interleave(*input_iter):
    """
        Interleaves multiple iterables and returns a list with elements from all,
        including remaining elements from the longest iterable.

        Returns:
            A list of elements interleaved from the input iterables. Any remaining elements from
            the longer iterables are appended at the end in order.
        """
    if not input_iter:
        return []
    result = []
    for items in zip(*input_iter):
        result.extend(items)
    min_len = min(map(len, input_iter))
    max_len = max(map(len, input_iter))
    for i in range(min_len, max_len):
        for it in input_iter:
            if i < len(it):
                result.append(it[i])
    return result


if __name__ == "__main__":
    interleave()
    generator_interleave()


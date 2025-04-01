def interleave(*iterables):
    """
    Yield elements from multiple iterables in an interleaved (round-robin) fashion.

    The function stops as soon as one of the iterables is exhausted.

    :param iterables: Any number of iterable objects.
    :yield: Elements from the input iterables in round-robin order.
    :rtype: generator
    """
    # Convert each iterable to its iterator form
    iterators = [iter(it) for it in iterables]

    while True:
        try:
            # Yield the next item from each iterator in order
            for it in iterators:
                yield next(it)
        except StopIteration:
            # Stop if any iterator is exhausted
            break

if __name__ == '__main__':
    for item in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(item, end=' ')

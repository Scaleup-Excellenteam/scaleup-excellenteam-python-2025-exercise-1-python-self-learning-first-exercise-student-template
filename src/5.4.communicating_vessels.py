def interleave(*iterables):
    """
    Yield elements from multiple iterables in an interleaved (round-robin) fashion.

    Continues until all iterables are exhausted.
    """
    # Convert each iterable to an iterator
    iterators = [iter(it) for it in iterables]

    while iterators:
        next_iterators = []
        for it in iterators:
            try:
                yield next(it)
                next_iterators.append(it)
            except StopIteration:
                continue
        iterators = next_iterators

# Match the expected name
generator_interleave = interleave

if __name__ == '__main__':
    for item in generator_interleave('abc', [1, 2], ('!',)):
        print(item, end=' ')

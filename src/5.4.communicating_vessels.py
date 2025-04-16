def interleave(*iterables):
    """
    Yield elements from multiple iterables in an interleaved (round-robin) fashion.

    Continues until all iterables are exhausted.
    For example:
    interleave('abc', [1, 2], ('!',)) → a, 1, !, b, 2, c
    """
    # Convert each input iterable into an iterator so we can manually fetch items
    iterators = [iter(it) for it in iterables]

    # Continue as long as there are iterators with remaining items
    while iterators:
        next_iterators = []  # List of iterators that still have items

        for it in iterators:
            try:
                # Yield the next item from the iterator
                yield next(it)
                # If successful, keep this iterator for the next round
                next_iterators.append(it)
            except StopIteration:
                # If this iterator is exhausted, skip it
                continue

        # Update the list of iterators for the next round
        iterators = next_iterators

# Alias to match the name expected in tests
generator_interleave = interleave

if __name__ == '__main__':
    # Test example: should print a1!b2c
    for item in generator_interleave('abc', [1, 2], ('!',)):
        print(item, end=' ')

def interleave(*iterables):
    """Regular function that returns a list."""
    iterators = [iter(it) for it in iterables]
    result = []
    while iterators:
        for it in list(iterators):
            try:
                result.append(next(it))
            except StopIteration:
                iterators.remove(it)
    return result


def generator_interleave(*iterables):
    """Generator version that yields items one by one."""
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in list(iterators):
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)


if __name__ == '__main__':
    # Test the functions
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))  # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))))  # Same output
"""Interleaves elements from multiple iterables and returns them as a list."""

def interleave(*iterables):
    """
    Interleaves elements from multiple iterables and returns them as a list.

    :param iterables: One or more iterables to interleave
    :return: List of interleaved elements from all iterables
    """
    iterators = [iter(it) for it in iterables]
    result = []
    while iterators:
        for iterator in iterators:
            try:
                result.append(next(iterator))
            except StopIteration:
                iterators.remove(iterator)
    return result

def generator_interleave(*iterables):
    """
    Interleaves elements from multiple iterables and yields them one by one.

    :param iterables: One or more iterables to interleave
    :yield: Elements interleaved from all iterables
    """
    iterators = [iter(it) for it in iterables]
    while iterators:
        for iterator in iterators:
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)


if __name__ == '__main__':
    result = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    print(list(result))

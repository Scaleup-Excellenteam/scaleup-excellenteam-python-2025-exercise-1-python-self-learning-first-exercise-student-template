def communicating_vessels(*iterables):
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
    result = communicating_vessels('abc', [1, 2, 3], ('!', '@', '#'))
    print(list(result))

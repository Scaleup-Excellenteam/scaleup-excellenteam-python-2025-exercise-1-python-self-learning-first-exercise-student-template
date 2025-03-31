
def interleave(*iterables):
    """
    Takes one or more iterables and returns a list of interleaved elements.
    Elements are taken from each iterable in round-robin fashion.
    """
    if not iterables:
        return []

    arr = []
    iterators = [iter(it) for it in iterables]
    active = len(iterators)

    while active > 0:
        active = 0
        for iterator in iterators:
            try:
                arr.append(next(iterator))
                active += 1
            except StopIteration:
                pass

    return arr


def generator_interleave(*iterables):
    """
    Generator version of interleave that yields interleaved elements.
    """
    if not iterables:
        return

    iterators = [iter(it) for it in iterables]
    active = len(iterators)

    while active > 0:
        active = 0
        for iterator in iterators:
            try:
                yield next(iterator)
                active += 1
            except StopIteration:
                pass


if __name__ == "__main__":
    print("test1:")
    result = list(interleave('ab', [1, 2, 3], ('@', '%')))
    print(result)

    print("\ntest2:")
    result = list(interleave([10, 20, 30]))
    print(result)

    print("\ntest3:")
    result = list(interleave())
    print(result)

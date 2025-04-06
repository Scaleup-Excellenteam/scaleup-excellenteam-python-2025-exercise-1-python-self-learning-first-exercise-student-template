from itertools import zip_longest


def interleave(*iterables):
    """
    Interleave all items from input iterables. Pads shorter ones with None.
    """
    result = []
    for values in zip_longest(*iterables, fillvalue=None):
        for value in values:
            if value is not None:
                result.append(value)
    return result


def generator_interleave(*iterables):
    """
    Generator version of interleave that yields items one by one.
    """
    for values in zip(*iterables):
        for value in values:
            yield value


if __name__ == '__main__':
    print(list(interleave('ab', [1, 2, 3], ('@', '%'))))
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))))

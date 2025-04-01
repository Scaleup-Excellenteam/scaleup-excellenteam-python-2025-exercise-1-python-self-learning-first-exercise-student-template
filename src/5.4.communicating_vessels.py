from itertools import zip_longest

_FILL = object()  # single shared filler

def interleave(*iterables):
    """
    Interleaves multiple iterables, continuing until the longest one is exhausted.
    """
    result = []
    for group in zip_longest(*iterables, fillvalue=_FILL):
        for item in group:
            if item is not _FILL:  # correctly skip filler
                result.append(item)
    return result


def generator_interleave(*iterables):
    """
    Generator that yields items interleaved from the given iterables.
    """
    for group in zip_longest(*iterables, fillvalue=_FILL):
        for item in group:
            if item is not _FILL:
                yield item


if __name__ == '__main__':
    result = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    result_gen = list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#')))

    print(f'Result: {result}')  # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    print(f'Generator Result: {result_gen}')  # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
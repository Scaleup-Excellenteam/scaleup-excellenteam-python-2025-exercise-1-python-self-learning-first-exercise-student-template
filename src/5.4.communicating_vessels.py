def generator_interleave(*input):
    """
    A generator function that interleaves multiple iterables and yields their elements one by one.

    Parameters:
    *input (iterables): Multiple iterables to interleave.

    Yields:
    element: Each element from the iterables, interleaved one by one.
    """
    for item in zip(*input):
        for index in item:
            yield index  # Yield each element one by one

def interleave(*input):
    """
    Interleaves multiple iterables and yields their elements one by one.
    Ensures that elements from the longest iterable are also included.

    Parameters:
    *input (iterables): Multiple iterables to interleave.

    Yields:
    element: Each element from the iterables, interleaved one by one.
        """
    if not input:
        return
    for item in zip(*input):
        yield from item

    longest = max(input, key=len, default=[])
    if input:
        yield from longest[min(map(len, input)):]

def main():
    lst = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(lst)

if __name__ == "__main__":
    main()

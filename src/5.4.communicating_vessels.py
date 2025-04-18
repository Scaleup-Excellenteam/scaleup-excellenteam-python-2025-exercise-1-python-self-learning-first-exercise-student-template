from itertools import zip_longest

def interleave(*iterables):
    """
    Interleaves multiple iterables using zip_longest and flattens the result.
    Returns a list, skipping None values.
    """
    return [item for group in zip_longest(*iterables) for item in group if item is not None]

def generator_interleave(*iterables):
    """
    Generator version using zip_longest.
    Yields items one by one, skipping None values.
    """
    for group in zip_longest(*iterables):
        for item in group:
            if item is not None:
                yield item


if __name__ == "__main__":
    numbers = [10, 20]
    letters = ['x', 'y', 'z']
    symbols = ['#', '*', '&', '@']

    print("Interleaved List:", interleave(numbers, letters, symbols))
    print("Interleaved Generator:", list(generator_interleave(numbers, letters, symbols)))

def interleave(*iterables):
    """
    Function to interleave multiple iterables into a single list.
    This version returns the result as a list.
    """
    combined = []
    if len(iterables) == 0:
        return combined

    longest = max(len(seq) for seq in iterables)

    for idx in range(longest):
        for seq in iterables:
            if idx < len(seq):
                combined.append(seq[idx])

    return combined


def generator_interleave(*iterables):
    """
    Generator version of the interleave function.
    Yields elements from the iterables one by one.
    """
    if len(iterables) == 0:
        return

    limit = max(len(item) for item in iterables)

    for pos in range(limit):
        for item in iterables:
            if pos < len(item):
                yield item[pos]


if __name__ == "__main__":
    numbers = [10, 20]
    letters = ['x', 'y', 'z']
    symbols = ['#', '*', '&', '@']

    print("Interleaved List:", interleave(numbers, letters, symbols))
    print("Interleaved Generator:", list(generator_interleave(numbers, letters, symbols)))
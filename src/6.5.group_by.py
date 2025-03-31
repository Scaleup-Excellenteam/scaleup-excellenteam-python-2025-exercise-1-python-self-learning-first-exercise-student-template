def group_by(func, iterable):
    """
    Groups elements of an iterable by the result of a function.

    Returns dict a dictionary where keys are function results and values are lists of elements
    """
    result = {}

    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)

    return result


if __name__ == "__main__":
    strings = ["hi", "bye", "yo", "try"]
    grouped_by_length = group_by(len, strings)
    print("Grouped by length:", grouped_by_length)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def yuval(n):
        return n % 3


    grouped_by_remainder = group_by(yuval, numbers)
    print("Grouped by remainder when divided by 3:", grouped_by_remainder)



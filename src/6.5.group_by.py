"""Groups elements of an iterable based on the result of applying func to each element."""

from collections import defaultdict

def group_by(func, iterable) -> dict:
    """
    Groups elements of an iterable based on the result of applying func to each element.

    :param func: A function that takes an element and returns a value.
    :param iterable: An iterable whose elements will be grouped.
    :return: A dictionary where keys are results of func and values are lists of corresponding elements.
    """
    grouped_dict = defaultdict(list)
    for item in iterable:
        grouped_dict[func(item)].append(item)
    return dict(grouped_dict)

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))

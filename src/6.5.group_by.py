"""
Groups elements of an iterable based on the result of a given function.
Each element is passed through the function, and grouped by its return value.
Example:
    group_by(len, ["hi", "bye", "yo", "try"])
    => {2: ['hi', 'yo'], 3: ['bye', 'try']}
"""


def group_by(func, iterable):
    """
    Groups items in an iterable by the result of applying a function to each item.
    Args:
        func (callable): Function used to classify items.
        iterable (iterable): A collection of items to group.
    Returns:
        dict: A dictionary with keys from `func(item)` and values as lists of matching items.
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))

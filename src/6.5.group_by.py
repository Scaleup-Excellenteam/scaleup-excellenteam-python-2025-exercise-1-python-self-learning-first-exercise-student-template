"""
Module that defines a function for grouping items by a given key function.
"""

def group_by(func, iterable):
    """
    Group elements of an iterable based on the result of applying a function to each element.

    :param func: A function that takes one argument and returns a key for grouping.
    :param iterable: An iterable of elements to group.
    :return: A dictionary where keys are the results of func(item), and values are lists of items with that key.
    :rtype: dict
    """
    result = {}

    # Iterate over each item in the iterable
    for item in iterable:
        # Apply the function to get the grouping key
        key = func(item)

        # Initialize the group if the key is new
        if key not in result:
            result[key] = []

        # Append the item to the appropriate group
        result[key].append(item)

    return result

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))

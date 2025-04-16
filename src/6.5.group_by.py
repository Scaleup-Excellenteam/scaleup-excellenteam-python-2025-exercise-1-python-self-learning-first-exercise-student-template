
"""
This module defines the `group_by` function, which categorizes elements of an iterable
based on the output of a given function.

The function returns a dictionary where each key is a function output, and the corresponding
value is a list of elements that produced that output.
"""

def group_by(function, iterable):
    """
    Groups elements of the iterable based on the key returned by the function.
    Args:
        function (callable): A function applied to each element to determine the grouping key.
        iterable (iterable): A collection of elements to be grouped.
    Returns:
        dict: A dictionary where keys are function outputs and values are lists of elements
        that produced the same output.
    """
    result = {}
    for item in iterable:
        key = function(item)
        if key not in result:
            result[key] = []
        result[key].append(item)

    return result


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))

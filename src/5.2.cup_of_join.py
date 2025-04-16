"""
This module provides a function to join multiple lists with optional separators.
"""

_sentinel = object()  # Unique marker to detect if 'sep' was explicitly provided

def cup_of_join(*lists, sep=_sentinel):
    """
    Join multiple lists into a single list.
    If a separator is explicitly provided, insert it after each list (even after the last one).
    If not, simply concatenate all the elements from all lists.

    :param lists: Any number of lists to join together.
    :param sep: The separator to insert after each list (if given).
    :return: A single list containing all elements with optional separators.
    """
    # Return an empty list if no input lists were provided
    if not lists:
        return []

    result = []  # This will store the final combined list

    # Iterate over each list provided
    for i, lst in enumerate(lists):
        result.extend(lst)  # Add all elements of the current list to result
        if sep is not _sentinel:
            result.append(sep)  # Add the separator if it was explicitly provided

    return result  # Return the final joined list


# Example usage when running this file directly
if __name__ == '__main__':
    # Example with custom separator '#'
    print(cup_of_join([1, 2, 30], [7, 8], [1], sep='#'))

    # Example without specifying a separator — just concatenate lists
    print(cup_of_join([1, 2], [8], [9, 5, 6]))

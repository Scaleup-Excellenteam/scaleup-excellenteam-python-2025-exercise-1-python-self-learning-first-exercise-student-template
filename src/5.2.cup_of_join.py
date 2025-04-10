"""
This module contains a function that flattens multiple lists into a single list.
Optionally, a separator can be added between each inner list.
"""


def cup_of_join(*matrix, sep=None):
    """
    Flattens one or more lists into a single list.
    Optionally inserts a separator between the inner lists.
    Args:
        *matrix: One or more lists to flatten.
        sep (optional): An item to insert between each list.
    Returns:
        list or None: The flattened list with optional separators, or None if no lists are provided.

    """
    if not matrix:
        return None
    cup = []
    for num_list in matrix:
        for num in num_list:
            cup.append(num)
        if sep:
            cup.append(sep)

    return cup


if __name__ == '__main__':
    print(cup_of_join([9, 5, 6], sep='@'))

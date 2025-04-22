"""
Module for joining elements from multiple iterables with a separator.
This script defines a function that takes multiple iterables and joins their elements
into a single list. A specified separator is inserted between elements from different iterables.
The separator can be customized, and the default is a hyphen '-'.
"""
def cup_of_join(*iterables: list, sep: str = '-') -> list:
    """
    Joins elements from multiple iterables into a single list with a separator.
    
    Parameters:
        *iterables (list): Multiple lists to join.
        sep (str): The separator to insert between elements of different lists (default is '-').
    
    Returns:
        list: A list containing all elements from the iterables, separated by `sep`.
              If no iterables are provided, returns None.
    
    Example:
        cup_of_join([1, 2], [8], [9, 5, 6], sep='@') -> [1, 2, '@', 8, '@', 9, 5, 6]
    """
    if len(iterables) == 0:
        return None
    joined_result = []
    for index, current_iterable in enumerate(iterables):
        if index != 0 and sep != '':
            joined_result.append(sep)
        joined_result.extend(current_iterable)
    return joined_result


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))  

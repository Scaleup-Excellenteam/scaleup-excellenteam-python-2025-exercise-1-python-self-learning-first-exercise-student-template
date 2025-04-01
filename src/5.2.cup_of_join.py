"""
Module for joining elements from multiple iterables with a separator.

This script defines a function that takes multiple iterables and joins their elements
into a single list. A specified separator is inserted between elements from different iterables.
The separator can be customized, and the default is an empty string.
"""
def cup_of_join(*lst, sep=''):
    """
        Joins elements from multiple iterables into a single list with a separator.

        Parameters:
            *lst (iterables): Multiple iterables (lists, tuples, etc.) to join.
            sep (str): The separator to insert between elements of different iterables (default is an empty string).

        Returns:
            list: A list containing all elements from the iterables, separated by `sep`.
                  If no iterables are provided, returns None.

        Example:
            cup_of_join([1, 2], [8], [9, 5, 6], sep='@') -> [1, 2, '@', 8, '@', 9, 5, 6]
        """
    if len(lst)==0:
        return None
    new_lst=[]
    for item in lst:
        for num in item:
            new_lst.append(num)
        if not sep =='':
            new_lst.append(sep)
    return new_lst


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))

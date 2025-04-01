"""
This module defines a function `cup_of_join` that flattens multiple lists into a single list,
separating the elements of each list with a specified separator.

Function:
    cup_of_join(*args, sep=""):
        - Takes any number of lists as arguments and an optional separator string.
        - Flattens all the lists and inserts the separator between each list.
        - Returns a new list with the combined elements and separators.

Example:
    cup_of_join([1, 2], [3, 4], sep=",") -> [1, 2, ',', 3, 4]
"""
from typing import List

def cup_of_join(*args, sep:str = "")->List:
    """
    :param args: unlimited number of lists
    :param sep: seperator to add between lists
    :return: flatten list of lists with sep between each list
    """
    if not args:
        return None

    result = []

    for i,lst in enumerate(args):
        result.extend(lst)
        if i <= len(args)-1 and sep != "":
            result.append(sep)

    return result


if __name__ == '__main__':
    print(cup_of_join([1]))

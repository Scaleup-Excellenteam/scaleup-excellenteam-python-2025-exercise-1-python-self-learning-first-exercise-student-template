"""
Module: group_by_utility
This module provides a function to group elements from an iterable based on
the result of applying a given function to each element.
"""
def group_by(func, iter1):
    """
    Groups elements in an iterable based on the result of applying a function to each element.

    Parameters:
        func (function): A function that will be applied to each element in the iterable.
        iter1 (iterable): The iterable containing the elements to group.

    Returns:
        dict: A dictionary where keys are the results of applying `func` to elements,
              and values are lists of elements that have the same result.

    Raises:
        ValueError: If applying `func` to an element raises an exception.
    """
    new_dic = {}
    for item in iter1:
        try:
            key = func(item)
            new_dic.setdefault(key, []).append(item)
        except Exception as e:
            raise ValueError(f"Error applying function to item '{item}': {e}") from e
    return new_dic



if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))

def join(*lists, sep='-'):
    """
    Join multiple lists into a single list, inserting a separator between each original list.

    :param lists: Any number of lists to be joined.
    :param str sep: The separator to insert between lists (default is '-').
    :return: A new list containing all elements of the input lists with separators in between.
             Returns None if no lists are provided.
    :rtype: list or None
    """
    # If no lists were provided, return None
    if len(lists) == 0:
        return None

    # If only one list is provided, return it as-is
    if len(lists) == 1:
        return lists[0]

    new_lst = []
    # Loop through each list and append its contents to the new list
    for i, lst in enumerate(lists):
        new_lst.extend(lst)
        # Add the separator between lists, but not after the last one
        if i != len(lists) - 1:
            new_lst.append(sep)

    return new_lst

if __name__ == '__main__':
    print(join([1, 2, 30], [7, 8], [1], sep='#'))
    print(join([1, 2], [8], [9, 5, 6]))
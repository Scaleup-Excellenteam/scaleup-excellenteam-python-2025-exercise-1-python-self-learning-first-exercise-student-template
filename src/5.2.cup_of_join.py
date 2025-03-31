def cup_of_join(*lists, sep=None):
    """
    Joins all lists into one, separated by the separator.
    :param lists: Any number of lists
    :param sep: Separator to insert between lists (default is None = no separator)
    :return: A single merged list with separators between
    """

    if not lists:
        return None

    result = []

    for i, lst in enumerate(lists):
        # Add separator between lists
        if i != 0 and sep is not None:
            result.append(sep)

        result.extend(lst)

    # Add trailing separator if sep is given
    if sep is not None:
        result.append(sep)

    return result

if __name__ == '__main__':
    # Example test cases
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))  # [1, 2, '@', 8, '@', 9, 5, 6]
    print(cup_of_join([1, 2], [8], [9, 5, 6]))  # [1, 2, '-', 8, '-', 9, 5, 6]
    print(cup_of_join([1]))  # [1]
    print(cup_of_join())  # None

from typing import Union, Any


def join(*lists: list[Any], sep: str = "-") -> Union[None, list[Any]]:
    """
    Takes any number of lists and returns a list of joined lists.
    :param lists: lists of any type
    :param sep: the seperator between the lists
    :return: the combined list or None if there are no lists
    """
    if len(lists) == 0:
        return None

    res = []

    # Adds the flattened list to res then the sep
    for lst in lists:
        res.extend(lst)
        res.append(sep)

    # Deletes the last sep
    return res[:-1]


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())

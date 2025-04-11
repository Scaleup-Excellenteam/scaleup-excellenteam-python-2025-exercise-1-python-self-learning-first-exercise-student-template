"""Exercise solution 5.2"""


def cup_of_join(*lists, sep="-"):
    """
    Joins multiple lists into a single list with a separator between each list.
    Also adds a separator at the end if needed.
    """
    if len(lists) == 1:
        result = list(lists[0])
        result.append(sep)
        return result

    result = []

    for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)
        result.extend(lst)

    # מוסיף מפריד בסוף
    result.append(sep)

    return result


if __name__ == "__main__":

    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([], [1], [], sep='x'))
    print(cup_of_join())

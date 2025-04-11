"""Exercise solution 5.2"""


def cup_of_join(*lists, sep="-"):
    """
    Joins multiple lists into a single list with a separator between each list.
    Also adds a separator at the end of the result.
    """
    result = []

    for i, lst in enumerate(lists):
        result.extend(lst)

        if i < len(lists) - 1:
            result.append(sep)

    if lists:
        result.append(sep)

    return result


if __name__ == "__main__":
    """main function"""

    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([], [1], [], sep='x'))
    print(cup_of_join())

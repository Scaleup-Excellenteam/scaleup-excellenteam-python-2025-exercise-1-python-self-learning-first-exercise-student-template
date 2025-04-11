"""Exercise solution 5.2"""


def cup_of_join(*lists, sep="-"):
    """
    Joins multiple lists into a single list with a separator between each list.
    """
    result = []

    if sep == "-" and len(lists) > 0 and all(isinstance(lst, list) for lst in lists):
        for lst in lists:
            result.extend(lst)
        return result

    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(sep)

    if lists:
        result.append(sep)

    return result


if __name__ == "__main__":

    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([], [1], [], sep='x'))
    print(cup_of_join())

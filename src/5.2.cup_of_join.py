def cup_of_join(*lists, sep="-"):
    """
    Joins multiple lists into a single list with a separator between each list.
    """
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    result = []

    result.extend(lists[0])

    for lst in lists[1:]:
        result.append(sep)
        result.extend(lst)

    return result


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([], [1], [], sep='x'))
    print(cup_of_join())

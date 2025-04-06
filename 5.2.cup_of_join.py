def cup_of_join(*arrays, sep=None):
    """
    Joins multiple lists with an optional separator.
    If sep is None, lists are simply concatenated.
    If sep is given, it is added between lists and also after the last list.
    """
    if not arrays:
        return None

    result = []

    if sep is None:
        for array in arrays:
            result.extend(array)
        return result

    for i, array in enumerate(arrays):
        result.extend(array)
        # always add sep after each list (including the last one)
        result.append(sep)

    return result


if __name__ == '__main__':
   print(cup_of_join([1, 2], ['a', 'b'], [True]))
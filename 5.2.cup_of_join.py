def cup_of_join(*lists, sep='-'):
    if not lists:
        return None
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i != len(lists) - 1:
            result.append(sep)
    return result


if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())

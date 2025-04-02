def join(*arrays, sep='-'):
    if not arrays:
        return None

    result = []
    for i, array in enumerate(arrays):
        result.extend(array)
        if i != len(arrays) - 1:
            result.append(sep)

    return result


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))  # [1, 2, '@', 8, '@', 9, 5, 6]
    print(join([1, 2], [8], [9, 5, 6]))           # [1, 2, '-', 8, '-', 9, 5, 6]
    print(join([1]))                              # [1]
    print(join())                                 # None

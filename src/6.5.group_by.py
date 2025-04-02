def group_by(func, iterable):
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

if __name__ == '__main__':
    group_by(len, ["hi", "bye", "yo", "try"])
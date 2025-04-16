def group_by(items, key_function):
    grouped = {}
    for item in items:
        key = key_function(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped


if __name__ == '__main__':
    print(group_by(["cat", "car", "dog", "door"], lambda word: word[0]))
    print(group_by([1, 2, 3, 4, 5], lambda x: 'even' if x % 2 == 0 else 'odd'))

def group_by(func, iterable):
    grouped_dict = {}
    for element in iterable:
        group_key = func(element)
        if group_key in grouped_dict:
            grouped_dict[group_key].append(element)
        else:
            grouped_dict[group_key] = [element]
    return grouped_dict


if __name__ == "__main__":
    # Example: Group numbers by even or odd
    numbers = [1, 2, 3, 4, 5, 6, 7]
    grouped = group_by(lambda x: 'even' if x % 2 == 0 else 'odd', numbers)

    print("Grouped by even/odd:", grouped)

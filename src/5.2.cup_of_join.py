def cup_of_join(*lists, sep=None):
    """
    Combines multiple lists into one.
    If 'sep' is given, adds it after each list (even if empty), including after the last.
    If no lists are given, returns None.
    """
    if len(lists) == 0:
        return None

    merged = []

    for group in lists:
        merged.extend(group)
        if sep is not None:
            merged.append(sep)

    return merged


if __name__ == "__main__":
    nums = [10, 20]
    chars = ['x', 'y']
    signs = ['!', '?']

    print(cup_of_join(nums, chars, signs))
    print(cup_of_join(nums, [], signs, sep='|'))
    print(cup_of_join())

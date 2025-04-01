def group_by(func, iterable):
    """
    Groups elements from the iterable based on the result of applying the given function.

    :param func: A function that takes an item and returns a value to group by.
    :param iterable: An iterable of items to be grouped.
    :return: A dictionary where each key is the result of func(item),
             and the corresponding value is a list of items that produced that key.
    """
    result = {}  # Dictionary to hold the grouped results
    for item in iterable:
        key = func(item)  # Apply the function to get the grouping key
        if key not in result:
            result[key] = []  # Create a new list for this key if it doesn't exist
        result[key].append(item)  # Add the current item to the corresponding list
    return result

if __name__ == '__main__':
    # Example usage
    print(group_by(len, ["hi", "bye", "yo", "try"]))
    # Output: {2: ['hi', 'yo'], 3: ['bye', 'try']}

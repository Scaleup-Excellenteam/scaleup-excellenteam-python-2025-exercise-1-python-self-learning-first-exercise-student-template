

def group_by(function, iterable):
    """
       Groups elements of the iterable based on the key returned by the function.
       Returns a dictionary where keys are function outputs and values are lists of corresponding elements.
       Ensures each key maps to a list of items that produce the same function output.
       """
    result = {}
    for item in iterable:
        key = function(item)
        if key not in result:
            result[key] = []
        result[key].append(item)

    return result


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
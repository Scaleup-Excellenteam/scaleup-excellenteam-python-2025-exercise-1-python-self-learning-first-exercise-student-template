def group_by(function, iterable_val):
    """
    This Function Will Get An Function and Iterable, And Return Dictionry Of Run The Function On The Iterable.
    """
    result_dict = {}

    for value in iterable_val:

        # Apply The Function For Each One Of The Iterable.
        dict_key = function(value)

        # Check If Already The Dictionary Exists The Key, Otherwise Add It With Empty List.
        if dict_key not in result_dict:
            result_dict[dict_key] = []

        result_dict[dict_key].append(value)

    return result_dict


def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))
    print(group_by(lambda x: x % 5, [10, 1, 15, 34, 17, 2, 11, 5, 7, 50, 12, 55]))


if __name__ == "__main__":
    main()

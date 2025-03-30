def cup_of_join(*args, sep='-') -> list:
    """
    Combine lists to one list and separate them with the char sep

    :param args: tuple of lists
    :param sep: char
    :return: one list from all the lists
    """
    try:
        if not args:
            raise ValueError("No list provided.")

        result = []
        for lst in args:
            if not isinstance(lst, list):
                raise TypeError(f"Expected a list, got {type(lst).__name__}.")

            if result:
                result.append(sep)
            result.extend(lst)

        return result

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

if __name__ == '__main__':
    lst = cup_of_join([1, 2], [8], [9, 5, 6], sep='@')
    print(lst)
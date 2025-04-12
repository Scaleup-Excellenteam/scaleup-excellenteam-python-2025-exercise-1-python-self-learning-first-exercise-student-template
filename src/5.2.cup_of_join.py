def cup_of_join(*lists, sep=None):
    """
    Receive An Unlimited Number Of Lists On Which We Will Perform A Union, And Between Each Two Lists We Will Insert The Value Seq.
    """
    if not lists:
        return []

    joined_list = []

    # If Ehe User Don't Give A Separtor.
    if sep is None:
        # Union All The Lists To One List.
        for list in lists:
            joined_list += list

    else:
        # Union All The Lists To One List If We Have A Separtor.
        for list in lists:
            # Add The List And The Separator.
            joined_list += list
            joined_list.append(sep)

    if (len(joined_list) == 0):
        return None
    return joined_list


def main():
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())


if __name__ == '__main__':
    main()

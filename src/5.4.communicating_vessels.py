from itertools import zip_longest


def interleave(*iterables_val):
    """
    This Function Accepts An Unlimited Number Of Iterables And Returns A List
    Of Their Elements Interleaved One After Another.
    """

    # Create A New List That Will Contain All The Lists Values.
    ziped_list = zip_longest(*iterables_val, fillvalue=None)
    interleaved_list = []

    # Get The Values For Each Tuble In The Zipeed List.
    for tuple_val in ziped_list:
        for value in tuple_val:
            if value != None:
                interleaved_list.append(value)

    return interleaved_list


def generator_interleave(*iterables_val):
    """
    Create To Call The 'interleave' Function.
    """
    return interleave(*iterables_val)


def main():
    print(generator_interleave('abc', [1, 2, 3], ('!', '@', '#')))


if __name__ == '__main__':
    main()

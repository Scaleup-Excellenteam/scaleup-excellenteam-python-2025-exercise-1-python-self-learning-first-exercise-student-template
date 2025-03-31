def cup_of_join(*lst, sep=''):
    """
        Joins elements from multiple iterables into a single list,
        inserting a separator between elements from different iterables.

        Parameters:
        *lst (iterables): Multiple iterables to join.
        sep (str): The separator to insert between elements of different iterables (default is '-').

        Returns:
        list: A list containing all elements from the iterables, separated by `sep`.
        """

    if len(lst)==0:
        return None
    new_lst=[]
    for item in lst:
        for num in item:
            new_lst.append(num)
        if not sep =='':
            new_lst.append(sep)
    return new_lst


def main():
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    result = cup_of_join([], [1], [], sep='x')
    print(result, ['x', 1, 'x', 'x'])


if __name__ == "__main__":
    main()
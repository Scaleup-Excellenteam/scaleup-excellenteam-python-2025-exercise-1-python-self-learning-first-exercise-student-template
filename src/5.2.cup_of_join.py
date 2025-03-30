def cup_of_join(*args, **kwargs):
    if args is None:
        return None

    # if 'sep' not in kwargs:
    #    kwargs['sep'] = '-'

    my_list = []
    for arg in args:
        for i in arg:
            my_list.append(i)

        if 'sep' in kwargs:
            my_list.append(kwargs['sep'])

    # my_list.pop(-1)
    return my_list


print(cup_of_join([1, 2], [1], sep='%'))

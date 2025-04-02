def communicating_vessels(*iterables):
    """
    This function takes a iterable (one or more) and returns a list of all the iterables weave each other
    :param *iterables : iterable (one or more)
    :return: list of all iterables weave each other
    """
    # return_list =[]
    for values in zip(*iterables):
        for value in values:
            # return_list.append(value)
            yield value
    # return return_list // adding this cuz in the mission its said to return the list like this : [a ,1 ,! ,b , 2, @ , c , 3, #]
if __name__ == '__main__':
    # print(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    generator_iterator = communicating_vessels('abc', [1, 2, 3], ('!', '@', '#'))
    for item in generator_iterator:
        print(item , end =' ')

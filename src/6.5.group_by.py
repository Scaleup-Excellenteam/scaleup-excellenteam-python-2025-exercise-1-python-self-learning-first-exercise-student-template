def group_by(function , iterable):
    """
    Function takes a function and an iterable and returns a dictionary with the keys of function getting the values of iterable and the values is the values of iterable that match with the keys
    :param function: function that takes a single argument from iterable and returns a dictionary with the keys of function
    :param iterable: iterable represent by user
    :return: dictionary with the keys of function getting values of iterable after applying function and values of iterable after applying function
    """
    dictionary = {function(key) : [item for item in iterable if function(key)==function(item)] for key in iterable}
    return dictionary
if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
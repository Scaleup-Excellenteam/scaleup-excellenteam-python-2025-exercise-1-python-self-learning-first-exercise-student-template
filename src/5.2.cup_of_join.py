

from typing import List

def cup_of_join(*args, sep:str = "-")->List:
    """
    :param args: unlimited number of lists
    :param sep: seperator to add between lists
    :return: flatten list of lists with sep between each list
    """
    if not args:
        return None

    result = []

    for i,lst in enumerate(args):
        result.extend(lst)
        if i < len(args)-1:
            result.append(sep)

    return result


if __name__ == '__main__':
    print(cup_of_join([1]))

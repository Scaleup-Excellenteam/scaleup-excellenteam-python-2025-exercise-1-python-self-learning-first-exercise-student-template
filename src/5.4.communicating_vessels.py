from itertools import chain
from typing import Iterable, List, Generator


def communicating_vessels(*args:Iterable)->List:
    """
     Interleaves multiple iterables and returns a flattened list.
    :param args: Iterables to merge
    :return: Flattened list
    """
    return list(chain.from_iterable(zip(*args)))

def communicating_vessels_generator(*args:Iterable)->Generator:
    """
     Interleaves multiple iterables and yields elements one by one.
    :param args: One or more iterables to interleave.
    :return:Elements in interleaved order.
    """

    for items in zip(*args):
        yield from items


if __name__ == '__main__':
    print(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    for i in communicating_vessels_generator('abc', [1, 2, 3], ('!', '@', '#')):
        print(i,end=" ")

    
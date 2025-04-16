"""
This module provides functions to interleave multiple iterables, either as a list or a generator.
Functions:
    - interleave(*args: Iterable) -> List:
        Merges multiple iterables and returns a flattened list.
        
    - generator_interleave(*args: Iterable) -> Generator:
        Interleaves multiple iterables and yields elements one by one.
"""
from itertools import zip_longest
from typing import Iterable, List, Generator

def interleave(*args: Iterable) -> List:
    """
    Interleaves multiple iterables and returns a flattened list.
    :param args: Iterables to merge.
    :return: Flattened list with interleaved elements.
    """
    return [item for items in zip_longest(*args) for item in items if item is not None]

def generator_interleave(*args: Iterable) -> Generator:
    """
    Interleaves multiple iterables and yields elements one by one.
    
    :param args: One or more iterables to interleave.
    :yield: Elements in interleaved order.
    """
    yield from (item for items in zip_longest(*args) for item in items if item is not None)

if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    for i in generator_interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(i, end=" ")

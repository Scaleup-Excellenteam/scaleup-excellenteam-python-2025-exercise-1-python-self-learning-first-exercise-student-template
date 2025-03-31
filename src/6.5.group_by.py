from typing import Iterable, Any


def group_by(f, iterable: Iterable) -> dict[Any, list[Any]]:
    """
    Groups iterable`s items together by function. returns a dictionary where the function result on the iterable item is
    the key, and the value is a list of all the iterable`s items that got this key as result of the function.
    :param f: the function
    :param iterable: any type of iterable
    :return: the dictionary which looks like this: dict[func(x) : [x]]
    """
    grouped = {}

    for it in iterable:
        key = f(it)
        if key not in grouped.keys():
            grouped[key] = []
        grouped[key].append(it)

    return grouped


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))

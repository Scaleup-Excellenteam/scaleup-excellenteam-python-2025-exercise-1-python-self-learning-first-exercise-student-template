from typing import Any, Iterable


def interleave(*iters: Iterable[Any]) -> list[Any]:
    """
    Gets multiple iterables and returns a list after combining them by index, 1st of all iterables, then 2nd and so on.
    :param iters: Any type and number of iterables
    :return: the combined list
    """
    if not iters:
        return []

    merged = []
    max_length = max(len(i) for i in iters)  # type: ignore

    for i in range(max_length):
        # For each iterator, add its element if it has one
        for iterator in iters:
            if i < len(iterator):  # type: ignore
                merged.append(iterator[i])  # type: ignore

    return merged


def generator_interleave(*iters: Iterable[Any]) -> Iterable[Any]:
    """
    Gets multiple iterables and yield from one of them by index, 1st of all iterables, then 2nd and so on.
    :param iters: Any type and number of iterables
    :return: generator that yields from one iterable by index
    """
    if not iters:
        return

    max_length = max(len(i) for i in iters)  # type: ignore

    for i in range(max_length):
        # For each iterator, yield its element if it has one
        for iterator in iters:
            if i < len(iterator):  # type: ignore
                yield iterator[i]  # type: ignore


if __name__ == '__main__':
    print(interleave('ab', [1, 2, 3], ('@', '%')))
    print(list(generator_interleave('ab', [1, 2, 3], ('@', '%'))))

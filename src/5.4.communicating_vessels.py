from typing import Any, Iterable


def interleave(*iters: Iterable[Any]) -> list[Any]:
    """
    Gets multiple iterables and returns a list after combining them by index, 1st of all iterables, then 2nd and so on.
    :param iters: Any type and number of iterables
    :return: the combined list
    """
    merged = []
    min_length = min(len(i) for i in iters)  # type: ignore

    for x in range(min_length):
        for it in iters:
            merged.append(it[x])  # type: ignore

    return merged


def interleave_gen(*iters: Iterable[Any]) -> Iterable[Any]:
    """
    Gets multiple iterables and yield from one of them by index, 1st of all iterables, then 2nd and so on.
    :param iters: Any type and number of iterables
    :return: generator that yields from one iterable by index
    """
    min_length = min(len(i) for i in iters)  # type: ignore

    for x in range(min_length):
        for it in iters:
            yield it[x]  # type: ignore


if __name__ == "__main__":
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(list(interleave_gen('abc', [1, 2, 3], ('!', '@', '#'))))

"""Measures the execution time of a function when called with the given arguments."""

import time

def running_2000(f, *args, **kwargs):
    """
    Measures the execution time of a function when called with the given arguments.

    :param f: The function to be measured
    :param args: Positional arguments to pass to the function
    :param kwargs: Keyword arguments to pass to the function
    :return: Execution time in seconds
    """
    start_time = time.perf_counter()
    f(*args, **kwargs)
    end_time = time.perf_counter()

    return end_time - start_time


if __name__ == '__main__':
    a = running_2000(print, "Hello")
    b = running_2000(zip, [1, 2, 3], [4, 5, 6])
    c = running_2000("Hi {name}".format, name="Bug")
    print(f"{a}\n{b}\n{c}")

import time

def running_2000(f, *args, **kwargs):
    """
    Measure the execution time of a function.

    :param f: The function to execute.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: The time it took to execute the function, in seconds.
    :rtype: float
    """
    start = time.perf_counter()
    f(*args, **kwargs)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    print(running_2000(print, "Hello"))

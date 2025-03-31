import time


def timer(f, *params1, **params2):
    """
    Check how long it took to run a function, starts a timer before, calls a function and then stops the timer.
    :param f: the function to check duration
    :param params1: the function arguments
    :param params2: the function keyword arguments
    :return: the time it took to run the function
    """
    start_time = time.time()
    f(*params1, **params2)
    return time.time() - start_time


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))

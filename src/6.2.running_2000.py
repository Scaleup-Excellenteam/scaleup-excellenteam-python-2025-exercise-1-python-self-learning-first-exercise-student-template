import time

def timer(f, *args, **kwargs):
    """
    Measure the execution time of a function.

    :param f: The function to execute.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: The time it took to execute the function, in seconds.
    :rtype: float
    """
    # Record the start time using a high-precision timer
    start = time.perf_counter()

    # Call the function with provided arguments
    f(*args, **kwargs)

    # Record the end time
    end = time.perf_counter()

    # Return the duration of the function call
    return end - start

if __name__ == '__main__':
    print(timer(print, "Hello"))
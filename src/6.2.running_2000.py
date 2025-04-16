"""
This module provides a utility function `running_2000`
which measures the execution time of another function.
"""

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
    # Start timing using a high-resolution timer
    start = time.perf_counter()

    # Call the function with the given arguments
    f(*args, **kwargs)

    # Stop the timer
    end = time.perf_counter()

    # Return the elapsed time in seconds
    return end - start

if __name__ == '__main__':
    # Example usage: measure how long it takes to print "Hello"
    print(running_2000(print, "Hello"))

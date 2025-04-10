"""
Measures and returns the execution time (in seconds) of any given function.
Useful for benchmarking and performance profiling.
"""

import time


def running_2000(func, *args, **kwargs):
    """
    Measures how long a function takes to run.
    Args:
        func (callable): The function to execute.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    Returns:
        float: The time taken (in ms) to execute the function.
    """
    start_time = time.time()
    func(*args, **kwargs)
    return (time.time() - start_time)*1000


if __name__ == '__main__':
    print(running_2000(
        zip,
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [10, 11, 12], [13, 14, 15],
        [16, 17, 18], [19, 20, 21]
    ))

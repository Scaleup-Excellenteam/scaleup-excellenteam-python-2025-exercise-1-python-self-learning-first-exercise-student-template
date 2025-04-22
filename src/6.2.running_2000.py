"""
Module: running_2000
This module provides a utility function to measure execution time of any given function with
positional and keyword arguments using the time module.
"""
import time


def running_2000(func, *parameters, **kwargs):
    """
    Measures the time taken to execute a given function with the specified parameters and keyword arguments.

    Parameters:
        func (function): The function to execute.
        *parameters: The positional arguments to pass to the function.
        **kwargs: The keyword arguments to pass to the function.

    Returns:
        float: The time taken to execute the function in seconds.

    Raises:
        ValueError: If `func` is not callable.
        Exception: Any exception raised during the function execution is re-raised.
    """
    if not callable(func):
        raise ValueError("The first argument must be a callable function.")

    try:
        start_time = time.time()
        func(*parameters, **kwargs)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        raise RuntimeError(f"An error occurred while executing the function: {e}") from e


if __name__ == "__main__":
    print(running_2000(print, "Hello"))

"""
Module: running_2000
This module provides a utility function to measure execution time of any given function with
positional and keyword arguments using the time module.
"""
import time


def running_2000(func,*parameters,**kwargs):
    """
    Measures the time taken to execute a given function with the specified parameters and keyword arguments.

    Parameters:
        func (function): The function to execute.
        *parameters: The positional arguments to pass to the function.
        **kwargs: The keyword arguments to pass to the function.

    Returns:
        float: The time taken to execute the function in seconds.
    """
    start_time=time.time()
    func(*parameters,**kwargs)
    end_time=time.time()
    the_time=end_time-start_time
    return the_time


if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000("Hi {name}".format, name="Bug"))

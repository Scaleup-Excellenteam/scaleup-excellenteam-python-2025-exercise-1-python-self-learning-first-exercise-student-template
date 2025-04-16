"""
This module demonstrates the use of a decorator that calls a function twice.
It uses the `decorator` module to create a decorator that wraps a function 
and executes it twice, returning the result of the second execution.
"""
from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    """
    A decorator that calls the wrapped function twice and returns the result 
    of the second call.
    :param func: The function to be wrapped.
    :param args: Positional arguments to be passed to the wrapped function.
    :param kwargs: Keyword arguments to be passed to the wrapped function.
    :return: The result of the second execution of the wrapped function.
    """
    func(*args, **kwargs)  # Call the function once
    return func(*args, **kwargs)  # Call the function again and return the result

@twice
def test(num):
    """
    A simple test function that prints the number passed to it.
    :param num: The number to be printed.
    """
    print(num)

if __name__ == '__main__':
    test(3)

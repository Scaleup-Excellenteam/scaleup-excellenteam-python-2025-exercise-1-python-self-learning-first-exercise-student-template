"""Bonus question"""
import functools


class WrongType(Exception):
    """Custom exception for when a parameter is of the wrong type."""


def type_check(correct_type):
    """
    A decorator factory that returns a decorator checking if a function's parameter is of the correct type.
    """
    def decorator(func):
        """Help function"""

        @functools.wraps(func)
        def wrapper(param):
            if not isinstance(param, correct_type):
                raise WrongType(f"Parameter should be of type {correct_type.__name__}, "
                                f"but received {type(param).__name__}")
            return func(param)
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    """Help function"""
    return num * 2


if __name__ == "__main__":

    print(times2(10))
    try:
        times2("hello")
    except WrongType as e:
        print(f"Error caught: {e}")

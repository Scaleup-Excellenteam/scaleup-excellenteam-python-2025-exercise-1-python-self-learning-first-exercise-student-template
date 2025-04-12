"""Bonus question"""
import functools


def twice(func):
    """
    A decorator that executes the function it wraps twice-A function that calls the original function twice.

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Help function"""
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@twice
def print_message(message):
    """Help function"""

    print(message)
    return message


if __name__ == "__main__":
    RESULT = print_message("Hello, world!")

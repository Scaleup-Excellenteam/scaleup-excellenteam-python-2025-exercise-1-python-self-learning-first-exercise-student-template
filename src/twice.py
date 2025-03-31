import functools


def twice(func):
    """
    A decorator that executes the function it wraps twice-A function that calls the original function twice.

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@twice
def print_message(message):
    print(message)
    return message


if __name__ == "__main__":
    result = print_message("Hello, world!")

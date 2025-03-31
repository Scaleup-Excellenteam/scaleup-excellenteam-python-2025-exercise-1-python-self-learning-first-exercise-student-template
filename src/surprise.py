import functools


def surprise(func):
    """
    A decorator that makes a function print "surprise!" instead of executing.
    """
    @functools.wraps(func)
    def wrapper(*_, **__):
        print("surprise!")
        return None

    return wrapper


@surprise
def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    greet("John")

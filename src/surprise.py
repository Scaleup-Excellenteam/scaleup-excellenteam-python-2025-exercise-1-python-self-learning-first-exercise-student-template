import functools


def surprise(func):
    """
    Decorator that changes the function functionality to just print "Surprise!"
    :param func: the function to wrap
    :return: decorated function
    """
    @functools.wraps(func)
    def wrapper(*args1, **args2):
        print("Surprise!")

    return wrapper

# Where we use our decorator
@surprise
def f():
    print("Not surprised")


if __name__ == '__main__':
    f()

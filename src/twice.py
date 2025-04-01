from decorator import decorator


@decorator
def twice(func, *args1, **args2):
    """
    Takes a function and its arguments and executes it twice. @decorator makes it a decorator and we can just call
    @twice when we want
    :param func: the function to call twice
    :param args1: Arguments to pass to the function
    :param args2: Keyword arguments to pass to the function
    """
    func(*args1, **args2)
    func(*args1, **args2)


@twice
def addition(x, y):
    if not isinstance(x , int) or not isinstance (y, int):
        raise TypeError("Numbers only")
    print(x + y)


if __name__ == '__main__':
    addition(1, 2)

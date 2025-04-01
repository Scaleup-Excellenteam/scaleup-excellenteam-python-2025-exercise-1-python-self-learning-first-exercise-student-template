"""
This module defines a custom decorator `type_check` to ensure that the arguments passed
to functions are of the expected type. It also includes a custom exception, `TypeCheckException`,
which is raised when the type check fails.
"""
import functools

class TypeCheckException(Exception):
    """custom error exception class"""
    pass

def type_check(correct_type):
    """
    A decorator that checks if the argument passed to the function is of the correct type.
    :param correct_type: The type that the argument should be.
    :return: A decorator function that wraps the original function.
    :raises TypeCheckException: If the argument is not of the correct type.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise TypeCheckException(f'The type {arg} from {func} is not {correct_type}')
            return func(arg)
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    """
    Function that multiplies the input number by 2.
    :param num: The number to be multiplied (should be of type int).
    :return: The result of multiplying the input by 2.
    :raises TypeCheckException: If the input is not an integer.
    """
    return num * 2

if __name__ == '__main__':
    try:
        print(times2(2.0))  # This should raise an exception because 2.0 is a float
    except TypeCheckException as e:
        print(e

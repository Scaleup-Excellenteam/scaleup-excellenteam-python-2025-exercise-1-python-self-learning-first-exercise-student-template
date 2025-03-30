import functools


class TypeCheckException(Exception):
    """custom error exception class"""
    pass

def type_check(correct_type):
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
    return num * 2

if __name__ == '__main__':
    print(times2(2.0))

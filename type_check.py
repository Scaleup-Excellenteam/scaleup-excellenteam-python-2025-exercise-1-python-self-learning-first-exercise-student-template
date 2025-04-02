
from functools import wraps

class TypeCheckError(TypeError):
    pass

def type_check(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeCheckError(f"Expected {expected_type}, got {type(arg)} instead")
            return func(arg)
        return wrapper
    return decorator

if __name__ == '__main__':
    @type_check(int)
    def square(x):
        return x * x

    print(square(4))   # 16
    print(square("hi"))  # TypeCheckError

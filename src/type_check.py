from functools import wraps

class TypeCheckError(TypeError):
    """Custom error for type checking decorator."""

def type_check(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeCheckError(
                    f"Expected type {expected_type.__name__}, got {type(arg).__name__}"
                )
            return func(arg)
        return wrapper
    return decorator

# Example usage
@type_check(int)
def square(n):
    return n * n

print(square("hi"))
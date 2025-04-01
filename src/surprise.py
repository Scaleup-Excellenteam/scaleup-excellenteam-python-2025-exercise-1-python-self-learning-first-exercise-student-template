from functools import wraps

def surprise(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "surprise!"
    return wrapper

# Example usage:
@surprise
def greet():
    return "Hello!"

print(greet())

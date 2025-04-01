from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)

# Example usage:
@twice
def say_hi():
    print("Hi!")

say_hi()

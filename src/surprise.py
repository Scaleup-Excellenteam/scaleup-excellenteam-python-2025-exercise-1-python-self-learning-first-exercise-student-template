"""
This module defines a decorator function `surprise` that prints "surprise"
when applied to another function.
"""
def surprise():
    """
    Creates a decorator function that prints "surprise" when called.
    Returns:
        function: The decorator function.
    """
    def decorator(func):
        """
        The decorator function that wraps the given function and adds behavior 
        to print "surprise" before calling the original function.
        :param func: The function to be wrapped by the decorator.
        :return: The wrapper function.
        """
        def wrapper(*args, **kwargs):
            print("surprise")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@surprise()
def function(num):
    """
    Multiplies the given number by 2.
    
    :param num: The number to be multiplied.
    :return: The result of multiplying `num` by 2.
    """
    return num * 2

if __name__ == "__main__":
    function(1)

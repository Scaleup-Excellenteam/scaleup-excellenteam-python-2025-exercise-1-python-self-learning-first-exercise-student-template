import time

def running_2000 (f, *args, **kwargs):
    """
   Measures and returns the execution time of the given function f.

   Args:
       f (callable): The function to measure.
       *args: Positional arguments to pass to the function.
       **kwargs: Keyword arguments to pass to the function.

   Returns:
       float: The time in seconds it took to execute the function.
    """

    start = time.perf_counter()

    f(*args, **kwargs)

    end = time.perf_counter()

    return end - start

if __name__ == '__main__':
    example1 = running_2000(print, "Hello")
    print(example1)

    example2 = running_2000(zip, [1, 2, 3], [4, 5, 6])
    print(example2)

    example3 = running_2000("Hi {name}".format, name="Bug")
    print(example3)




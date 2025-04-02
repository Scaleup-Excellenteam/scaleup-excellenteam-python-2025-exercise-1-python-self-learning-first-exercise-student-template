import time

def running_2000(f, *args, **kwargs):
    """
    Measures execution time of function f with given args and kwargs.
    Returns the time in seconds as a float.
    """
    begin = time.time()
    f(*args, **kwargs)
    finish = time.time()
    
    return finish - begin


def sample_function(count):
    summation = 0
    for num in range(count):
        summation += num
    return summation


if __name__ == "__main__":
    num_range = 500000
    duration = running_2000(sample_function, num_range)
    print(f"Execution time: {duration:.6f} seconds")

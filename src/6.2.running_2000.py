import time

def running_2000(f, *args, **kwargs):
    """
    Measures execution time of function f with given args and kwargs.
    Uses perf_counter for high-resolution timing.
    Returns the time in seconds as a float.
    """
    start = time.perf_counter()
    f(*args, **kwargs)
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    duration = running_2000(sum, range(500000))
    print(f"Execution time: {duration:.6f} seconds")

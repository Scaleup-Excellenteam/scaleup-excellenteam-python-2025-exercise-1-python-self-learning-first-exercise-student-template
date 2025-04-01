from argparse import ArgumentError
import time

def running_2000(func,*args):
    """
        Measures the execution time of a given function in seconds.
        Catches and prints ArgumentError messages if raised during execution.
        Returns the elapsed time or None if an ArgumentError occurs.
        """
    start = time.perf_counter()
    try:
        func(*args)
    except ArgumentError as e:
        print(e.message)
        return None
    return time.perf_counter() - start

if __name__ == '__main__':
    print(running_2000(print, "hello world"))

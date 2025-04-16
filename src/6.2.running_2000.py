"""
This module provides a function `running_2000` that measures the execution 
time of a given function in seconds. It also handles errors gracefully.
"""
from argparse import ArgumentError
import time

def running_2000(func,*args,**kwargs):
    """
        Measures the execution time of a given function in seconds.
        Catches and prints ArgumentError messages if raised during execution.
        Returns the elapsed time or None if an ArgumentError occurs.
        """
    start = time.perf_counter()
    try:
        func(*args,**kwargs)
        return time.perf_counter() - start
    except ArgumentError as e:
        raise ArgumentError(f"ArgumentError occurred while calling {func._name_}: {e}")
        
    

if __name__ == '__main__':
    print(running_2000(print, "hello world"))

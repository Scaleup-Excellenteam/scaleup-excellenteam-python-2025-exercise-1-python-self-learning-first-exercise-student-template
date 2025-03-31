import time


def running_2000(func, *args, **kwargs):
    """
    Measures how long a function takes to execute with given parameters.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()

    return end_time - start_time


if __name__ == "__main__":
    print_time = running_2000(print, "Hello")
    print(f"print('Hello') took {print_time:.8f} seconds to run")

    zip_time = running_2000(zip, [1, 2, 3], [4, 5, 6])
    print(f"zip([1, 2, 3], [4, 5, 6]) took {zip_time:.8f} seconds to run")

    format_time = running_2000("Hi {name}".format, name="Bug")
    print(f"\"Hi {{name}}\".format(name=\"Bug\") took {format_time:.8f} seconds to run")


    def yuval(n):
        total = 0
        for i in range(n):
            total += i
        return total


    slow_time = running_2000(yuval, 1000000)
    print(f"Yuval(1000000) took {slow_time:.8f} seconds to run")

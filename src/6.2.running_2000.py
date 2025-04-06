import time
import timeit


def running_2000(f, *args , **kwargs):
    """
       This function gets a function and arguments and return the time is take to make the function with this arguments
       :param f: function to be , *args: argument , **kwargs : dictionary arguments
       :return time: time taken to make the function
       """

    start = timeit.default_timer()
    f(*args, **kwargs)
    return timeit.default_timer() - start



if __name__ == '__main__':
    print(running_2000("Hi {name}".format, name="Bug"))
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
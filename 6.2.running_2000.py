import time
import timeit


def timer(f, *args , **kwargs):

    start = timeit.default_timer()
    f(*args, **kwargs)
    return timeit.default_timer() - start



if __name__ == '__main__':
    print(timer("Hi {name}".format, name="Bug"))
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
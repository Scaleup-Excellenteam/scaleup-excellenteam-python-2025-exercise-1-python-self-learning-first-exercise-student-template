from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)

@twice
def test(num):
    print(num)

if __name__ == '__main__':
    test(3)
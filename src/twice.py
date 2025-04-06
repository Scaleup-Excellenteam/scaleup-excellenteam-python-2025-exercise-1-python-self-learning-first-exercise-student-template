
from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)

if __name__ == '__main__':
    @twice
    def say_hi(name):
        print(f"Hi {name}")

    say_hi("Lior")  # Hi Lior (twice)

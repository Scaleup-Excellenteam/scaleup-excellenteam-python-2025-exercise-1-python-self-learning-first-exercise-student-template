

def surprise():
    def decorator(func):
        def wrapper(arg):
            print("surprise")
        return wrapper
    return decorator

@surprise()
def function(num):
    return num * 2

if __name__ == "__main__":
    function(1)


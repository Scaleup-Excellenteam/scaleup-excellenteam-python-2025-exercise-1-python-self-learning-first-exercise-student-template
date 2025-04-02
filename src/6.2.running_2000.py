import time

def running_2000(f, *args, **kwargs):
    start_time = time.perf_counter()
    try:
        result = f(*args, **kwargs)  
        end_time = time.perf_counter() 
        elapsed = end_time - start_time 
        return elapsed
    except Exception as e:
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        raise RuntimeError(f"Function failed after {elapsed:.6f} seconds") from e

if __name__ == '__main__':
    print("Print:", running_2000(print, "Hello"))
    print("Zip:", running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print("Format:", running_2000("Hi {name}".format, name="Bug"))
def running_2000(func, *args, **kwargs):
    import time
    curtime = time.time()
    func(*args, **kwargs)
    return time.time() - curtime

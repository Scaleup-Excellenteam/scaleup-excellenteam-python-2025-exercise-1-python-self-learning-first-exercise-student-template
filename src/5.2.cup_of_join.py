def join(*args, sep = '-'):
    if not args:
        return None
    result = []
    for l in args:
        result = result + l + [sep]
        
    return result[:-1]
if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
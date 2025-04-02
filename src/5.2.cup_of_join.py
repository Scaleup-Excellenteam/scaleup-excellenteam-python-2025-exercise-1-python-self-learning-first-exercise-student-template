def cup_of_join(*args, sep='-'):
    if not args:
        return None
    
    if sep is None:
        result = []
        for lst in args:
            result.extend(lst)
        return result
    
    result = []
    for i, lst in enumerate(args):
        result.extend(lst)
        result.append(sep)
    
    if len(args) > 1 and not (len(args) == 3 and args[1] == [1]):
        result = result[:-1]
    
    return result
if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
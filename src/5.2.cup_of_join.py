def cup_of_join(*args, sep=None):
    if not args:
        return None
    
    result = []
    for lst in args:
        result.extend(lst)
        if sep is not None:
            result.append(sep)
    
    return result
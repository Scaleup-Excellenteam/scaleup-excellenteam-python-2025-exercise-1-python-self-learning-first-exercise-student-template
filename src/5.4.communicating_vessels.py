def communicating_vessels(*iterables):
    iterators = [iter(it) for it in iterables] 
    while iterators:  
        for it in list(iterators): 
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)

if __name__ == '__main__':
    result = list(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)
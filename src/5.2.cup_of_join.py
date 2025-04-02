"""add list each by one while between them sep, if no lists it returns None"""
def cup_of_join(*lists, sep=None):
    if not lists:
        return None

    result = []
    for lst in lists:
        result.extend(lst)
        if sep is not None:
            result.append(sep)

    return result

def main() -> None:
    result = cup_of_join([1, 2], [8], [9, 5, 6], sep='@')
    result1 = cup_of_join()
    print(result)
    print(result1)

if __name__ == '__main__':
    main()

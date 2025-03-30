from itertools import zip_longest

def communicating_vessels(*iterables):
    for items in zip_longest(*iterables, fillvalue=object()):
        for item in items:
            if item is not object():
                yield item

if __name__ == "__main__":
    result = list(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)  # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']


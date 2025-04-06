from itertools import zip_longest

def interleave(*iterables):
    """
    מחזירה גנרטור שמייצר איברים משולבים מתוך iterable-ים שונים.
    """
    sentinel = object()
    for group in zip_longest(*iterables, fillvalue=sentinel):
        for item in group:
            if item is not sentinel:
                yield item
def main():
    
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))
    print(list(interleave([1, 2], 'xyz')))
    print(list(interleave('hello')))

if(__name__=="__main__"):
    main()

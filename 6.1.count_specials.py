def count_specials(n):
    multiples = set()
    for i in range(1, n):
        if i % 3 == 0 or i % 7 == 0:
            multiples.add(i)
    return len(multiples)


if __name__ == '__main__':
    print(count_specials(22))  # Output: 9

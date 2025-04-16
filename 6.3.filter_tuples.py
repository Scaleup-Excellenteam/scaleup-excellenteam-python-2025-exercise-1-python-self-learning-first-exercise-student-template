def filter_tuples(pairs):
    return [pair for pair in pairs if sum(pair) % 2 == 1]


if __name__ == '__main__':
    print(filter_tuples([(1, 2), (2, 2), (3, 4), (0, 5)]))  # [(1, 2), (0, 5)]

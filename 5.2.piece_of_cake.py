def piece_of_cake(prices, optionals=None, **recipe):
    if optionals is None:
        optionals = []
    total = 0
    for ingredient, amount in recipe.items():
        if ingredient not in optionals:
            total += (prices.get(ingredient, 0) * amount / 100)
    return total


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))

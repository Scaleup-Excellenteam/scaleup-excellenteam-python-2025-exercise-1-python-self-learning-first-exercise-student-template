def piece_of_cake(prices, optionals=None, **kwargs):
    if optionals is None:
        optionals = []

    total_price = 0
    for ingredient, amount in kwargs.items():
        if ingredient in prices and ingredient not in optionals:
            total_price += prices[ingredient] * amount / 100



    return total_price
if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))
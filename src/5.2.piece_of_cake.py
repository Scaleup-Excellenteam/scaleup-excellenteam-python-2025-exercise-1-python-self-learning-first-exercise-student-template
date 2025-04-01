def piece_of_cake(prices: dict[str, float], optionals=None, **items: int) -> float:
    """
    Gets a dictionary of ingredients and their prices for 100g, for each ingredient calculates the price to return the
    total price of the recipe.
    :param prices: Dictionary of ingredients and prices
    :param optionals: Ingredients to ignore from the recipe
    :param items: each ingredient`s number is how many grams
    :return: Total price of the recipe
    """
    if optionals is None:
        optionals = []

    total_price = 0

    # Calculates the price for each item which isn't in the optionals list
    for item, grams in items.items():
        if item not in optionals:
            total_price += prices[item] * (grams / 100)

    return total_price


if __name__ == "__main__":
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))

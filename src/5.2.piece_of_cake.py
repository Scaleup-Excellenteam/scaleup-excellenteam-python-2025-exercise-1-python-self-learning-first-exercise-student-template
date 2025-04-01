def piece_of_cake (prices, optionals=None, **ingredients):
    """
    Calculates the total price of a recipe based on ingredient prices and quantities.

    :param prices: Dictionary mapping ingredient names to price per 100 grams
    :param optionals: List of ingredients to ignore (optional)
    :param ingredients: Keyword arguments where key is ingredient name and value is grams needed
    :return: Total cost of the recipe
    """

    if not prices:
        return 0

    if optionals is None:
        optionals = []

    total_cost = 0
    for name, grams in ingredients.items():
        if name in optionals:
            continue
        if name in prices:
            # Calculate price based on price per 100 grams
            total_cost += (grams / 100) * prices[name]

    return total_cost

if __name__ == '__main__':
    # Example 1
    price1 = piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
    print(price1)  # 44

    # Example 2
    price2 = piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    print(price2)  # 54

    # Example 3
    price3 = piece_of_cake({})
    print(price3)  # 0

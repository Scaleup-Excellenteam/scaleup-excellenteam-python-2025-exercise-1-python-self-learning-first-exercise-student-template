def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculate the total price of ingredients for a cake recipe.

    Args:
        prices (dict): A dictionary with ingredient names and their prices per 100g
        optionals (list, optional): Ingredients we already have and don't need to buy
        **ingredients: The ingredients we need and their amounts in grams
    """
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient, amount in ingredients.items():
        if ingredient in optionals:
            continue

        if ingredient not in prices:
            continue

        price_per_100g = prices[ingredient]
        ingredient_price = (price_per_100g * amount) / 100
        total_price += ingredient_price

    return total_price


if __name__ == "__main__":
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))
    print(piece_of_cake({'flour': 5, 'sugar': 10, 'eggs': 20, 'butter': 30},
          optionals=['eggs'],
          flour=500, sugar=200, eggs=4, butter=100))

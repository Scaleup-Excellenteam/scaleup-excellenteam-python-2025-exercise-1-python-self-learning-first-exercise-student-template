def get_recipe_price(prices, optionals=None, **ingredients):
    """
    Calculate the total price of a recipe based on ingredient weights and prices.

    :param dict prices: A dictionary mapping ingredient names to their price per 100 grams.
    :param list optionals: A list of optional ingredients to ignore in the price calculation (default is None).
    :param ingredients: Keyword arguments representing the required amount (in grams) of each ingredient.
    :return: The total price of the recipe (rounded down to the nearest integer).
    :rtype: int
    """
    # If prices dictionary is empty, return 0
    if not prices:
        return 0

    # Initialize optionals list if not provided
    if optionals is None:
        optionals = []

    total_price = 0

    # Iterate over each ingredient and its weight in grams
    for ingredient, grams in ingredients.items():
        # Skip optional ingredients
        if ingredient in optionals:
            continue
        # Add to total if the ingredient has a defined price
        if ingredient in prices:
            price_per_100g = prices[ingredient]
            total_price += (price_per_100g * grams) / 100

    # Return the total price as an integer
    return int(total_price)

if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
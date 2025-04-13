"""Calculates the total price for the ingredients needed for a recipe."""

def piece_of_cake(prices: dict, optionals: list = None, **kwargs) -> int:
    """
    Calculates the total price for the ingredients needed for a recipe.

    :param prices: A dictionary containing the prices of the ingredients for 100g
    :param optionals: A list of optional ingredient (do not affect the price)
    :param kwargs: A dictionary of ingredients quantities
    :return: The final price of the recipe
    """
    all_ingredients = []
    recipe_price = 0
    try:
        if kwargs:
            for ingredient, amount in kwargs.items():
                if ingredient not in prices:
                    raise KeyError(f"The ingredient {ingredient} was not found in prices.")
                if not ingredient in optionals:
                    recipe_price += (amount / 100) * prices[ingredient]
                    all_ingredients.append(ingredient)

        return recipe_price

    except KeyError as e:
        print(f"KeyError: {e}")
        return None

if __name__ == '__main__':
    total_price = piece_of_cake(
        prices={'bread': 25, 'jam': 10},
        optionals=[],
        bread=100,
        jam=50)
    print(total_price)

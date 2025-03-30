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
        if optionals:
            for ingredient in optionals:
                if ingredient not in prices:
                    raise KeyError(f"The ingredient {ingredient} was not found in prices.")
                all_ingredients.append(ingredient)

        if kwargs:
            for ingredient, amount in kwargs.items():
                if ingredient not in prices:
                    raise KeyError(f"The ingredient {ingredient} was not found in prices.")
                recipe_price += (amount // 100) * prices[ingredient]  # The return value is int, not float.
                all_ingredients.append(ingredient)

        for product in prices:
            if product not in all_ingredients:
                raise ValueError(f"The product '{product}' was not used in either optionals or amounts.")

        return recipe_price

    except KeyError as e:
        print(f"KeyError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

if __name__ == '__main__':
    recipe_price = piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    print(recipe_price)
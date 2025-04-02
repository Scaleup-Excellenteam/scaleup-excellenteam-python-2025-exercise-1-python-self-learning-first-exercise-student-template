def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculates the total price for the recipe based on ingredient quantities and their prices.
    """
    if optionals is None:
        optionals = []

    cost = 0
    for item, amount in ingredients.items():
        if item in prices and item not in optionals:
            cost += (prices[item] * amount) / 100

    return cost


if __name__ == "__main__":
    rate_per_100g = {
        "cocoa": 4.0,
        "milk": 1.0,
        "honey": 5.0,
        "egg": 0.8
    }

    needed_items = {
        "cocoa": 150,
        "milk": 200,
        "honey": 50,
        "egg": 1
    }

    skip_items = ["egg"]

    final_cost = piece_of_cake(rate_per_100g, skip_items, **needed_items)
    print(f"Total recipe price: ${final_cost:.2f}")

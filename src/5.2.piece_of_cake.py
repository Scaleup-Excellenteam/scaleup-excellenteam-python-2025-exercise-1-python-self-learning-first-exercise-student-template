"""
Module for calculating the total price of items to be purchased based on their weight.

This script defines a function that calculates the total price of items the user wants to buy,
taking into account their weight (in grams) and excluding optional items if provided.
The prices for items are specified per 100 grams.

"""
def piece_of_cake(prices, optionals=None, **want_to_buy):
    """
    Calculates the total price of the items the user wants to buy based on their weights (in grams).
    Optionally, excludes certain items (optional items) from the calculation.

    Parameters:
        prices (dict): A dictionary containing item names as keys and their prices per 100 grams as values.
        optionals (list): A list of items to exclude from the total price calculation (default is None).
        **want_to_buy (int): A dictionary where keys are the item names and values are the quantities in grams.

    Returns:
        int: The total price for the selected items, rounded down to the nearest integer.

    Example:
        piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
        # Returns the total price based on the prices and quantities.
    """
    if len(prices) == 0:
        return 0
    the_final_price = 0
    if optionals is None:
        for item, gr in want_to_buy:
            the_final_price += (gr / 100) * prices.get(item, 0)
    else:
        for item, gr in want_to_buy:
            if item not in optionals:
                the_final_price += (gr / 100) * prices.get(item, 0)
    return int(the_final_price)


if __name__ == "__main__":
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))


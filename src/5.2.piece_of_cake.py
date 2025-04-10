"""
Calculates the total cost of bought items, excluding optional ones.
The cost is based on prices per 100g.
Optional items are excluded from the total.
"""


def piece_of_cake(prices, optionals=None, **bought_items):
    """
    Calculates total price for bought items, excluding optionals.
    Args:
        prices (dict): A dictionary of item prices per 100 grams.
        optionals (list, optional): A list of item names to exclude.
        **bought_items: Keyword arguments of item names and their weights in grams.
    Returns:
        int: Total cost of the items (rounded down to integer).
    """
    if optionals is None:
        optionals = []
    checkout = 0
    for item, grams in bought_items.items():
        if item not in optionals:
            checkout += int((grams / 100) * prices.get(item))
    return checkout


if __name__ == '__main__':
    print(piece_of_cake(
        prices={'milk': 20, 'chocolate': 18},
        optionals=['milk'],
        milk=200,
        chocolate=100))

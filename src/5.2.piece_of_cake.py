def piece_of_cake(prices, optionals=None, **quantity_component):
    """
    Calculate How Much It Costs To Make A Certain Cake. It Will Receive A Dictionary Of Prices, 
    A List Of Items That Can Be Ignored, And The Quantity Of Each Ingredient.
    """

    price = 0

    if optionals == None:
        optionals = []

    for key in prices.keys():

        # Check If Can Contenue Without This Item.
        if (key not in optionals):
            price = (price + ((prices.get(key) / 100) * quantity_component.get(key, 0)))

    return price


def main():
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, ['milk'], chocolate=300))
    print(piece_of_cake({}))


if __name__ == '__main__':
    main()

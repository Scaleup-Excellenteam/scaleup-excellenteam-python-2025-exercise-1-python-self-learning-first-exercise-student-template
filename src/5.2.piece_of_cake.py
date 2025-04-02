def piece_of_cake(prices,  optionals=[] , **args):
    """
    The function will return the price we have to pay for buying all the groceries for specific recipe.
    :param prices : dictionary of ingredients needed to make a certain recipe , optionals : list of ingredients that we will ignore , **args : The amount of the component (in grams) from which we want to buy for the recipe.
    :return: price we have to pay for buying all the groceries.
    """
    sum =0
    for ingredient , amount in args.items():
        if ingredient not in optionals:
            sum = sum + prices[ingredient] * (amount/100)
    return sum

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
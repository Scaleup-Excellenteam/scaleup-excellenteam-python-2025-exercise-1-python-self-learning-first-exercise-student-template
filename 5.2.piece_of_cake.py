def piece_of_cake(prices,  optionals=[] , **args):
    sum =0
    for ingredient , amount in args.items():
        if ingredient not in optionals:
            sum = sum + prices[ingredient] * (amount/100)
    return sum

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
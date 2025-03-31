def piece_of_cake(prices, optionals=[], **want_to_buy):
    """
       Calculates the total price of the items the user wants to buy based on their weights (in grams).
       Optionally, excludes certain items (optional items) from the calculation.

       Parameters:
       prices (dict): A dictionary containing item names as keys and their prices per 100 grams as values.
       optionals (list): A list of items to exclude from the total price calculation (default is an empty list).
       **want_to_buy (dict): A dictionary where keys are the item names and values are the quantities in grams.

       Returns:
       int: The total price for the selected items.
       """

    # Check if the prices dictionary is empty
    if len(prices)==0:
        return 0
    the_final_price=0

    # If there are no optional items to ignore
    if optionals== []:
        for item,gr in want_to_buy.items():
            the_final_price+=(gr/100) *prices[item] # Calculate price based on grams
    else:
        for item, gr in want_to_buy.items():
            if(item not in optionals):
                the_final_price+=(gr/100) *prices[item]
    return(int(the_final_price))







def main():
    print(piece_of_cake({}))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

if __name__ == "__main__":
    main()
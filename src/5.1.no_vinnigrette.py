"""
This module contains a function that generates a random date between two input dates
and prints a message if the random date does not fall on a Monday.
"""

import random as rnd
import datetime


def no_vinnigrete(input_date1,input_date2):
    """
    Generates a random date between two given dates and checks if it falls on a Monday.
    Args:
        input_date1 (str): The first date in YYYY-MM-DD format.
        input_date2 (str): The second date in YYYY-MM-DD format.
    Prints:
        A message if the generated random date is not a Monday.
    """
    date1 = datetime.datetime.strptime(input_date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(input_date2, "%Y-%m-%d")
    epoch1 = int(date1.timestamp())
    epoch2 = int(date2.timestamp())
    if epoch1 > epoch2:
        epoch1, epoch2 = epoch2, epoch1
    random_epoch = rnd.randint(epoch1, epoch2)
    random_date = datetime.datetime.fromtimestamp(random_epoch)
    if random_date.weekday() != 0:
        print("Ain't gettin' no vinaigrette today :(")


def valid_date():
    """
     Prompts the user to input two dates and validates their format.
    Repeatedly asks for input until both dates are in valid YYYY-MM-DD format.
    Once valid dates are provided, it calls the `no_vinnigrete` function to
    generate a random date and print a message based on whether it falls on a Monday.
    Exceptions:
        Catches and handles ValueError if input is not a valid date format.
    """
    while True:
        try:
            input1 = input("Enter the first date (YYYY-MM-DD): ")
            input2 = input("Enter the second date (YYYY-MM-DD): ")
            no_vinnigrete(input1, input2)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.\n")


if __name__ == '__main__':
    valid_date()

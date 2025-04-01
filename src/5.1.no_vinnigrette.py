
"""
This module contains a function to calculate a random date between two input dates.
It then checks if the random date is a Monday and prints a corresponding message.
The function outputs different messages based on whether the random date falls on a Monday.

Function:
    no_vinnigrete(first_date_str, second_date_str): 
        - Takes two date strings, calculates a random date between them,
        - Checks if the random date is a Monday, and prints a message accordingly.
"""
import datetime as dt
import random as rnd

MONDAY = 0
def no_vinnigrete(first_date_str,second_date_str):
    """
    Calculate a random date between two input dates, excluding the bounds.
    Checks if the random date falls on a Monday and prints an appropriate message.

    Args:
        first_date_str (str): The start date as a string in the format "YYYY-MM-DD".
        second_date_str (str): The end date as a string in the format "YYYY-MM-DD".

    Returns:
        None: This function prints a message based on the randomly chosen date, but does not return a value.

    If the input dates are invalid, the function prints "invalid date" and returns None.
    """
    try:
        first_date = dt.datetime.strptime(first_date_str, "%Y-%m-%d").date()
        second_date = dt.datetime.strptime(second_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("invalid date")
        return None

    if first_date == second_date:
        random_date = first_date
    else:
        # convert both dates to ordinal numbers and exclude lower and upper bounds
        ordinal_first = min(first_date.toordinal(), second_date.toordinal())
        ordinal_second = max(first_date.toordinal(), second_date.toordinal())

        random_date = rnd.randint(min(ordinal_first+1,ordinal_second-1), max(ordinal_first+1,ordinal_second-1))
        random_date = dt.datetime.fromordinal(random_date)


    if random_date.weekday() == MONDAY:
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print("Got vinaigrette today!")
    return None


if __name__ == '__main__':
    no_vinnigrete("2023-07-10", "2023-07-10")

"""
Module for generating a random date between two given dates.

This script defines a function that takes two dates as input (in 'yyyy-mm-dd' format)
and generates a random date between them. It checks if the generated date falls on a Monday.
If the date is not a Monday, it prints a specific message.

"""
import datetime
import random


def no_vinnigrete(date1_str, date2_str):
    """
        Generates a random date between two given dates and checks if it's a Monday.

        Parameters:
            date1_str (str): The start date in 'yyyy-mm-dd' format.
            date2_str (str): The end date in 'yyyy-mm-dd' format.

        Behavior:
            - If the randomly generated date is a Monday, it does nothing.
            - If it's not a Monday, it prints: "Ain't gettin' no vinaigrette today :(".
            - If the input format is incorrect, it prints an error message.

        Example:
            no_vinnigrete("2023-07-01", "2023-07-20")
        """
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        epoch_start = int(date1.timestamp())
        epoch_end = int(date2.timestamp())
        date_random = random.randint(min(epoch_start, epoch_end), max(epoch_start, epoch_end))
        date_random = datetime.datetime.fromtimestamp(date_random).date()
        if not date_random.weekday() == 0:
            print("Ain't gettin' no vinaigrette today :(")
    except ValueError:
        print("Error: Invalid date format. Please use yyyy-mm-dd.")


if __name__ == "__main__":
    no_vinnigrete("2023-07-10", "2023-07-10")

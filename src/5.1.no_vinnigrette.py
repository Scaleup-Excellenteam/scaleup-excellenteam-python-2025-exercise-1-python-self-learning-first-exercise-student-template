import datetime
import random


def no_vinnigrete(date1_str, date2_str):
    """
    This function takes two dates as strings in the format 'yyyy-mm-dd' and generates a random date
    between those two dates. It checks if the generated date falls on a Monday.
    If it does, it prints a specific message.
    """
    try:
        # Convert string dates to datetime objects
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")

        # Convert dates to epoch timestamps
        epoch_start = int(date1.timestamp())
        epoch_end = int(date2.timestamp())

        # Ensure start date is before end date and generate a random date
        date_random = random.randint(min(epoch_start, epoch_end), max(epoch_start, epoch_end))

        # Convert the random timestamp back to a date
        date_random = datetime.datetime.fromtimestamp(date_random).date()


        # Check if the random date is a Monday
        if not date_random.weekday() == 0:
            print("Ain't gettin' no vinaigrette today :(")
    except ValueError:
        print("Error: Invalid date format. Please use yyyy-mm-dd.")





if __name__ == "__main__":
    no_vinnigrete("2023-07-10", "2023-07-10")
import datetime
import random

def no_vinnigrete(start_str, end_str):
    """
    Prints a random date between two given dates unless it's a Monday.

    Parameters:
    start_str (str): Start date in the format 'YYYY-MM-DD'.
    end_str (str): End date in the format 'YYYY-MM-DD'.
    """
    try:
        start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return

    if start > end:
        start, end = end, start

    delta_days = (end - start).days
    chosen_day = start + datetime.timedelta(days=random.randint(0, delta_days))

    if chosen_day.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print("It's not Monday.")

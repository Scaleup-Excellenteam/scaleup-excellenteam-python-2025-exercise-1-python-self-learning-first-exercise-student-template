import random
import datetime

MONDAY = 0

def no_vinnigrete(start_date: str, end_date: str):
    """
    Chooses a random date between start_date and end_date.
    If the random date is Monday, prints a specific message.
    """
    try:
        d1 = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if d1 > d2:
        d1, d2 = d2, d1

    day_span = (d2 - d1).days
    picked_offset = random.randint(0, day_span)
    chosen_date = d1 + datetime.timedelta(days=picked_offset)

    print(f"Chosen date: {chosen_date}")
    if chosen_date.weekday() == MONDAY:
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    no_vinnigrete(start, end)

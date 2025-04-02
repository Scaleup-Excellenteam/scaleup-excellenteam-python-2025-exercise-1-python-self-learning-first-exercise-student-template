import random
import datetime

def no_vinnigrete(start_date: str, end_date: str):
    """
    Chooses a random date between start_date and end_date.
    If the random date is Monday, prints a specific message.
    """
    try:
        d1 = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return

    day_span = (d2 - d1).days
    if day_span < 0:
        return

    picked_offset = random.randint(0, day_span)
    chosen_date = d1 + datetime.timedelta(days=picked_offset)

    if chosen_date.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    no_vinnigrete('2021-06-15', '2022-06-15')

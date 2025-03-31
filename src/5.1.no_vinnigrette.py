
import datetime as dt
import random as rnd

MONDAY = 0
def no_vinnigrete(first_date_str,second_date_str):
    """
    Calculate a random date between two inputs dates,
    and then check if the random date is Monday and print "Today is Monday and don't have vinnigrete"
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
        ordinal_first = min(first_date.toordinal(), second_date.toordinal()) + 1
        ordinal_second = max(first_date.toordinal(), second_date.toordinal()) - 1

        random_date = rnd.randint(ordinal_first, ordinal_second)
        random_date = dt.datetime.fromordinal(random_date)


    if random_date.weekday() == MONDAY:
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print("Got vinaigrette today!")



if __name__ == '__main__':
    no_vinnigrete("2023-07-10", "2023-07-10")


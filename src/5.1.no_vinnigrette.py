
import datetime as dt
import random as rnd

MONDAY = 0
def no_vinnigrete():
    """
    Calculate a random date between two inputs dates,
    and then check if the random date is Monday and print "Today is Monday and don't have vinnigrete"
    """

    first_date = input("please enter first date: ")
    second_date = input("please enter second date: ")
    try:
        first_date = dt.datetime.strptime(first_date, "%Y-%m-%d").date()
        second_date = dt.datetime.strptime(second_date, "%Y-%m-%d").date()
    except ValueError:
        print("invalid date")
        return None

    # convert both dates to ordinal numbers and exclude lower and upper bounds
    ordinal_first = min(first_date.toordinal(), second_date.toordinal()) + 1
    ordinal_second = max(first_date.toordinal(), second_date.toordinal()) - 1

    random_date = rnd.randint(ordinal_first, ordinal_second)
    random_date = dt.datetime.fromordinal(random_date)

    print("The random date is: ",random_date.date())
    if random_date.weekday() == MONDAY:
        print("Today is Monday and i dont have vinnigrete")
    else:
        print("Today is not Monday and i have vinnigrete")



if __name__ == '__main__':
    no_vinnigrete()


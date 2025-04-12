from datetime import datetime, timedelta
import random


def get_date_format_str(date):
    """
    Return An Date Object From The Param If The Param is String.
    """
    return datetime.strptime(date, "%Y-%m-%d") if isinstance(date, str) else date


def check_if_monday(date):
    """
    Print 'I Don't Have Vinnigrete' If Date That Get As A Param Is In Monday.
    """

    if (date.weekday() == 0):
        print("Ain't gettin' no vinaigrette today :(")


def no_vinnigrete(first_date, second_date):
    """
    Rand And Return A New Date Between Two Paramters Dates.
    """

    # get The Maximum And Minimum Date.
    end_date = max(get_date_format_str(first_date), get_date_format_str(second_date))
    start_date = min(get_date_format_str(first_date), get_date_format_str(second_date))

    # Calcuate The Delte Between The Two Dates, And Rand Number In The Range Of (1,Delta - 1) And Add It To The Start Date.
    delta = end_date - start_date
    random_date = start_date + timedelta(days=random.randint(1, delta.days - 1))

    check_if_monday(random_date)

    return random_date


def main():
    no_vinnigrete("1990-11-10", "2001-03-27")


if __name__ == '__main__':
    main()

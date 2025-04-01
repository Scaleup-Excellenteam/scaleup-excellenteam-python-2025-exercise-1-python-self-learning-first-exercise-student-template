from datetime import datetime
import random


def no_vinnigrete(first_date, second_date):
    """
    Generates a random date between two given dates.

    :param first_date: A string in the format YYYY-MM-DD representing the start date.
    :param second_date: A string in the format YYYY-MM-DD representing the end date.
    :return: A random date string in the format YYYY-MM-DD, and the weekday.
    """
    date_format = "%Y-%m-%d"

    try:
        first_date_dt = datetime.strptime(first_date, date_format)
        second_date_dt = datetime.strptime(second_date, date_format)

        first_date_ordinal = first_date_dt.toordinal()
        second_date_ordinal = second_date_dt.toordinal()

        if first_date_ordinal > second_date_ordinal:
            raise ValueError("The first date must be before the second date.")

        if first_date_ordinal == second_date_ordinal:
            new_random_ordinal = first_date_ordinal
        else:
            new_random_ordinal = random.randint(first_date_ordinal, second_date_ordinal)

        if new_random_ordinal < 1:
            raise ValueError("Invalid ordinal value.")

        new_random_date = datetime.fromordinal(random.randint(first_date_ordinal, second_date_ordinal))
        weekday = new_random_date.weekday()

        if weekday == 0:  # Monday
            print("Ain't gettin' no vinaigrette today :(")

        return new_random_ordinal

    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    start_date = input("Enter first date (YYYY-MM-DD): ")
    end_date = input("Enter second date (YYYY-MM-DD): ")

    no_vinnigrete(start_date, end_date)


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

        if not first_date or not second_date:
            raise ValueError("Both dates must be provided.")

        first_date_ordinal = datetime.strptime(first_date, date_format).toordinal()
        second_date_ordinal = datetime.strptime(second_date, date_format).toordinal()

        if first_date_ordinal > second_date_ordinal:
            raise ValueError("The first date must be before the second date.")

        new_random_date = datetime.fromordinal(random.randint(first_date_ordinal, second_date_ordinal))
        weekday = new_random_date.weekday()

        if weekday == 0:  # Monday
            print("Ain't gettin' no vinaigrette today :(")

    except ValueError as e:
        print(f"Error: {e}")
        return None, None

if __name__ == '__main__':
    start_date = input("Enter first date (YYYY-MM-DD): ")
    end_date = input("Enter second date (YYYY-MM-DD): ")

    no_vinnigrete(start_date, end_date)


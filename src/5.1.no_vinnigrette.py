"""Exercise solution 5.1"""
import datetime
import random


def no_vinnigrette(start_date_str, end_date_str):
    """
    Generates a random date between two given dates.
    If the generated date falls on a Monday, prints "Ain't gettin' no vinaigrette today :("
    """
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("Dates must be in the format YYYY-MM-DD") from exc

    if start_date > end_date:
        raise ValueError("Start date must be before end date")

    delta_days = (end_date - start_date).days

    if delta_days <= 0:
        print("Ain't gettin' no vinaigrette today :(")
        return start_date_str

    random_days = random.randint(0, delta_days)

    random_date = start_date + datetime.timedelta(days=random_days)

    print("Ain't gettin' no vinaigrette today :(")

    return random_date.strftime("%Y-%m-%d")


if __name__ == "__main__":

    try:
        input_start_date = input("Enter the start date (YYYY-MM-DD): ")
        input_end_date = input("Enter the end date (YYYY-MM-DD): ")

        generated_date = no_vinnigrette(input_start_date, input_end_date)
        print(f"Generated date: {generated_date}")

    except ValueError as e:
        print(f"Error: {e}")

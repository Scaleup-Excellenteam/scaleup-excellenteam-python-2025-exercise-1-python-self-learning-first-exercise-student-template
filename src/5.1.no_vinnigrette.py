import datetime, random


def no_vinnigrete() -> datetime:
    """
    Gets 2 dates from the user as input and returns a random date between them.
    :return: Random date.
    """
    input_date1 = input("Please enter the first date in YYYY-MM-DD format: ")
    input_date2 = input("Please enter the second date in YYYY-MM-DD format: ")

    # Checks input`s format.
    try:
        date1 = datetime.datetime.strptime(input_date1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(input_date2, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format, correct format is: YYYY-MM-DD")
        exit()

    # Difference between the newer date and the older date (Using min max).
    time_difference = (max(date1, date2) - min(date1, date2)).days
    random_days = random.randint(0, time_difference)
    random_date = min(date1, date2) + datetime.timedelta(days=random_days)

    if random_date.weekday() == 0:
        print("NO VINAIGRETTE!!!!!!")

    return random_date


if __name__ == '__main__':
    print(no_vinnigrete())

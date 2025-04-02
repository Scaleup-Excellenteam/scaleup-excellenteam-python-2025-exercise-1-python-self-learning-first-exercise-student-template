import random
from datetime import datetime, timedelta

def no_vinnigrete(start_date, end_date):
    """
    This function takes two dates(start , end) and print a random date between the two dates or "No vinaigrette!" if its on Monday.
    :param start_date : start date , end_date : end date
    :return: print a random date or "No vinaigrette!"
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    if random_date.weekday() == 0:
        print("No vinaigrette!")
    else:
        print(random_date.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    no_vinnigrete(start_date, end_date)
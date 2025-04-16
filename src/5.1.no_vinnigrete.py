from datetime import datetime, timedelta
import random

def no_vinnigrette(start_date, end_date):
    """
    Generate a random date between two dates.
    If the generated date is a Monday, print a special message.
    """
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)
    print("The generated date is:", random_date.strftime("%Y-%m-%d"))
    if random_date.weekday() == 0:
        print("No vinaigrette for me!")


no_vinnigrete = no_vinnigrette

if __name__ == '__main__':
    start = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end = datetime.strptime("2023-12-31", "%Y-%m-%d")
    no_vinnigrette(start, end)

from datetime import datetime, timedelta
import random

def no_vinnigrette(start_date, end_date):
    """
    Generate a random date between two dates.
    If the generated date is a Monday, print a special message.
    """

    # Calculate the number of days between the two dates
    delta_days = (end_date - start_date).days

    # Pick a random number of days within the range
    random_days = random.randint(0, delta_days)

    # Generate the random date
    random_date = start_date + timedelta(days=random_days)

    # Print the result
    print("The generated date is:", random_date.strftime("%Y-%m-%d"))

    # If the date falls on a Monday, print the message
    if random_date.weekday() == 0:  # 0 = Monday
        print("No vinaigrette for me!")

if __name__ == '__main__':
    start = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end = datetime.strptime("2023-12-31", "%Y-%m-%d")
    no_vinnigrette(start, end)
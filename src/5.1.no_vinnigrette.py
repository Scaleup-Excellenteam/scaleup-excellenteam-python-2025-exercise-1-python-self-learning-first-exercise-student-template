import datetime
import random

def no_vinnigrete(date1, date2):
    """
    Returns a random date between two given dates (format: YYYY-MM-DD).
    """

    # Parse the input strings into datetime.date objects
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

    # Ensure the earlier date.
    earlier_date = min(date1, date2)
    latest_date = max(date1, date2)

    # Calculate the number of days between the two dates
    days_between = (latest_date - earlier_date).days

    # Generate a random number of days to add
    random_days = random.randint(0, days_between)

    # Get random date
    random_date = earlier_date + datetime.timedelta(days=random_days)

    # Check if it's Monday (0 = Monday, 6 = Sunday)
    if random_date.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")

    return random_date

if __name__ == '__main__':
    # Get input from user
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    # Get random date between the two:
    random_date = no_vinnigrete(date1, date2)

    # Print the result
    print("Random date:", random_date)

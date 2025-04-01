from datetime import datetime, timedelta
import random

def no_vinnigrete():
    """
    Generate a random date between two user-provided dates.
    If the generated date is a Monday, print a special message.

    :return: None
    """
    # Get input from the user
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")

    # Convert string input to datetime objects
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")

    # Determine the earlier and later date
    start_date = min(date1, date2)
    end_date = max(date1, date2)

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
    no_vinnigrete()
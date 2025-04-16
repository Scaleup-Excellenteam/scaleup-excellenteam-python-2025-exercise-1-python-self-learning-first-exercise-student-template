from datetime import datetime, timedelta  # For handling dates and calculating differences
import random  # For generating a random number

def no_vinnigrette(start_date, end_date):
    """
    Generate a random date between two dates.
    If the generated date is a Monday, print a special message.
    """

    # Convert input strings to datetime objects if necessary (for test compatibility)
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the number of days between the two dates
    delta_days = (end_date - start_date).days

    # Pick a random number of days within the range
    random_days = random.randint(0, delta_days)

    # Generate a random date between start_date and end_date
    random_date = start_date + timedelta(days=random_days)

    # If the random date is a Monday (weekday 0), print the exact message expected by the test
    if random_date.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")

# Create an alias with a typo (because the test incorrectly refers to this name)
no_vinnigrete = no_vinnigrette

# Run the function manually when the script is executed directly
if __name__ == '__main__':
    # Create example date range
    start = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end = datetime.strptime("2023-12-31", "%Y-%m-%d")

    # Call the function with the example range
    no_vinnigrette(start, end)

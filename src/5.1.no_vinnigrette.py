import random
from datetime import datetime, timedelta

def no_vinnigrete(start_date_str, end_date_str):
    try:
        # Convert input strings to datetime objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        # Swap dates if start is after end
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        
        # Calculate total days in range
        delta = end_date - start_date
        total_days = delta.days
        
        # Generate random day
        random_days = random.randint(0, total_days)
        random_date = start_date + timedelta(days=random_days)
        
        # Monday check (now with English message)
        if random_date.weekday() == 0:
            print("Ain't gettin' no vinaigrette today :(")
        
        return random_date.strftime("%Y-%m-%d")
    
    except ValueError:
        return "Error: Please enter valid dates in YYYY-MM-DD format"


# Test block remains the same
date1 = input("Enter start date (YYYY-MM-DD): ")
date2 = input("Enter end date (YYYY-MM-DD): ")

if __name__ == '__main__':
    result = no_vinnigrete(date1, date2)
    print(f"Random date: {result}")
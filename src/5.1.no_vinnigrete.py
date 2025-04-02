import random
from datetime import datetime, timedelta

def no_vinnigrete(start_date_str, end_date_str):

    try:
        # converting the input strings to datetime objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        # checking if the start date is after the end date
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        
        # calculating the total number of days in the range
        delta = end_date - start_date
        total_days = delta.days
        
        # generating a random day in the range
        random_days = random.randint(0, total_days)
        random_date = start_date + timedelta(days=random_days)
        
        # monday check
        if random_date.weekday() == 0:
            print("אין לי ויניגרט!")
        
        return random_date.strftime("%Y-%m-%d")
    
    # handling invalid date
    except ValueError:
        return "שגיאה: נא להזין תאריכים תקינים במבנה YYYY-MM-DD"


date1 = input("הזן תאריך התחלה (YYYY-MM-DD): ")
date2 = input("הזן תאריך סיום (YYYY-MM-DD): ")

if __name__ == '__main__':
    result = no_vinnigrete(date1, date2)
    print(f"התאריך האקראי: {result}")

from datetime import datetime, timedelta
import random


def no_vinnigrete(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    if date2 < date1:
        date1, date2 = date2, date1
    delta = date2 - date1
    random_days = random.randint(0, delta.days)
    new_date = date1 + timedelta(days=random_days)
    print(new_date.date())
    if new_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == '__main__':
    no_vinnigrete("1912-06-23", "1954-06-07")

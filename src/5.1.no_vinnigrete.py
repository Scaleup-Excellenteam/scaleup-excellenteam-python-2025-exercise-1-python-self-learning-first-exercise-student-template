#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 09:05:24 2025

@author: alon
"""

import random
import datetime

def generate_random_date(start_date: str, end_date: str):
    """
    מקבלת שני תאריכים בפורמט YYYY-MM-DD ומגרילה תאריך אקראי ביניהם.
    אם התאריך שיצא הוא יום שני, תדפיס הודעה מיוחדת.
    """
    date_format = "%Y-%m-%d"
    start = datetime.datetime.strptime(start_date, date_format)
    end = datetime.datetime.strptime(end_date, date_format)
    
    random_days = random.randint(0, (end - start).days)
    random_date = start + datetime.timedelta(days=random_days)
    
    print(f"Random date: {random_date.strftime(date_format)}")
    
    if random_date.weekday() == 0:  # 0 מייצג יום שני
        print("אין לי ויניגרט!")

def main():
# קלט מהמשתמש
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    generate_random_date(start_date, end_date)

if(__name__=='__main__'):
    main()
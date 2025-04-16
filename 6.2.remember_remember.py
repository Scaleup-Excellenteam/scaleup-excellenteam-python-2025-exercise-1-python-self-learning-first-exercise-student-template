from datetime import datetime

remembered_dates = []


def remember_remember(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        remembered_dates.append(date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


if __name__ == '__main__':
    remember_remember("2025-11-05")
    remember_remember("2024-04-01")
    print("Remembered dates:", remembered_dates)

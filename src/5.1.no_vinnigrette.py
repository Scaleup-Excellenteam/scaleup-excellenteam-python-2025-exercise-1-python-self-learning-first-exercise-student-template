from datetime import datetime
from random import randint


def no_vinnigrete(date1, date2):
    _date1 = datetime.fromisoformat(date1)
    _date2 = datetime.fromisoformat(date2)
    diff = _date2 - _date1
    my_rand = randint(0, diff.days)
    dayofweek = (_date1.weekday() + my_rand) % 7
    print("Ain't gettin' no vinaigrette today :(" if dayofweek !=
          2 else "Getting vinaigrette!")

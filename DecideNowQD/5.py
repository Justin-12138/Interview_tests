from datetime import datetime

def question_5(year, month, day):
    date = datetime(year, month, day)
    day_count = date.timetuple().tm_yday
    return day_count
year = 2024
month = 2
day = 2
day_count = question_5(year, month, day)
print("day_count:", day_count)

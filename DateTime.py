import datetime
def day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")
print(day_of_week(25,12,2024))
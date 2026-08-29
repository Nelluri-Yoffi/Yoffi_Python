from datetime import date
def daysBetweenDates(date1, date2):
    first = date.fromisoformat(date1)
    second = date.fromisoformat(date2)
    return abs((second - first).days)
print(daysBetweenDates("2019-06-29", "2019-07-30")) 
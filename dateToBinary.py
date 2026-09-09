def convert_date_to_binary(date):
    year, month, day = date.split("-")
    year_binary = bin(int(year))[2:]
    month_binary = bin(int(month))[2:]
    day_binary = bin(int(day))[2:]
    return year_binary + "-" + month_binary + "-" + day_binary
print(convert_date_to_binary("2080-02-29"))  
print(convert_date_to_binary("1900-01-01"))
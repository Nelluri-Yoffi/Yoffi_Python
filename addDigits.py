def add_digits(num):
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
    return num
print(add_digits(38))

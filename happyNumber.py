def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        n = total
    return n == 1
print(is_happy(19))  
print(is_happy(2))
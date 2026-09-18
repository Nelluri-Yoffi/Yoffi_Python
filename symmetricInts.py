def countSymmetricIntegers(low: int, high: int) -> int:
    count = 0
    for x in range(low, high + 1):
        s = str(x)
        n = len(s)
        if n % 2:                     
            continue
        half = n // 2
        if sum(map(int, s[:half])) == sum(map(int, s[half:])):
            count += 1
    return count
print(countSymmetricIntegers(1,4))
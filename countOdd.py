def countOdds(low:int, high:int) -> int:
    count = 0
    for num in range(low, high + 1):
        if num % 2 != 0:
            count += 1
    return count
print(countOdds(3,9))
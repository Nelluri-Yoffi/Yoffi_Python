def checkPerfectNumber(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total == n

print(checkPerfectNumber(28))
print(checkPerfectNumber(7))
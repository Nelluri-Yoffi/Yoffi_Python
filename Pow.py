def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    while n > 0:
        if n % 2 == 1:
            result = result * x
        x = x * x
        n = n // 2
    return result
print(myPow(2.0, 10))
print(myPow(2.0, -2))
print(myPow(3.0, 3))
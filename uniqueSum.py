def sum_zero(n):
    result = []
    for i in range(1, n // 2 + 1):
        result.append(i)
        result.append(-i)
    if n % 2 == 1:
        result.append(0)
    return result
print(sum_zero(5))   
print(sum_zero(3))   
print(sum_zero(1))
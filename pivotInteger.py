def pivot_integer(n):
    for x in range(1, n + 1):
        left_sum = 0
        for i in range(1, x + 1):
            left_sum += i
        right_sum = 0
        for i in range(x, n + 1):
            right_sum += i
        if left_sum == right_sum:
            return x
    return -1
print(pivot_integer(8))   
print(pivot_integer(1))   
print(pivot_integer(4))
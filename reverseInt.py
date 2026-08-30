def reverse(x):
    negative = x < 0
    x = abs(x)
    reversed_x = int(str(x)[::-1])
    if negative:
        reversed_x = -reversed_x
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

print(reverse(123))  
print(reverse(-123)) 
print(reverse(120))  
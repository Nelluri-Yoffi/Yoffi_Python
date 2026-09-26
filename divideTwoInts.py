def divideTwoInts(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    negative = (dividend < 0) != (divisor < 0)
    
    dvd = abs(dividend)
    dvs = abs(divisor)
    
    quotient = 0
    while dvd >= dvs:
        temp = dvs
        multiple = 1
        while dvd >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dvd -= temp
        quotient += multiple
    
    result = -quotient if negative else quotient
    return max(INT_MIN, min(INT_MAX, result))


print(divideTwoInts(3, 4))
print(divideTwoInts(3, 4))
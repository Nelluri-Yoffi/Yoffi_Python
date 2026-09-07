def to_hex(num):
    if num==0:
        return "0"
    hex_digits="0123456789abcdef"
    if num<0:
        num=num+2**32
    result=""
    while num>0:
        remainder=num % 16
        result=hex_digits[remainder] + result
        num=num // 16
    return result
print(to_hex(26))    
print(to_hex(-1))    
print(to_hex(0))
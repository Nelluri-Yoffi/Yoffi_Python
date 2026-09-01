def sum_of_digits_with_sign(n):
    digits = str(n)
    total = 0
    
    for i in range(len(digits)):
        if i % 2 == 0:
            total += int(digits[i])   
        else:
            total -= int(digits[i])   
    
    return total
print(sum_of_digits_with_sign(521))    
print(sum_of_digits_with_sign(111))   
print(sum_of_digits_with_sign(886996)) 
print(sum_of_digits_with_sign(1234))   
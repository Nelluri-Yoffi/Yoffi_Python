def arrange_coins(n):
    row = 1
    while n >= row:      
        n -= row         
        row += 1         
    return row - 1     
print(arrange_coins(1))  
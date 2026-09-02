def find_missing_and_repeating(grid):
    n = len(grid)
    count = [0] * (n * n + 1)  
    for row in grid:
        for num in row:
            count[num] += 1
    
    a = -1  
    b = -1  
    for num in range(1, n * n + 1):
        if count[num] == 2:
            a = num
        elif count[num] == 0:
            b = num
    
    return [a, b]
grid = [[1, 3], [2, 2]]
print(find_missing_and_repeating(grid)) 
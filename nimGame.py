def can_win_nim(n):
    win = [False] * (n + 1)  

    for i in range(1, n + 1):
        for take in [1, 2, 3]:
            if take <= i and win[i - take] == False:
                win[i] = True  
    return win[n]
print(can_win_nim(1))
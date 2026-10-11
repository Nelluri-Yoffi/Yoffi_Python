def fairCandySwap(aliceSizes, bobSizes):
    sumAlice = sum(aliceSizes)
    sumBob = sum(bobSizes)
    diff = (sumBob - sumAlice) // 2
    bobSet = set(bobSizes)
    for a in aliceSizes:
        b = a + diff
        if b in bobSet:
            return [a, b]
print(fairCandySwap([1, 1], [2, 2]))
print(fairCandySwap([1, 2], [2, 3]))
print(fairCandySwap([2], [1, 3]))
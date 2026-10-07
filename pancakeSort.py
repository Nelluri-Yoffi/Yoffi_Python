def pancakeSort(arr):
    flips = []
    n = len(arr)
    for size in range(n, 1, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            arr[:max_index + 1] = reversed(arr[:max_index + 1])
            flips.append(max_index + 1)
            arr[:size] = reversed(arr[:size])
            flips.append(size)
    return flips
arr = [3, 2, 4, 1]
print(pancakeSort(arr))
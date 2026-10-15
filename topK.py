def top_k_frequent(nums, k):
    counts = {}  
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    sorted_nums = sorted(counts, key=lambda x: counts[x], reverse=True)

    return sorted_nums[:k]
print(top_k_frequent([4, 4, 5, 6, 6, 6, 5, 6], 2)) 
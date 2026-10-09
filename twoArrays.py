def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result = []
    for num in set1:
        if num in set2:
            result.append(num)
    return result
print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
def smallest_range(nums, k):
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    gap = largest - smallest
    new_gap = gap - 2 * k
    if new_gap < 0:
        new_gap = 0
    return new_gap

nums = [1, 3, 6]
k = 3

print("Numbers:", nums)
print("k:", k)

result = smallest_range(nums, k)
print("Minimum score:", result)
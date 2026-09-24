def smallest_range(nums, n):
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    gap = largest - smallest
    new_gap = gap - 2 * n
    if new_gap < 0:
        new_gap = 0
    return new_gap


nums = [1, 3, 6]
n = 3

print("Numbers:", nums)
print("n:", n)

result = smallest_range(nums, n)
print("Minimum score:", result)
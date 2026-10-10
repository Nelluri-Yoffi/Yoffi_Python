def find132pattern(nums):
    stack = []
    third = float('-inf')
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < third:
            return True
        while stack and stack[-1] < nums[i]:
            third = stack.pop()
        stack.append(nums[i])
    return False
print(find132pattern([1, 2, 3, 4]))
print(find132pattern([3, 1, 4, 2]))
print(find132pattern([-1, 3, 2, 0]))
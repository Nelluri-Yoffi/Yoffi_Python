def differenceOfSum(nums):
    diff = 0
    for n in nums:
        diff += n
        while n:
            diff -= n % 10
            n //= 10
    return abs(diff)
print(differenceOfSum([1, 2, 3, 15]))
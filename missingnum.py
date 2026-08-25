def missingNumber(nums):
    n=len(nums)
    idealsum = 0
    for i in range(n+1):
        idealsum+=i
        actualsum=0
    for num in nums:
        actualsum+=num
    return idealsum-actualsum

numbers=[3,0,1]
print(missingNumber(numbers))


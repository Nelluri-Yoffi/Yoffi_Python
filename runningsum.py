def runningSum(nums):
    
    total = 0
    answer = []

    for i in range(len(nums)):
        total = total + nums[i]
        answer.append(total)

    return answer


nums = [1, 2, 3, 4]

print(runningSum(nums))
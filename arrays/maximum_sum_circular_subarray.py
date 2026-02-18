def maximumCircularSubarraySum(nums):
    curMin = 0
    curMax = 0
    globalMin = nums[0]
    globalMax = nums[0]
    total = 0

    for num in nums:
        curMax = max(curMax+num,num)
        curMin = min(curMin+num,num)
        total += num
        globalMax = max(globalMax,curMax)
        globalMin = min(globalMin,curMin)
    return max(globalMax,total-globalMin) if globalMax > 0 else globalMax

nums = [-2,4,-5,4,-5,9,4]
print(maximumCircularSubarraySum(nums))
def missing_number(nums):
    res = len(nums)
    for i in range(len(nums)):
        res+= i - nums[i]
    return res
nums = [0,2,3]
print(missing_number(nums))
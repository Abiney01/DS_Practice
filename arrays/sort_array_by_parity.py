def sortArrayByParity(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] % 2 == 0:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
    return nums

nums = [3,1,2,4]
print(sortArrayByParity(nums))
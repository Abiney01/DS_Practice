def rearrange_array(nums):
    i = 0
    j = 1
    res = [0]*len(nums)
    
    for k in range(len(nums)):
        if nums[k] > 0:
            res[i] = nums[k]
            i+=2
        else:
            res[j] = nums[k]
            j+=2
    return res

nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))
def remove_element(nums,val):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            n-=1
            nums[i] = nums[n]
        else:
            i+=1
    return n

nums = [1,1,2,3,4]
print(remove_element(nums,1))
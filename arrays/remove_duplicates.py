def remove_duplicates(nums):
    if len(nums) == 1:
        return 1
    left = 1
    right = 1
    while right < len(nums):
        if nums[right]!=nums[right-1]:
            nums[left] = nums[right]
            left+=1
        right+=1
    return left


nums = [2,10,10,30,30,30]
print(remove_duplicates(nums))
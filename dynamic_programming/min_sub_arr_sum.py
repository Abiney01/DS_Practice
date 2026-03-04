def min_sub_arr_sum(nums,target):
    left = 0
    total = 0
    res = float("inf")
    for right in range(len(nums)):
        total+=nums[right]
        while total >= target:
            res = min(res,(right-left)+1)
            total-=nums[left]
            left+=1
    return 0 if res == float("inf") else res

nums =  [2,1,5,1,5,3]
target = 10
print(min_sub_arr_sum(nums,target))
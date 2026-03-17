def minimumDifference(nums, k):
    l,r = 0,k-1
    nums.sort()
    res = float("inf")
    while r < len(nums):
        res = min(res,nums[r]-nums[l])
        l+=1
        r+=1
    return res

nums = [2,5,3,1,6,3]
k = 3
print(minimumDifference(nums,k))
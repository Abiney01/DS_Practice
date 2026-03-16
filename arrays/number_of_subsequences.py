def numSub(nums,target):
    r = len(nums)-1
    res = 0
    mod = (10**9 + 7)
    nums.sort()
    for i,l in enumerate(nums):
        while (l+nums[r]) > target and i <= r:
            r -=1 
        if i <= r:
            res += (2**(r-i))
            res %= mod
    return res

nums = [3,5,6,7]
target = 9
print(numSub(nums,target))
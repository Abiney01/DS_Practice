def splitArray(nums,k):
    def canSplit(largest):
        curSum = 0
        sub_array = 1
        for num in nums:
            curSum+=num
            if curSum > largest:
                sub_array+=1
                if sub_array > k:
                    return False
                curSum = num
        return True
    
    l = max(nums)
    r = sum(nums)
    res = r
    while l <= r:
        mid = (l + r)//2
        if canSplit(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


nums = [2,4,10,1,5]
k = 2
print(splitArray(nums,k))
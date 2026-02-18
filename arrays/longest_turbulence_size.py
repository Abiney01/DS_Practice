def longest_turbulence_size(nums):
    l = 0
    r = 1
    res = 1
    prev = ""
    while r < len(nums):
        if nums[r-1] > nums[r] and prev != ">":
            res = max(res,r-l+1)
            r+=1
            prev = ">"
        elif nums[r-1] < nums[r] and prev != "<":
            res = max(res,r-l+1)
            r+=1
            prev = "<"
        else:
            r = r+1 if nums[r] == nums[r-1] else r
            l = r-1
            prev = ""
    return res

nums = [2,4,3,2,2,5,1,4]
print(longest_turbulence_size(nums))
        
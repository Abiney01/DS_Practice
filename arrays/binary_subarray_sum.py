def binary_subarray_sum(nums,goal):
    def helper(x):
        if x < 0:
            return 0
        res = 0
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum > x:
                cur_sum -= nums[l]
                l+=1
            res += (r-l+1)
        return res
    return helper(goal) - helper(goal-1)

nums = [1,0,1,0,1]
goal = 3
print(binary_subarray_sum(nums,goal))
def four_sum(nums,target):
    nums.sort()
    quad = []
    res = []
    def kSum(start,k,target):
        if k!=2:
            for i in range(start,len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(i+1,k-1,target-nums[i])
                quad.pop()
            return 
        
        l = start
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                l+=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                res.append(quad+[nums[l],nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
    kSum(0,4,target)
    return res

nums = [3,2,3,-3,1,0]
target = 3
print(four_sum(nums,target))
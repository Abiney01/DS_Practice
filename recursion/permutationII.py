def permutationII(nums):
    res = []
    visited = [False] * len(nums)
    nums.sort()
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return 
        
        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            visited[i] = True    
            curr.append(nums[i])
            backtrack(curr)
            curr.pop()
            visited[i] = False
    
    backtrack([])
    return res

nums = [1,1,2]
print(permutationII(nums))
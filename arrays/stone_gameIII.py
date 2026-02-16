def stone_gameIII(nums):
    dp = {}
    
    def dfs(i):
        if i >= len(nums):
            return 0
        if i in dp:
            return dp[i]
        
        res = float("-inf")
        total = 0
        
        for j in range(i, min(i+3, len(nums))):
            total += nums[j]  
            res = max(res, total - dfs(j+1))
        
        dp[i] = res
        return res
    
    score = dfs(0)
    
    if score > 0:
        return "Alice"
    elif score < 0:
        return "Bob"
    else:
        return "Tie"
    
nums = [2,4,3,1]
print(stone_gameIII(nums))
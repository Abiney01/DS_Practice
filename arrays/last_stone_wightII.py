def last_stone_weightII(stones):
    stone_sum = sum(stones)
    target = stone_sum//2
    dp = [0]*(target+1)
    for stone in stones:
        for t in range(target,stone-1,-1):
            dp[t] = max(dp[t],dp[t-stone]+stone)
    return stone_sum - 2 * dp[target]

stones = [4,4,1,7,10]
print(last_stone_weightII(stones))
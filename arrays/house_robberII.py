def house_robberII(money):
    n = len(money)
    if n < 2:
        return money[0]
    skipFirst = [0] * (n-1) 
    skipLast = [0] * (n-1)
    for i in range(n-1):
        skipLast[i] = money[i]
        skipFirst[i] = money[i+1]
    
    loot_skipping_first = rob_helper(skipFirst)
    loot_skipping_last = rob_helper(skipLast)
    return max(loot_skipping_first,loot_skipping_last)


def rob_helper(money):
    n = len(money)
    if n < 2:
        return money[0]
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])
    for i in range(2,n):
        dp[i] = max(dp[i-2]+money[i],dp[i-1])
    return dp[n-1]

money = [2,9,8,3,6]
print(house_robberII(money))
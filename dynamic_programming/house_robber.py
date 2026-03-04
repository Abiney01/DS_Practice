def house_robber(money):
    n = len(money)
    if n < 2:
        return money[0]
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])
    for i in range(2,n):
        dp[i] = max(dp[i-2]+money[i],dp[i-1])
    return dp[n-1]

money = [1,1,3,3]
print(house_robber(money))
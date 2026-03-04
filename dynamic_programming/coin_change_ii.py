def coin_change(coins,amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    for i in range(len(coins)-1,-1,-1):
        for a in range(1,amount+1):
            dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
    return dp[amount]

coins = [1,2,3]
amount = 4
print(coin_change(coins,amount))

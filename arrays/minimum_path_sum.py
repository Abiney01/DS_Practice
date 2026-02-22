def minimum_path_sum(path):
    m = len(path)
    n = len(path[0])
    dp = [[float("inf")]*(n+1) for _ in range(m+1)]
    dp[m-1][n] = 0
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            dp[i][j] = path[i][j] + min(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

path = [[1,2,0],[5,4,2],[1,1,3]]
print(minimum_path_sum(path))
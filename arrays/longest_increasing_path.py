def longest_increasing_path(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    dp = {}
    def dfs(r,c,prevVal):
        if (r < 0 or r == ROWS or
            c < 0 or c == COLS or 
            matrix[r][c] <= prevVal):
            return 0
        
        if (r,c) in dp:
            return dp[(r,c)]
        
        res = 1
        res = max(res,1 + dfs(r+1,c,matrix[r][c]))
        res = max(res,1 + dfs(r-1,c,matrix[r][c]))
        res = max(res,1 + dfs(r,c+1,matrix[r][c]))
        res = max(res,1 + dfs(r,c-1,matrix[r][c]))
        dp[(r,c)] = res
        return res
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,-1)
    return max(dp.values())

matrix = [[5,5,3],[2,3,6],[1,1,1]]
print(longest_increasing_path(matrix))
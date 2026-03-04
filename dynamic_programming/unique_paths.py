def unique_paths(m,n):
    grid = [[0]*n]*m
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m-1][n-1]

m = 3
n = 6
print(unique_paths(m,n))
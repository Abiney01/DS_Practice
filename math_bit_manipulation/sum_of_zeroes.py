def sum_of_zeroes(matrix,m,n):
    total_coverage = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                coverage = 0
                for dx, dy in directions:
                    ni = i+dx
                    nj = j+dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj]==1:
                        coverage+=1
                total_coverage+=coverage
    return total_coverage

matrix = [[1,0],[0,1]]
m = 2
n = 2
print(sum_of_zeroes(matrix,m,n))

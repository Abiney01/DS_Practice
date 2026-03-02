def distinct_subsequences(s1,s2):
    dp = {}
    def dfs(i,j):
        if j == len(s2):
            return 1
        if i == len(s1):
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        if s1[i] == s2[j]:
            dp[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
        else:
            dp[(i,j)] = dfs(i+1,j)
        return dp[(i,j)]
    return dfs(0,0)

s1 = "caaat"
s2 = "cat"
print(distinct_subsequences(s1,s2))
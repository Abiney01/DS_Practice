def stone_game_ii(stones):
    dp = {}
    def dfs(alice,i,M):
        if i == len(stones):
            return 0
        if (alice,i,M) in dp:
            return dp[(alice,i,M)]

        res = 0 if alice else float("inf")
        total = 0
        for x in range(1,2*M+1):
            if i + x > len(stones):
                break
            total += stones[i+x-1]
            if alice:
                res = max(res,total+dfs(not alice,i+x,max(M,x))) 
            else:
                res = min(res,dfs(not alice,i+x,max(M,x)))
        dp[(alice,i,M)] = res
        return res
    return dfs(True,0,1)

stones = [3,1,2,5,7]
print(stone_game_ii(stones))
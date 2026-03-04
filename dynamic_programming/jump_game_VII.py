def jump_game(s,minJump,maxJump):
    n = len(s)
    if s[n-1] == "1":
        return False
    dp = [False] * n
    dp[0] = True
    j = 0
    for i in range(n):
        if dp[i] == False:
            continue

        j = max(j,i+minJump)
        while j < min(i+maxJump+1,n):
            if s[j] == "0":
                dp[j] = True
            j+=1
    return dp[n-1]

s = "00110010"
minJump = 2
maxJump = 4
print(jump_game(s,minJump,maxJump))
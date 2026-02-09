def matchsquare(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    
    length = total//4
    sides = [0] * 4
    matchsticks.sort(reverse = True)
    
    def backtrack(i):
        if i == len(matchsticks):
            return True
        for side in range(4):
            if sides[side] + matchsticks[i] <= length:
                sides[side] += matchsticks[i]
            
                if backtrack(i+1):
                    return True
            
                sides[side]-=matchsticks[i]
                if sides[side] == 0:
                    break
        return False
    return backtrack(0)


matchsticks = [1,3,4,2,2,4]
print(matchsquare(matchsticks))
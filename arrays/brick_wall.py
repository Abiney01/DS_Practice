def leastBricks(wall):
    countGap = {0:0}
    for r in wall:
        total = 0
        for pos in r[:-1]:
            total+=pos
            countGap[total] = countGap.get(total,0) + 1
    return len(wall) - max(countGap.values())

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall))
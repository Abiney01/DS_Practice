import math
def minEatingSpeed(pile,h):
    l, r = 1, max(pile)
    res = r
    while l <= r:
        k = (l + r) // 2

        totalTime = 0
        for p in pile:
            totalTime += math.ceil(float(p) / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res
pile = [1,4,3,2]
h = 9
print(minEatingSpeed(pile,h))
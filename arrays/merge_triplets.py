def mergeTriplets(triplets,target):
    result = set()
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        for i,v in enumerate(t):
            if v == target[i]:
                result.add(i)
    return len(result) == 3

triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]
print(mergeTriplets(triplets,target))
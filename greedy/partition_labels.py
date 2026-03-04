def partition_labels(s):
    lastIndex = {}
    for i,v in enumerate(s):
        lastIndex[v] = i
    size = 0
    result = []
    end = 0
    for i,v in enumerate(s):
        size+=1
        end = max(end,lastIndex[v])

        if i == end:
            result.append(size)
            size = 0

    return result

s = "xyxxyzbzbbisl"
print(partition_labels(s))
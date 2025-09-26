def topK_frequent(arr,k):
    count = {}
    freq = [[] for i in range(len(arr)+1)]
    for num in arr:
        count[num] = 1 + count.get(num,0)
    for num , cnt in count.items():
        freq[cnt].append(num)
    res= []
    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            res.append(num)
            if len(res)==k:
                return res
arr = [1,2,2,3,3,3]
k = 2
print(topK_frequent(arr,k))
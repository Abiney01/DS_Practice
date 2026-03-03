import heapq
def k_closest_point(points,k):
    minHeap = []
    for x,y in points:
        dist = (x**2) + (y**2)
        minHeap.append([dist,x,y])
    heapq.heapify(minHeap)
    res = []
    while k > 0:
        dist,x,y = heapq.heappop(minHeap)
        res.append([x,y])
        k-=1
    return res

points = [[0,2],[2,0],[2,2]]
k = 2
print(k_closest_point(points,k))
import heapq
def kth_largest_element(nums,k):
    minHeap = []
    n = len(nums)
    for i in nums:
        minHeap.append(i)
    heapq.heapify(minHeap)
    for i in range(n-k):
        heapq.heappop(minHeap)
    return minHeap[0]


nums = [2,3,1,5,4]
k = 2
print(kth_largest_element(nums,k))
import heapq
class KthLargest:
    def __init__(self,k,nums):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
    
    def add(self,val):
        heapq.heappush(self.minheap,val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
    
KthLargest_obj = KthLargest(3,[1,2,3,3])
print(KthLargest_obj.add(3))
print(KthLargest_obj.add(5))
print(KthLargest_obj.add(6))
print(KthLargest_obj.add(7))
print(KthLargest_obj.add(8))
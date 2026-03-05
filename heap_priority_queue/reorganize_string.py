import heapq
from collections import Counter
def reorganize_string(s):
    counter = Counter(s)
    maxHeap = [[-cnt,char] for char,cnt in counter.items()]
    heapq.heapify(maxHeap)
    prev = None
    res = ""
    while maxHeap or prev:
        if prev and not maxHeap:
            return ""
        cnt,char = heapq.heappop(maxHeap)
        res += char
        cnt += 1
        
        if prev:
            heapq.heappush(maxHeap,prev)
            prev = None
        if cnt != 0:
            prev = [cnt,char]
    return res

s = "cccd"
print(reorganize_string(s))
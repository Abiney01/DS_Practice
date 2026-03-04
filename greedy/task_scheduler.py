from collections import Counter
from collections import deque
import heapq
def task_scheduler(tasks,n):
    counter = Counter(tasks)
    maxHeap = [-cnt for cnt in counter.values()]
    heapq.heapify(maxHeap)
    time = 0
    q = deque()
    while maxHeap or q:
        time+=1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt,time+n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap,q.popleft()[0])
    return time

time = ["X","X","Y","Y"]
n = 2
print(task_scheduler(time,n))
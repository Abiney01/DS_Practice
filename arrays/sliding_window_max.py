from collections import deque
def sliding_window_max(arr,k):
    output = []
    q = deque()
    l = r = 0
    while r < len(arr):
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)
        if l > q[0]:
            q.popleft()
        if(r+1)>=k:
            output.append(arr[q[0]])
            l+=1
        r+=1
    return output

arr = [1,2,1,0,4,2,6]
k = 3
print(sliding_window_max(arr,k))
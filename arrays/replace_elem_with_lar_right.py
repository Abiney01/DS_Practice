def replace_elements(arr):
    n = len(arr)
    ans = [0]*n
    rightMax = -1
    for i in range(n-1,-1,-1):
        ans[i] = rightMax
        rightMax = max(arr[i],rightMax)
    return ans    
arr = [2,4,5,3,1,2]
print(replace_elements(arr))
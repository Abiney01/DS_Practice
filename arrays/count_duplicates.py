def minElementsToRemove(arr):
    arr.sort()
    removal_count = 0
    n = len(arr)
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            removal_count+=1
    return removal_count

    
arr = [1,2,3,1,2]
print(minElementsToRemove(arr))
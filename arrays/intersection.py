def intersection(arr,brr):
    i=0
    j=0
    n = len(arr)
    m = len(brr)
    intersection = []
    while i<n and j<m:
        if arr[i] == brr[j]:
            intersection.append(arr[i])
            i+=1
            j+=1
        elif arr[i] < brr[j]:
            i+=1
        else:
            j+=1
    return intersection if intersection else -1

arr = [1,2,2,2,3,4]
brr = [2,2,3,3]
print(intersection(arr,brr))

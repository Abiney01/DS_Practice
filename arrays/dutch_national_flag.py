def sort(arr,n):
    left = 0
    right = n-1
    mid = 0
    while mid<= right:
        if arr[mid] == 0:
            arr[mid],arr[left] = arr[left],arr[mid]
            mid+=1
            left+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid],arr[right] = arr[right],arr[mid]
            right-=1
    return arr
arr = [0,1,2,2,1,0]
n = len(arr)
print(sort(arr,n))
def moving_negative(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] < 0:
            left+=1
        elif arr[right] > 0:
            right-=1
        else:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
    return arr
arr = [2,3,-4,9,-2,5]
print(moving_negative(arr))



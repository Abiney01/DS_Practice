def most_water(arr):
    left = 0
    right = len(arr)-1
    max_area = 0
    while left < right:
        area = min(arr[left],arr[right]) * (right-left)
        max_area = max(area,max_area)
        if arr[left] < arr[right]:
            left+=1
        else:
            right-=1
    return max_area
arr = [4,3,2,1,4]
print(most_water(arr))
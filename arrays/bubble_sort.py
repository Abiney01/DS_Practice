def bubble_sort(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
        if swapped == False:
            break
    return arr
arr = [6,2,8,4,10]
n = 5
print(bubble_sort(arr,n))
    
def selection_sort(arr,n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]< arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr
arr = [6,2,8,4,10]
n = 5
print(selection_sort(arr,n))

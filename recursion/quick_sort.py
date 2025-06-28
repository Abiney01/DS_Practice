def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x>= pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr = [2,3,6,4,1]
print(quick_sort(arr))







# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low-1
#     for j in range(low,high):
#         if arr[j] < pivot:
#             i+=1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i+1


# def quick_sort(arr,low,high):
#     if low<high:
#         pivot_index = partition(arr,low,high)
#         quick_sort(arr,low,pivot_index-1)
#         quick_sort(arr,pivot_index+1,high)
#     return arr

arr= [2,3,4,1,5]
low = 0
high = 4
# print(quick_sort(arr,low,high))
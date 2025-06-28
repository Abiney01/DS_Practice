def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_sorted(left,right,arr)

def merge_sorted(arr1,arr2,arr):
    k = 0
    i = 0
    j = 0
    while i <len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1
    while i < len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1
    return arr
arr = [2,4,1,3,7,6,8]
print(merge_sort(arr))


def merge(nums1, m, nums2, n):
        i = m-1 
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i] 
                i-=1
            else:
                nums1[k] = nums2[j] 
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j] 
            j-=1
            k-=1
        return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1,m,nums2,n))
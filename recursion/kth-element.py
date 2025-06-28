def k_element(arr1,arr2,k):
    arr1 = arr1+arr2
    arr1.sort()
    print(arr1)
    return arr1[k-1]
arr1 = [1,4,7,10]
arr2 = [2,5,6]
k = 4
print(k_element(arr1,arr2,k))
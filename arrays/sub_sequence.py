def sub_sequence(arr1,arr2):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            i+=1
        j+=1
    return i == len(arr1)
arr1 = ['AE']
arr2 = ['BADE']
print(sub_sequence(arr1,arr2))

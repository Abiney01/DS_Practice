def majority_element(arr):
    count = 0
    candidate = 0
    for num in arr:
        if count == 0:
            candidate = num
        count+=(1 if candidate==num else -1)
    if arr.count(candidate) > len(arr)//2:
        return candidate
    return -1 
arr = [2,3,9,2,2]
print(majority_element(arr))
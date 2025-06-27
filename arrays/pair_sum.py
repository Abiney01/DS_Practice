def pairSum(arr, target):
    left = 0
    right = len(arr)-1
    count = 0
    while left<right:
        curr_sum = arr[left] + arr[right]
        if curr_sum== target:
            left+=1
            right-=1
            count+=1
        elif curr_sum < target:
            left+=1
        else:
            right-=1
    return count if count>0 else -1
arr = [1,2,3,4,5,6]
target = 6
print(pairSum(arr,target))

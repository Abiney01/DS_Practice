def max_subArray(arr):
    max_Sub = arr[0]
    curr_sum = 0
    for i in arr:
        curr_sum+=i
        if curr_sum  <0:
            curr_sum = 0
        max_Sub = max(curr_sum,max_Sub)
    return max_Sub
arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(max_subArray(arr))
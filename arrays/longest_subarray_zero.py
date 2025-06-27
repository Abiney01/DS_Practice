def LongestSubsetWithZeroSum(arr):
    max_length = 0
    sub_array = {}
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum == 0:
            max_length = i+1
        if prefix_sum in sub_array:
            max_length = max(max_length,i-sub_array[prefix_sum])
        else:
            sub_array[prefix_sum] = i 
    return max_length

arr = [1,3,-1,4,-4]
print(LongestSubsetWithZeroSum(arr))


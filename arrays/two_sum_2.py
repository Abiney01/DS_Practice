def two_sum_2(arr,target):
    nums_map = {}
    for i , j in enumerate(arr):
        complement = target - j 
        if complement in nums_map:
            return [nums_map[complement]+1,i+1]
        nums_map[j] = i

arr = [2, 7, 11, 15]
target = 9
print(two_sum_2(arr,target))
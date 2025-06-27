from collections import defaultdict
def sub_array_sum_divisible(arr,k):
    prefix_sum = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    count = 0
    for i in arr:
        prefix_sum+=i
        remain = prefix_sum % k
        if remain in prefix_count:
            count+=prefix_count[remain]
        prefix_count[remain]+=1
    return count

arr = [4,5,0,-2,-3,1]
k = 5
print(sub_array_sum_divisible(arr,k))
        

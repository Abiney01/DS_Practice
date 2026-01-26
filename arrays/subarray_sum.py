from collections import defaultdict
def subarraySum(nums, k):
    prefix_sum = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    count = 0

    for i in nums:
        prefix_sum += i
        remain = prefix_sum - k

        if remain in prefix_count:
            count += prefix_count[remain]

        prefix_count[prefix_sum] += 1   

    return count

nums = [1,2,3]
k = 3
print(subarraySum(nums,k))
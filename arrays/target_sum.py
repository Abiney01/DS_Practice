from collections import defaultdict
def target_sum(nums,target):
    dp = defaultdict(int)
    dp[0] = 1
    for num in nums:
        new_dp = defaultdict(int)
        for total,count in dp.items():
            new_dp[total+num] += count
            new_dp[total-num] += count
        dp = new_dp
    return dp[target]

nums = [2,2,2]
target = 2
print(target_sum(nums,target))
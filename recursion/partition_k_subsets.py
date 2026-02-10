def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False

    target = total // k
    nums.sort(reverse=True)

    if nums[0] > target:
        return False

    used = [False] * len(nums)

    def backtrack(start, subsetSum, k):
        if k == 1:
            return True  

        if subsetSum == target:
            return backtrack(0, 0, k - 1)

        for i in range(start, len(nums)):
            if used[i] or subsetSum + nums[i] > target:
                continue

            used[i] = True
            if backtrack(i + 1, subsetSum + nums[i], k):
                return True
            used[i] = False

            # pruning: avoid duplicate empty subset attempts
            if subsetSum == 0:
                break

        return False

    return backtrack(0, 0, k)

nums = [2,4,1,3,5]
k = 3
print(canPartitionKSubsets(nums,k))
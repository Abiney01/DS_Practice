def subsetsII(nums):
    nums.sort()
    result = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            if subset not in result:
                result.append(subset.copy())
            return
        subset.append(nums[i])
        backtrack(i+1)

        subset.pop()
        backtrack(i+1)

    backtrack(0)
    return result

nums = [1,2,2]
print(subsetsII(nums))
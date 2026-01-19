def plus_one(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        nums[i] = 0

    return [1] + nums

nums = [1,2,3,9]
print(plus_one(nums))
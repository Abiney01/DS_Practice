def firstMissing(nums, n):
    i = 0
    while i < n:
        correct_pos = nums[i] - 1  # Expected index for nums[i]
        if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]  # Swap to correct position
        else:
            i += 1

    # Find the missing number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
nums = [9,6,4,2,3,5,7,0,1]
print(firstMissing(nums,9))
def subsetXOR(nums):
    res = 0
    for n in nums:
        res = res | n
    return res * 2**(len(nums)-1)

nums = [5,1,6]
print(subsetXOR(nums))
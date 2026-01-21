def single_number(nums):
    res = 0
    for num in nums:
        res = num ^ res
    return res

num = [3,2,3]
print(single_number(num))
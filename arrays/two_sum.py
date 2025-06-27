def twoSum(nums, target):
    num_map = {}
    for index,value in enumerate(nums):
        result = target - value
        if result in num_map:
            return [num_map[result],index]
        num_map[value] = index
nums = [3,2,4]
target = 6
print(twoSum(nums,target))  
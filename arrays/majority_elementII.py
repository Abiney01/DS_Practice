from collections import defaultdict
def majority_elementII(nums):
    count = defaultdict(int)
    for i in nums:
        count[i]+=1
        if len(count) <= 2:
            continue
        new_count = defaultdict(int)
        for num , c in count.items():
            if c > 1:
                new_count[num] = c - 1
        count = new_count
    
    res = []
    for num in count:
        if nums.count(num) > len(nums)//3:
            res.append(num)
    return res
        
nums = [5,2,3,2,2,2,2,5,5,5]
print(majority_elementII(nums))
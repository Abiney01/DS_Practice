from collections import Counter
def hands_straight(nums,groupSize):
    if len(nums) % groupSize:
        return False
    count = Counter(nums)
    nums.sort()
    for num in nums:
        if count[num] :
            for i in range(num,num+groupSize):
                if not count[i]:
                    return False
                count[i]-=1
    return True

nums = [1,2,4,2,3,5,3,4]
groupSize = 4
print(hands_straight(nums,groupSize))
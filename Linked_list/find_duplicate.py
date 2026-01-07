# This problem seems to be a normal array problem at first, but it is not, it's based on the concept of linked list, the duplicate values in the nums array is the cycle

def find_duplicate(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

nums = [1,2,3,2,2]
print(find_duplicate(nums))
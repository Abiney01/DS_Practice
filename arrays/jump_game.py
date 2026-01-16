def canJump(nums):
        final_position = len(nums)-1
        for index in range(len(nums)-2,-1,-1):
            if (index + nums[index]) >= final_position:
                final_position = index
        return final_position == 0

nums = [1,2,0,1,0]
print(canJump(nums))
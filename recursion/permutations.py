def permutations(nums):
    result = []

    def backtrack(curr,nums,result):
        if len(curr) == len(nums):
            result.append(curr.copy())
            return 
        
        for i in nums:
            if i in curr:
                continue
            curr.append(i)
            backtrack(curr,nums,result)
            curr.pop()
    
    backtrack([],nums,result)
    return result
        

nums = [1,2,3]
print(permutations(nums))
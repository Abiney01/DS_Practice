from typing import List
def combination_sum(candidates:List[int],target:int)->List[int]:
    result = []

    def backtrack(start:int,current:List[int],total:int):
        if total == target:
            result.append(list(current))
            return
        
        if total > target:
            return 
        
        for i in range(start,len(candidates)):
            current.append(candidates[i])
            backtrack(i,current,total+candidates[i])
            current.pop()

    backtrack(0,[],0)
    return result
candidates = [2,3,5]
target = 8
print(combination_sum(candidates,target))
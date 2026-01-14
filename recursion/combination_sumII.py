def combinationSum2(candidates, target):
        candidates.sort()
        result = []

        def backtrack(pos,curr,target):
            if target == 0:
                result.append(curr.copy())

            if target <= 0:
                return 

            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr,target-candidates[i])
                curr.pop()
                prev = candidates[i]
        backtrack(0,[],target)
        return result

candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum2(candidates,target))

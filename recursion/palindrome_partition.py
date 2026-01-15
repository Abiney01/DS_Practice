def partition(s):
        result = []
        part = []

        def backtrack(i):
            if i >= len(s):
                result.append(part.copy())
                return 
            
            for j in range(i,len(s)):
                if isPali(s,i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        backtrack(0)
        return result
    
def isPali(s,l,r):
    while l < r:
        if s[l] != s[r]:
            return False
        l,r = l+1, r-1
    return True

s = "aab"
print(partition(s))
        
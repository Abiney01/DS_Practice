def solveNQueens(n):
        col = set()
        posDia = set()
        negDia = set()
        result = 0

        def backtrack(r):
            if r == n:
                nonlocal result
                result+=1
                return 
            
            for c in range(n):
                if c in col or (r+c) in posDia or (r-c) in negDia:
                    continue
                
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                backtrack(r+1)
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)

        backtrack(0)
        return result

print(solveNQueens(4))
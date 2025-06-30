from typing import List

def generateString(N: int) -> List[str]:
    result = []
    
    def backtrack(current: str):
        if len(current) == N:
            result.append(current)
            return
        
        # Always add '0'
        backtrack(current + '0')
        
        # Add '1' only if last character is not '1'
        if not current or current[-1] != '1':
            backtrack(current + '1')

    backtrack("")
    return result
N = 2
print(generateString(N))
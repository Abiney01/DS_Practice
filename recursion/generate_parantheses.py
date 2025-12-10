from typing import List

def generate_parantheses(n:int) -> List[str]:
    result = []
    def backtrack(current:str,open_count:int,close_count:int):
        if open_count < 1 and close_count < 1:
            result.append(current)

        # Always add "("
        if open_count > 0 :
            backtrack(current+'(',open_count-1,close_count)

        # Add ")" only if it's greater than open_count
        if close_count > open_count:
            backtrack(current+')',open_count,close_count-1)

    backtrack("",n,n)
    return result

n = 2
print(generate_parantheses(n))
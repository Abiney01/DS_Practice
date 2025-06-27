def isValidParenthesis(s: str) -> str:
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        elif i == '{':
            stack.append('}')
        elif not stack or stack.pop() != i:  # Fix: Check empty stack before popping
            return "Not Balanced"

    return "Balanced" if not stack else "Not Balanced"

# Sample Test Cases
print(isValidParenthesis("[()]{}{[()()]()}"))  # ✅ Balanced
print(isValidParenthesis("[[}[") )  # ✅ Not Balanced

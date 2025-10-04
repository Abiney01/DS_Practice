def reverse_polish_notations(expr):
    stack = []
    for i in expr:
        if i == "+":
            stack.append(stack.pop()+stack.pop())
        elif i == "-":
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif i == "*":
            stack.append(stack.pop()*stack.pop())
        elif i == "/":
            a,b = stack.pop(),stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack[0]

expr = ["1","2","+","3","*","4","-"]
print(reverse_polish_notations(expr))
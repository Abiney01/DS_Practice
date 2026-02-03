def baseball_game(operations):
        stack = []
        for i in operations:
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(stack[-1]*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)

operations = ["5","2","C","D","+"]
print(baseball_game(operations))